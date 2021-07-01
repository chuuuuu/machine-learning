# Note
- bias-variance trade-off
    - overfitting is high variance
    - bad performance on training set is high bias

- scaling
    - feature scaling
        - if the features are not scaled
            - some of the features may be much bigger than others
            - and play a more important role than others
            - however, it should be avoided
        - notice that, we need to give the same mean & variation to train/ val/ test set
    - batch normalization 
        - we should not only scale feature, but also scale the hidden layers
            - it can solve the internal covariate shift problem
        - we should do it before activation function
            - make sure params are inside the active region
                - less exploding/ vanishing gradients
        - batch size should be big enough
            - since nn do the normalization for each batch
        - what happen when testing?
            - computing moving average of mean and variance during training
        - less affected by initialization
        - it can help when training loss is big

- training not converge:
    - more data
    - use corresponding model

- how to improve training loss
    - reduce model bias
        - make the model more complex
    - optimization
        - momentem
        - adjust learning rate with weight(current & previous)

- how to improve testing loss
    - more training data
        - collect more data
            - which is not allowed in this class
        - data augmentation
            - it'll be useful for cnn
                - white noise
                - rotate the picture
    - regulization
        - dropout
        - weight-decay
    - early stopping
    - detect if overfitting
        - simplify the model
            - feature selection
    - cross-validation
        - it is important since the distribution between each set might be slightly different
        - if you dont do the cross validation, you may do a great job on specific validation set, however, that's just lucky.
    - sometimes, the distribution between training set & testing set are different

- Adam
    - adjust learning rate with weight(current & previous)
    - weight-decay

- dropout
    - usually, p = 0.2 ~ 0.5
        - larger prob for larger nn
    - take long time to converge
    - high dropout rate -> hard to converge
        - use dynamic learning rate can solve it
    - used after activation function

- batch normalization
    - batch_size cannot be small

- if you have only a few data, try make whole data into batch size

- validation loss might be better than training loss
    - since validation data is more easily to predict

- why deep not shallow
    - deep imply heirachy, let diff layer learn diff things (modulization)

- suppose i do cross-validation with k=5, but i wanna do training with train_validation_ratio = 10
    - is it reasonable?
    - sometimes, the loss are quite different between two different ratio

- it's better to make sure every hyperparams are in config!
    - or you might forget what you just modified

- how to decide which validation set is to be used in early stopping

- colab
    - 利用checkpoint解決colab自動斷線問題
    - colab每日有12小時額度限制
- batch_size開最大（2700），總是有最好的結果

5 & 6 & 7

8: the best, testing loss: 0.88525

- learning rate & weight decay還是很重要，需要調整
    - 並不是adam就能做到完美（至少對於small data是如此）

- 儘管train和val都學得很好（都到0.82），testing也有可能差(0.90)
    - 以到strong base line 為目標 然後調整weight decay

- 越複雜的nn需要越大的weight decay才能避免overfitting