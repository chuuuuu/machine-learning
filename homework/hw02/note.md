- what activation function is better for classify nn?
    - relu > tanh > sigmoid (?)
    - you can begin with using ReLU and then move over to other activation functions in case ReLU doesn't provide with optimum results
- with huge amount data, how should we choose model?
    - too much data -> spend too much time on training
    - maybe we can do k-fold validation with k=2, since there're huge amount of data
- how many layer should we have?
    - is there an SOP?
        - for example, we need to train from the simplest to complexest
            - observe if overfitting or underfitting
            - but it would spend too much time
- what nn artitecture should we build?
    -   there are too much combination of artitecture, are there any good rule to choose?
- deep learning rules of thumb
    - https://jeffmacaluso.github.io/post/DeepLearningRulesOfThumb/
- more data can make loss lower, however, there's a limitation.
    - hence, when data is big enough, it'll be fine to use 20% of data as validation(?)
- we should add early stopping for every training.
    - what metric should we concern?
        - loss or accuracy?
            - maybe it should be loss
- smote
- You need at least 5,000 observations per category for acceptable performance (>=10 million for human performance or better).
- A collection of various deep learning architectures, models, and tips for TensorFlow and PyTorch in Jupyter Notebooks.
    - https://github.com/rasbt/deeplearning-models

- https://github.com/rasbt/deeplearning-models

- unbalanced data
    - using weight loss with [1 / num_data_in_class_i for i in range(num_class)]
    - split train and test with same distribution
    - early stopping with loss

- good performance on training set and validation set, but not on testing set. why?
    - however, i've already use cross-validation to make sure im not just lucky.
    - and i've use loss-weighted to make sure none of the class would be ignored.

- what happend when both of loss and accuracy of validation increasing in the end part?
    - maybe data is skew(imbalance)
    - the model will try to be more and more confident to minimize loss
        - model become over-confident (which is nature)