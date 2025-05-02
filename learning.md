# April 28- Project Prep
Retrieval Augmented Language Models:
TF-IDF-sparse retrieval- score functiion and query function to score for query overlaps (i.e, words that do or do not occur among source queries)

## Retrival methods
Ref: https://www.youtube.com/watch?v=mE7IDf2SmJg
##  sparse retrival 
DrQA: uses sparse retrival to return non-repeating & vast word vectors trained using LSTM.
## Dense retrival
Dense retrival: sematic similarity focus with smaller dimension, using laten variable in training + supervised. I.e. BERT (synonyms in semantic-focused LLM training)

dot product-> GPU friendly

## Word models (query and document interaction and scoring)
goal: to compute similarities of words

#SOTA
-Splade: Sparse+ Dense
-Dragon: Generalized densed + progressive data aug
- hybrid: sparse <-> dense


# In context Ralm


# April 29- evolution of Transformer Model 
Standford CS224N lecture 7: https://www.youtube.com/watch?v=wzfWHP6SXxY

## Neural Translation Model to Attention (self attention & transformer models)
- Starting from parallel text & stat model regression optimization: components are broken down into smaller chunks that sees higher probabilities of matching, the arrangement of words is considered "encoding" and "decoding"
- In nueral MT, encodes each word using RNN, last encoding state become input of decoding state.
- Use Beam Search instead of greedy in training.
- RNN: still hard to optimize, each state depends on prior state(s), hence, attention comes in:
- Attention in neural MT (RNN): decoder computes "similarity" score from each encoder state into attention score. 

# April 30- Self-Attention into Transformer

Standford CS224N lecture 8:
- Encode position allowes replacement of RNN while allowing parallel computation in feed-forward deep neural network training.
- In training, mask future words for prediction.


# May 02- A Complete Transformer
- CS224N NLP Lecture 8 
https://www.youtube.com/watch?v=LWMzyfvuehA&t=4464s
- Cross Attention on encoder side: remove masking, cross attention passes keys and values from encoder to decoder. Decoder produces query on these trainable values+ attention weighted values (these are results of entire context attention weighted sum + viewing from each words, and can be multi-headed with batch  + summing function to sum batches up, see linear algebra notes in the following).
- Linear Algebra notes in K,Q,V (Key, Query, Values) in dimension d by d are efficient GPU utilization, but are essentially:
- see 18:37 https://www.youtube.com/watch?v=LWMzyfvuehA&t=4464sCS224N%20NLP
-  In Linear Algebra:
- X= [x1....xn], n words, with word embedding of d dimensions, dimension of X= n by d
- XK and XQ are n by d, K and Q are trainable tensors.
- self attention of word i on word j for j in (1...n) is XQ(XK)^(T)= attention scores, this is a n by n vectore 
- Softmax [(XQ(XK)^(T))] (XV) -> normalize values

