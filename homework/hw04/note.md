- elmo
    - contexualize word embedding
- bert
    - transformer encoder
    - ernie
        - chinese version of bert
- gpt
    - transformer decoder
    - talktotransformer.com

- bert
    - using [cls] and [sep] for classification and seperating sentences
    - also you can use all sequence of vector to do classification
        - however, you need to fix the length of sequence or use the mean of all vector

- transformer encoder
    - when i train with specific len_segment
        - if i want to do the classification, i can use CLS or mean of all vector
            - in my experiences, using mean of all vector will give a better result than using CLS
        - usually, it give better prediction if len_segment is larger
            - hence, i can train with small len_segment, then test with regular len_segment
            - in my experiences, majority vote between different segment (which using training segment_len) will approach CLS
    - it is hard to train a deep transformer encoder
    - it is also hard to train a wide transformer encoder
    - pytorch transformer encoder does not include positional encoder

- conformer
    - a modified transformer which is for audio recognization
    - it give really good performace