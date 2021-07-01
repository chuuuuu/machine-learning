- self-training problem
    - may encounter over confidence problem(?)
    - it's important to make sure dataset is balanced
        - appending same (ratio of)number of data for each class

- there're exists tons of great model
    - alexnet, vgg, resnet...etc

- in this homework, i try to use vgg model

- how to improve weak class?
    - adaboost
        - https://www.youtube.com/watch?v=LsK-xG1cLYA
        - decision tree
            - https://www.youtube.com/watch?v=7VeUPuFGJHk
            - good at training data, but bad at validation data
        - random forest
            - https://www.youtube.com/watch?v=J4Wdy0Wc_xQ
            - bootstrap(randomly select data) + aggregate(majority vote) = bagging

- Mixed Precision
    - we don't need to save every float number with 64 bits
    - can save memeory and speed up
    - can be implemented by torch.cuda.amp.autocast & torch.cuda.amp.GradScaler
        - however, there's gradient explosion problem

- when appending unlabeled data to training data
    - testing data can also be appended
    - make sure data is balanced after appending
        - if it's lack of data of some specific class, then using weighted loss

- use transfer learning
    - convolution layer is for encoding (get the attribute)
        - reuse these layers to make training faster

- script
    - run HW03_pretrain.ipynb
    - run HW03_ensemble.ipynb