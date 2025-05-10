# RAG Technical Logs, Learnings and Decisions

## April 28- Project Prep
Retrieval Augmented Language Models:
TF-IDF-sparse retrieval- score functiion and query function to score for query overlaps (i.e, words that do or do not occur among source queries)

- Retrival methods
Ref: https://www.youtube.com/watch?v=mE7IDf2SmJg
- Sparse retrival 
DrQA: uses sparse retrival to return non-repeating & vast word vectors trained using LSTM.
- Dense retrival
Dense retrival: sematic similarity focus with smaller dimension, using laten variable in training + supervised. I.e. BERT (synonyms in semantic-focused LLM training)

dot product-> GPU friendly

- Word models (query and document interaction and scoring)
goal: to compute similarities of words

- SOTA (State of the Art RAG): 
    - Splade: Sparse+ Dense
    - Dragon: Generalized densed + progressive data aug
    - Hybrid: sparse <-> dense




## April 29- Evolution of Transformer Model 
Standford CS224N lecture 7: https://www.youtube.com/watch?v=wzfWHP6SXxY

- Neural Translation Model to Attention (self attention & transformer models)
    - Starting from parallel text & stat model regression optimization: components are broken down into smaller chunks that sees higher probabilities of matching, the arrangement of words is considered "encoding" and "decoding"
    - In nueral MT, encodes each word using RNN, last encoding state become input of decoding state.
    - Use Beam Search instead of greedy in training.
    - RNN: still hard to optimize, each state depends on prior state(s), hence, attention comes in:
    - Attention in neural MT (RNN): decoder computes "similarity" score from each encoder state into attention score. 

## April 30- Self-Attention into Transformer

Standford CS224N lecture 8:
    - Encode position allowes replacement of RNN while allowing parallel computation in feed-forward deep neural network training.
    - In training, mask future words for prediction.


## May 02- A Complete Transformer
- CS224N NLP Lecture 8  https://www.youtube.com/watch?v=LWMzyfvuehA&t=4464s

    - Cross Attention on encoder side: remove masking, cross attention passes keys and values from encoder to decoder. Decoder produces query on these trainable values+ attention weighted values (these are results of entire context attention weighted sum + viewing from each words, and can be multi-headed with batch  + summing function to sum batches up, see linear algebra notes in the following).
    - Linear Algebra notes in K,Q,V (Key, Query, Values) in dimension d by d are efficient GPU utilization, but are essentially:
    - see 18:37 https://www.youtube.com/watch?v=LWMzyfvuehA&t=4464sCS224N%20NLP
    -  In Linear Algebra:
    - X= [x1....xn], n words, with word embedding of d dimensions, dimension of X= n by d
    - XK and XQ are n by d, K and Q are trainable tensors.
    - self attention of word i on word j for j in (1...n) is XQ(XK)^(T)= attention scores, this is a n by n vectore 
    - Softmax [(XQ(XK)^(T))] (XV) -> normalize values

## May 02- Continue on RAG 
- Frozen RAG: use vector databases, retrival ranks and word embeddings to retrieve relevant info. 
- Stanford CS25: V3 I Retrieval Augmented Language Models at https://www.youtube.com/watch?v=mE7IDf2SmJg&t=3076s 
- Research shows positive results with higher efficiency in Query encoding. Other options are document encoding (expansive), ranking of retrival) etc. 
- LLM models less likely aware of RAG implementation while generating. Exception inclduiing Retro (Borgeaud et al 2022).
Advance topics:
- Model decides when to do additional retrival to call RAG. (i.e, Flare approach, GPT: web search)
- Observation: frozen RAG: document retrival order impacts response correctness.
- Self-RAG (Asai et al 2023): self critize in retrived info.
- Advanced fronzen RAG tools
    1. Zero shot LLM to retrive relevant info (via dense retrival/ similar word embeddings)
    2. HyDE: embed query and pre-config solutions in search docs (Gao, Ma et al 2022)
    3. Hybrid search: sparse + dense with reciprocal rank
    4. Child-Parent: Search from small to large info
- Allow Embed related compuation in cache
- Look into Multinodal RAG 1:08:29  https://www.youtube.com/watch?v=mE7IDf2SmJg&t=3076s
- Advantage: can choose light LLM (my thought: embedding not have to be the same)
- Challenge: hard to evaluate quality 


## May 03- Summeraize on RAG 
- Stanford CS25: V3 I Retrieval Augmented Language Models at https://www.youtube.com/watch?v=mE7IDf2SmJg&t=3076s 
- Incentive: 
    1. LLM become unpredictive when needing to generate content with very few source document- Hallucianation problem (problematic outpuit with high model confidence), but model editing expansive 
    2. Customized source document (i.e., RAG avoids editing model by semi parametric: no memorization on LLM with contents; non-parameteric); other options: semi- and parametric (Yogatama et al 2021)
    3. semi parametric: versatile update of source doc by indexing from multiple retrivers
    4. Grounding: LLM answers question iff doc gives evidence of such; source pointer feature 
- RAG 
    1. LLM generator, but contextualized 
    2. Retriver: has query and document encoder
    3. Hence, RAG and LLM become two trainable parts

- Frozen RAG vs RAG:
    1. forzen does not have train 


## May 08- High Level On RAG + Agent 

I chat with chatGPT after reading https://aws.amazon.com/what-is/langchain/. 

  Summary: 
  - Agents, as of now, LLMs, are more likely to be specially trained to question among multiple sources, to summarize, extract, compare etc. -- They basically "retrieve" useful information from a bunch of relevant informations, assume successfully retrieved. 
  - RAGs, like a library full of updated information, is made available to agnets when an user input is recieved, and extra information is needed to generate better/ more accurate response. 

  - Together, Agents need to know how to best use of the library, and wheres to search from. The generation can sometimes be evaluated by human, making it like a "multi-layer" debug: for example, if LLM is fixed, we change our search method, how well will generation perform? 
  This still depends on fixed variable: the agent (LLM). 


## May 09- Kick Start on RAG

https://dl.acm.org/doi/pdf/10.1145/3626772.3657834 

- Flow: Query + Document chunk -> Encoding (Sparse or Dense; cross-attention) -> Attention Score to calculate top relevant Document -> Decoder (selected Doc on masking) [1]
- Simplied version for now by excluding parts not included in initial RAG:
    - Document chunk -> Encoding (Sparse or Dense; cross-attention) -> Attention Score to calculate top relevant Document
    - *** For later, a fully encoder-decoder RAG should propogate decoder loss back to encoder for weight trainings, but I will leave this feature for later. 
    

- Reference 
  [1] F. Cuconasu et al., “The Power of Noise: Redefining retrieval for RAG systems,” Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp. 719–729, Jul. 2024, doi: 10.1145/3626772.3657834.
