import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

class VAE(nn.Module):
    def __init__(self, latent_dim=128, no_of_sample=10, batch_size=32, channels=3, image_size=64):
        super(VAE, self).__init__()

        self.no_of_sample = no_of_sample
        self.batch_size = batch_size
        self.channels = channels
        self.latent_dim = latent_dim
        self.image_size = image_size

        # Encoder
        def convlayer_enc(n_input, n_output, k_size=4, stride=2, padding=1, bn=False):
            block = [nn.Conv2d(n_input, n_output, kernel_size=k_size, stride=stride, padding=padding, bias=False)]
            if bn:
                block.append(nn.BatchNorm2d(n_output))
            block.append(nn.LeakyReLU(0.2, inplace=True))
            return block

        # Calculate the number of encoding layers based on image size.
        enc_layers = 0
        temp_size = image_size
        while temp_size > 4:
          temp_size //= 2
          enc_layers += 1

        encoder_layers_list = []
        n_channels = [channels, 64, 128, 256, 512]
        for i in range(enc_layers):
            bn = True if i >= 2 else False
            encoder_layers_list.extend(convlayer_enc(n_channels[i], n_channels[i+1], 4, 2, 2, bn=bn))
        encoder_layers_list.append(nn.Conv2d(n_channels[-1], self.latent_dim * 2, 4, 1, 1, bias=False))
        encoder_layers_list.append(nn.LeakyReLU(0.2, inplace=True))

        self.encoder = nn.Sequential(*encoder_layers_list)


        # Decoder
        def convlayer_dec(n_input, n_output, k_size=4, stride=2, padding=0):
            block = [
                nn.ConvTranspose2d(n_input, n_output, kernel_size=k_size, stride=stride, padding=padding, bias=False),
                nn.BatchNorm2d(n_output),
                nn.ReLU(inplace=True),
            ]
            return block
        
        # Calculate the number of decoding layers based on image size
        decoder_layers_list = []
        n_channels = [self.latent_dim, 512, 256, 128, 64]
        for i in range(enc_layers - 1):
          decoder_layers_list.extend(convlayer_dec(n_channels[i], n_channels[i+1], 4, 2, 1))
        
        decoder_layers_list.append(nn.ConvTranspose2d(n_channels[-1], self.channels, 3, 1, 1))
        decoder_layers_list.append(nn.Sigmoid())

        self.decoder = nn.Sequential(*decoder_layers_list)
        

    def encode(self, x):
        '''return mu_z and logvar_z'''
        x = self.encoder(x)
        return x[:, :self.latent_dim, :, :], x[:, self.latent_dim:, :, :]

    def decode(self, z):
        z = self.decoder(z)
        return z.view(-1, self.channels * self.image_size * self.image_size)

    def reparameterize(self, mu, logvar):
        if self.training:
            sample_z = []
            for _ in range(self.no_of_sample):
                std = logvar.mul(0.5).exp_()
                eps = Variable(std.data.new(std.size()).normal_())
                sample_z.append(eps.mul(std).add_(mu))
            return sample_z
        else:
            return mu

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)

        if self.training:
            return [self.decode(z) for z in z], mu, logvar
        else:
            return self.decode(z), mu, logvar

    def loss_function(self, recon_x, x, mu, logvar):
        if self.training:
            BCE = 0
            for recon_x_one in recon_x:
                BCE += F.binary_cross_entropy(recon_x_one, x.view(-1, self.channels * self.image_size * self.image_size))
            BCE /= len(recon_x)
        else:
            BCE = F.binary_cross_entropy(recon_x, x.view(-1, self.channels * self.image_size * self.image_size))

        KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
        KLD /= self.batch_size * self.channels * self.image_size * self.image_size

        return BCE + KLD