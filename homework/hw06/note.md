# GAN
the history of GAN
https://www.infoq.cn/article/gcgibopiftpbe9deqf3m

youtube GAN implementation
https://www.youtube.com/playlist?list=PLhhyoLH6IjfwIp8bZnzX8QR30TRcHO8Va

colab pro
https://colab.research.google.com/notebooks/pro.ipynb#scrollTo=V1G82GuO-tez

SAGAN, BigGAN, SinGAN, GauGAN, GANILLA, NICE-GAN
https://www.youtube.com/watch?v=hTNE8iFXEMU

some tips
https://github.com/soumith/ganhacks#authors

## GAN
- latent space
- using fixed noise to see how generator improve
- using BCELoss
- using transform.normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
  - which project the image range 
- using tanh in generator
- 3e-4 is the best learning rate for Adam
- GAN is sensitive to hyperparameter

## DCGAN
- generator
  - (100) -> (1024, 4, 4) -> (512, 8, 8) -> (256, 16, 16) -> (128, 32, 32) -> (3, 64, 64)
- discriminator
  - looks the same as generator but opposite
- replacing pooling layers with strided convolution (discriminator) and fractional-strided convolution (generator)
- using batchnorm
- remove fully connected hidden layers for deeper architetures
- use ReLU in generator for all layers except for the output, which uses Tanh
- use LeakyReLU in discriminator for all layers
- there're some others hyperparamters suggeted by the paper
  - they also have there own specific initialization method
- when you are using batchnorm, you can cancel the bias of the previous layer
  - since bn will center the values, bias is useless because it'll be canceled by bn
### deconv
X: kernel
O: input
@: kernel + input

(kernel_size=4, stride=1, padding=0) make 1x1 -> 4x4
XXXX
XXXX
XXXX
XXX@

(kernel_size=4, stride=2, padding=1) make 4x4 -> 8x8
XXXX
XXXX
XX@XO O O
XXXX
  O O O O

  O O O O

  O O O O

(kernel_size=2, stride=2, padding=0) make 4x4 -> 8x8
XX
X@ O O O

 O O O O

 O O O O

 O O O O

(kernel_size=3, stride=1, padding=1) make 4x4 -> 4x4
XXX
X@@OO
X@@OO
 OOOO
 OOOO

## WGAN
- pros
  - better stability
    -prevent mode collapse
  - loss mean something
  - termination criteria
- cons
  - longer to train
    - however, it is more stability, it takes less time to find a good hyperparameters
- there're lots of way to calculate the similarity of two distribution
  - the distribution in the vector space with the same dimension of image
- WGAN use Wasserstein distance instead of JS divergence
  - the loss calculated by JS divergence is meaningless
  - the loss used in WGAN mean something by which we can train model more stable
- when loss of discriminator goes to zero, the discriminator cannot distinguish two type of picture
- train the critic more than the generator
- using weight clipping of critic can achieve the constrain required
- however, weight clipping is a terrible way to enforce the constraint
- gradient penalty is a better way to enforce the constraint
- spectral normalization
  - Spectral normalization helps improve the model quality and is more computationally efficient than gradient penalty

## PROGAN
- progressive
- minibatch std (standard deviation)
  - increase variation
- pixelnorm
  - it is a heavy handed constraint
  - however, it doesnt harm the model a lot
  - and it can prevent signals escalating(?)
- equalize learning rate
  - solve the problem of optimizer
  - however, it haven't be seen in other papers
- the result is independent with the loss function
  - though, they use loss used by WGAN-GP
- in the official code, they do batch repeat = 4
  - for one batch, they do 4 update step
  - however, they didn't metion it in the paper
- he initialization

## Super Resolution

in the beginning of fadding in, gen doesn't give good output. However, the critic give gen good score. Maybe we need to update critic more.

it doesn't garantee that there's a nash equilibrium in GAN