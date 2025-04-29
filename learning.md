April 28- Project Prep
Retrieval Augmented Language Models:
TF-IDF-sparse retrieval- score functiion and query function to score for query overlaps (i.e, words that do or do not occur among source queries)

### Retrival methods
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


#In context Ralm
