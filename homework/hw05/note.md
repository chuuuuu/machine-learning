# seq2seq
## BLEU
- 1-gram (also called unigram)
  - e.g.
    - reference
      - 'the cat is on the mat'
      - ['the', 'cat', 'is', 'on', 'the', 'mat']
    - candidate
      - 'the cat the cat on the mat'
      - ['the', 'cat', 'the', 'cat', 'on', 'the', 'mat']
    - modified precision (denoted by p_1)
      - count_cand (based on candidate)
        - ['the': 3, 'cat': 2, 'on': 1, 'mat': 1]
      - count_ref (based on reference)
        - ['the': 2, 'cat': 1, 'on': 1, 'mat': 1]
      - p_1 = (2+1+1+1) / (3+2+1+1) = 5/7
- 2-gram (also called bigram)
  - e.g.
    - reference
      - 'the cat is on the mat'
      - ['the cat', 'cat is', 'is on', 'on the', 'the mat']
    - candidate
      - 'the cat the cat on the mat'
      - ['the cat', 'cat the', 'the cat', 'cat on', 'on the', 'the mat']
    - modified precision (denoted by p_2)
      - count_cand (based on candidate)
        - ['the cat': 2, 'cat the': 1, 'cat on': 1, 'on the': 1, 'the mat': 1]
      - count_ref (based on reference)
        - ['the cat': 1, 'cat the': 0, 'cat on': 0, 'on the': 1, 'the mat': 1]
      - p_2 = (1+0+0+1+1) / (2+1+1+1+1) = 3/6
- it could be generalized to n-gram
- brevity penalty (denoted by BP)
  - if c > r (where c is the length of candidate, r is the length of reference)
    - BP = 1
  - else
    - BP = exp(1-r/c)
  - if r is much small than c, BP would be very small
- formula of BLEU
  - BLEU = BP * (p_1^(w_1) * p_2^(w_2) * ... * p_N^(w_N))
    - w_1, w_2, ... are weight
      - sum(w_i) = 1
    - usually we use
      - N = 4
      - w_i = 1/4
- sacrebleu
  - the output will be muliplied by 100.
    - range: [0, 100]
- evaluating bleu score
  - even human translators do not achieve a perfect score of 1.0.
  - < 10
    - Almost useless
  - 10 - 19
    - Hard to get the gist
  - 20 - 29
    - The gist is clear, but has significant grammatical errors
  - 30 - 40
    - Understandable to good translations
  - 40 - 50
    - High quality translations
  - 50 - 60
    - Very high quality, adequate, and fluent translations
  - > 60
    - Quality often better than human
  - https://cloud.google.com/translate/automl/docs/evaluate
- different language have different best BLEU score
## subword units
- Out of vocabulary
  - Out of vocabulary (OOV) has been a major problem in machine translation
  - This can be alleviated by using subword units.
- sentencepiece package
  - which is an open source developed by google
  - do text tokenizer & detokenizer
  - implement algorithm
    - byte pair encoding
    - unigram language model
## byte pair encoding
- assume ['fish', 'fishing', 'fishes'] are in the corpus
- now, it comes a new word, 'fished'
- we can use lemmatization or stemming
- 'watermelon'
  - formed with 'water' and 'melon'
  - if you can split 'watermelon' into 'water' and 'melon'
    - then you can handle 'watermelon' even if it doesn't exist in the corpus
      - However, 'water' and 'melon' should be in the corpus
- thought of the algorithm (from wiki)
  - 'aaabdaaabac'
    - 'aa' occurs most often, set 'Z' = 'aa'
  - 'ZabdZabac'
    - 'ab' occurs most often, set 'Y' = 'ab'
  - 'ZYdZYac'
    - 'ZY' occurs most often, set 'X' = 'ZY'
  - 'XdXac'
  - in pratical, we consider the frequecy of word
  - https://www.youtube.com/watch?v=zjaRNfvNMTs
  - how many token do you want is a hyperparameter
    - usually it will be 8k, 16k, 24k, 32k
    - bert use about 20k for chinese, 30k for english 
## fairseq
- Fairseq is a sequence modeling toolkit written in PyTorch that allows researchers and developers to train custom models for translation, summarization, language modeling and other text generation tasks.
- encoding the word into numerical vector
  - e.g.
    - sample
      - 'id': 1
      - 'source': tensor([  54,   31,   26,  105, 2312,  224,   70,  127,    7,   21,  873,   82,   7,   2])
      - 'target': tensor([ 304,  458,  388, 3582,    4,   52,  143, 2503,  303,    2])
    - 'Source: but this is our front porch . we live there .'
    - 'Target: 這是我們的前庭 , 我們就住在那'
- teacher forcing
## data augmentation
- https://www.zhihu.com/question/305256736/answer/550873100
- noise
  - dropout
  - mask
- back translation (bt)
  - using back translation to get a new source data(get from f_b(target), f_b is bt model)
  - encoder is easily to train, but decoder is hard to train
    - hence, it's good enough to use synthetic data as source
    - however, it doesn't help anything to decoder if you use synthetic data as target
  - train a back translation model
    - generate new source data from target(can be labeled or unlabeled(also called monolingual data))
    - use new source data to train original model
  - you cannot use too much synthetic data
    - synthetic : real parallel corpora should not exceed 8:1 ratio
    - monolingual:  782527
    - read:         394066
  - Fadaee and Monz (2018) observe that
    - with an authentic-to-synthetic data ratio of 1:3, the benefit is only slightly larger than with a ratio of 1:1.
    - With a ratio of 1:10, synthetic data are clearly harmful.
## observation
- model tend to print a word repeatly
  - i guess it's caused by classification
    - machine will get reward only if it predict the word on the exactly position of reference
- rnn model also use the attention
  - what's difference between rnn with attetion and transformer
  - it seems that rnn only use attention between encoder and decoder(to make decoder understand where to notice)
- since parallelism, transformer is faster than rnn (in one epoch)
- is it possible to use the concept of GAN to train a machine translation?
  - since we dont have a good evaluation for measure how good the translation is
  - why dont we apply the work to machine, just like the discriminator in GAN
- when a model is getting complicated, it'll be more hard to be trained
  - simple model can be trained faster
- average last n model
  - it's kind of ensemble
## teacher forcing
- schedule sampling
## beam search
## model average
averaging models does not work better than the best_model
## data cleaning
- remove sentence-pair with a source/target length ratio exceeding 1.5
- remove sentence longer than 250
## what to do next
1. train a bt model (in bt.py) / train a ft model (in ft.py)
2. append monlingual data to trainset (in bt.py)
  - may related to fairseq.task.load_dataset
  - i think it will be easy to follow TA's hint
3. train a ft model with new dataset and see if BLEU increase
4. how to do schedule sampling with fairseq?
## resource
- bert architeture
  - https://medium.com/analytics-vidhya/understanding-bert-architecture-3f35a264b187
- sampling
  - https://zhuanlan.zhihu.com/p/131322356
- understand backtranslation at scale
  - https://www.aclweb.org/anthology/D18-1045.pdf
- some tips
  - https://zhuanlan.zhihu.com/p/113247337