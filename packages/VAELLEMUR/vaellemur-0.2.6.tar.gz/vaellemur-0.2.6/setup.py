from setuptools import setup

setup(
    name='VAELLEMUR',
    version='0.2.6',    
    description='VAE for LLEMUR',
    url='https://github.com/Qwest1204/LLEMUR',
    author='Daniil Ogorodnikov',
    author_email='128bit@128bit.xyz',
    license='Apache 2.0',
    packages=['VAE'],
    install_requires=['torch',
                      'torchvision',
                      'ray',
                      'torchinfo',
                      'torchmetrics',
                      'tqdm',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)