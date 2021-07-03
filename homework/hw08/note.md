https://www.youtube.com/watch?v=-C8RUrWb7F8

Autoencoder 通常用來降低高維度的資料，讓資料被投射在一個比較容易被分開的空間。以圖片為例, Autoencoder 會將高維度的資料投射到低維，在讓模型利用這些低維的資料，畫出一張和原本的一樣的圖片。這樣就能夠確保，雖然圖片降到低維還是保有應該要有的資訊。
然而，跟 SVD 這些使用統計學來降為的方法不同，Autoencoder 只有在與訓練資料相似的資料上表現的很好。GANomaly 卻把這個本來應該是缺點的特性拿來做異常偵測。
GANomaly 只用正常的資料訓練 Autoencoder，所以我們可以預期這個 Autoencoder 只有在測試資料是正常時，才在重畫出一張相似的圖片。當畫出來的資料不像原本的圖時，我們就判斷他為異常資料。

https://www.youtube.com/watch?v=9zKuYvjFFS8

https://zhuanlan.zhihu.com/p/61935975
1. Novelty Detection

中文翻译过来 新奇检测，不完全等同于异常检测。通俗来讲就是训练样本中只有单类（one-class）样本，测试中需要检测到不属于该类的样本。常用的方法有基于差异度量（重构误差）和基于分布（GMM）。对于基于距离度量方法，常用就是auto-encoder，通过单类样本训练一个AE，我们期望它对该类重构的误差越小越好，同时对于其他类样本，由于训练过程中没有见过，产生的重构误差应该较大。

但这有个问题，AE的capacity比较强，很难保证对于其他类样本重构较差，这在其他文献中也有出现（参考here）。该文作者发现，我们不仅需要1)单类样本在隐空间（latent space）中被很好表示，2)同时希望其他类样本在该空间不能被很好表示。之前的工作大部分局限在前半部分1)，而忽视了后半部分2）。基于此，作者提出自己的构想--->>如果整个隐空间被限制为表示给定类的图像，那么其他类(outof- class)样本的表示将认为在该空间几乎不存在(minimal)——从而为它们产生很高重构误差。

https://www.youtube.com/watch?v=Tk5B4seA-AU

https://blog.csdn.net/dhaiuda/article/details/102882786

min score is 0.5

there're too many kind of ways to calculate the abnomal score and to construct the loss function