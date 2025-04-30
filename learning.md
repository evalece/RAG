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
  
