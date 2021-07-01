# HW3
In this homework, there are two .ipynb files.
In HW03_pretrain.ipynb, I train a model which is used as the pretrained model in the HW03_emsembler.ipynb.
In HW03_emsembler.ipynb, I train 5 models and combine all of them into a ensembler.
Notice that, all of the convolutional layers of those 5 models are initialized by the pretrained model trained in HW03_pretrain.ipynb.

## Instructions
1. run HW03_pretrain.ipynb until val_acc > 0.79
2. run HW03_ensemble.ipynb for 30 epochs

## Comment
I run my code in colab environment, and it is easily to be disconnected. Hence, I run my code for unknown time to get the result. However, I didn't store the optimizer state and labels of unlabeled data. Moreover, I think that rerunning the code can improve the model performance because I can relabel those unlable data with better model. Additionaly, I think relabling is one of the important features in noisy student which is published by google. Therefore, I believe that it is hard to reproduce the result.