
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
        self.image_size = image_size  # Добавили размер изображения

        # Функция для вычисления размерности после свертки/транспонирования
        def calculate_output_size(input_size, kernel_size, stride, padding):
            return (input_size + 2 * padding - kernel_size) // stride + 1

        # Encoder
        def convlayer_enc(n_input, n_output, k_size=4, stride=2, padding=1, bn=False):
            block = [nn.Conv2d(n_input, n_output, kernel_size=k_size, stride=stride, padding=padding, bias=False)]
            if bn:
                block.append(nn.BatchNorm2d(n_output))
            block.append(nn.LeakyReLU(0.2, inplace=True))
            return block
       
        # Вычисление размерностей для сверточных слоев
        enc_output_sizes = []
        current_size = self.image_size
        enc_output_sizes.append(calculate_output_size(current_size, 4, 2, 2)) 
        current_size = enc_output_sizes[-1]
        enc_output_sizes.append(calculate_output_size(current_size, 4, 2, 2)) 
        current_size = enc_output_sizes[-1]
        enc_output_sizes.append(calculate_output_size(current_size, 4, 2, 2))
        current_size = enc_output_sizes[-1]
        enc_output_sizes.append(calculate_output_size(current_size, 4, 2, 2)) 
        current_size = enc_output_sizes[-1]
        

        self.encoder = nn.Sequential(
            *convlayer_enc(self.channels, 64, 4, 2, 2),  # (64, enc_output_sizes[0], enc_output_sizes[0])
            *convlayer_enc(64, 128, 4, 2, 2),           # (128, enc_output_sizes[1], enc_output_sizes[1])
            *convlayer_enc(128, 256, 4, 2, 2, bn=True),   # (256, enc_output_sizes[2], enc_output_sizes[2])
            *convlayer_enc(256, 512, 4, 2, 2, bn=True),   # (512, enc_output_sizes[3], enc_output_sizes[3])
            nn.Conv2d(512, self.latent_dim * 2, 4, 1, 1, bias=False),  # (latent_dim*2,  enc_output_sizes[3], enc_output_sizes[3])
            nn.LeakyReLU(0.2, inplace=True)
        )
      

        # Decoder
        def convlayer_dec(n_input, n_output, k_size=4, stride=2, padding=0):
            block = [
                nn.ConvTranspose2d(n_input, n_output, kernel_size=k_size, stride=stride, padding=padding, bias=False),
                nn.BatchNorm2d(n_output),
                nn.ReLU(inplace=True),
            ]
            return block
        
         # Вычисление размерностей для транспонированных сверточных слоев
        dec_input_sizes = []
        current_size = enc_output_sizes[3]
        dec_input_sizes.append(current_size)
        dec_input_sizes.append(calculate_output_size(dec_input_sizes[-1] , 4, 2, 1))
        dec_input_sizes.append(calculate_output_size(dec_input_sizes[-1] , 4, 2, 1))
        dec_input_sizes.append(calculate_output_size(dec_input_sizes[-1] , 4, 2, 1))
        dec_input_sizes.append(calculate_output_size(dec_input_sizes[-1] , 4, 2, 1))


        self.decoder = nn.Sequential(
            *convlayer_dec(self.latent_dim, 512, 4, 2, 1),           # (512, dec_input_sizes[1], dec_input_sizes[1])
            *convlayer_dec(512, 256, 4, 2, 1),                       # (256, dec_input_sizes[2], dec_input_sizes[2])
            *convlayer_dec(256, 128, 4, 2, 1),                       # (128, dec_input_sizes[3], dec_input_sizes[3])
            *convlayer_dec(128, 64, 4, 2, 1),                        # (64, dec_input_sizes[4], dec_input_sizes[4])
            nn.ConvTranspose2d(64, self.channels, 3, 1, 1),          # (3, self.image_size, self.image_size)
            nn.Sigmoid()
        )

    def encode(self, x):
        '''return mu_z and logvar_z'''
        x = self.encoder(x)
        return x[:, :self.latent_dim, :, :], x[:, self.latent_dim:, :, :]

    def decode(self, z):
         z = self.decoder(z)
         return z.view(-1, self.channels * self.image_size * self.image_size)

    def reparameterize(self, mu, logvar):
        if self.training:
            # multiply log variance with 0.5, then in-place exponent
            # yielding the standard deviation

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