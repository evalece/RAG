# RAG Technical Logs, Learnings and Decisions

### This project aims to implemnt retrieval of information as a trainable unit. In a transformer setting, input and queries/ or documents are processed in encoders where cross-attention helps identify the most relevant information. Decoders could be optimzed by training with cross-attention weights and weights on encoders as it generates output on masking. 

### In our case, the final goal is to back propogate generation loss throughtout the transformer model in a joint training [1].   

## Reference
[1] D. Bahdanau, K. Cho, and Y. Bengio, “Neural machine translation by jointly learning to align and translate,” arXiv.org, Sep. 01, 2014. https://arxiv.org/abs/1409.0473

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



- Flow: Query + Document chunk -> Encoding (Sparse or Dense; cross-attention) -> Attention Score to calculate top relevant Document -> Decoder (selected Doc on masking) [1]
- Simplied version for now by excluding parts not included in initial RAG:
    - Document chunk -> Encoding (Sparse or Dense; cross-attention) -> Attention Score to calculate top relevant Document
    - *** For later, a fully encoder-decoder RAG should propogate decoder loss back to encoder for weight trainings, but I will leave this feature for later. 


- Reference 
  [1] F. Cuconasu et al., “The Power of Noise: Redefining retrieval for RAG systems,” Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp. 719–729, Jul. 2024, doi: 10.1145/3626772.3657834 https://dl.acm.org/doi/pdf/10.1145/3626772.3657834 .


  # May 12: Setting RAG Benchmark tool (Debug of RAG)
Tools (thought: this is semi-useful, well distributed datasets, GPT generated Q/As, similar to my co-op, but scoring is in question)
 - The Huggging Face
 - Hotpotqa (Featuring multi-hob questions that would require multiple domain search)

Description: AI-generated questions from various sources, see appendix 7.2: https://arxiv.org/pdf/2407.11005
https://arxiv.org/pdf/2407.11005 
https://huggingface.co/datasets/rungalileo/ragbench  (cc-by-4.0)


Another one: 
Evaluation + prototype RAG (dot product)
https://docs.ragas.io/en/stable/getstarted/rag_eval/#evaluate 
https://docs.ragas.io/en/stable/ 

- I think implementation would significantly change the toolsets, so into implementation prototype tomorrow

# May 13 RAG implementation
- Start everything from here: https://arxiv.org/pdf/2402.19473 
- Check long-context retrieval: https://arxiv.org/pdf/2406.15319 
- Quantized influencer & AI judge in distillation & rethinking: https://arxiv.org/pdf/2402.17081 

- A possible prototype: 
    - Speculative RAG 
        - Decoupled decoder in non-training usage for low latency. 
        - Implement Semantic Cache, reference GPTCache [1] 
        - Similar Approach: REALM by Google [1]
    - Observation of RAG during training and testing 
        - Learning off means model do not learn from the operation for retrival 
        -  (Learning off on generation+document sets*) Logit RAG in pipeline to produce model confidence on each retrival and response. 
        - Store learning + toggle feature to run the model with and without learning on 
            - retrival 
            - decoder backprop (for later) 
        - Stat tracking (i.e., recall, precision, confidence etc )
    
*In Logit-Based RAG, generator and retriver output gets map to a softmax tensor, representing probabilities. In our case, we do not wish to combine generator output to train RAG. -- check if confidence LLM exists, if not, calculating it.

- Reference 
    - [1] P. Zhao et al., “Retrieval-Augmented Generation for AI-Generated Content: a survey,” arXiv.org, Feb. 29, 2024. https://arxiv.org/abs/2402.19473


# May 19 Modularization on each search method and prototype evaluation goals

- Summary
    - Setting easier evaluation goals for RAG prototype 
    - Re-design RAG with less required training to be replaced by a modularized Knowledge Graph [1] or other graph databases

- Evaluation Method (Prototype)
    - Inspired by "Your RAGs powered by Google Search technology, part 1" [2] on query expansion, given solution document, we may
        - 1. Calculate embedding similarity on query expansion 
        - 2. Calculate information graph similarity on retrival and solution (perphase propose a weighting to measure score)
        - 2. Validate query expansion effectiveness without generating responses
        - 3. The goal here is to ensure retrieval of accuracy instead of both generating correct response and retrieval of correct document
        



- Reference 
 [1] https://cloud.google.com/blog/products/ai-machine-learning/rags-powered-by-google-search-technology-part-2
 [2] https://cloud.google.com/blog/products/ai-machine-learning/rags-powered-by-google-search-technology-part-1

 # May 20 LangChain Prototype on How RAG is doing

 - Let's start by making a monitoring pipeline: 
 - Evaluation of upstream model that impacts downstream ones. (They can be injected with other values by Annotated) — but we can make an observation pipeline for the time being or see what LangGraph has to offer, otherwise, sampling Tool calling metrics within multinodal chain to present them in a graph databases by MVP submodule 

 I continue to read through LangChain docs and pinned the following key ideas:
 - 1. Spawn runnables - Runnable has defualt functions, they can spawn. There are some Python restrictions where "near parallel" is the best it can do https://python.langchain.com/docs/concepts/runnables/#runnableconfig 
 - 2. Review asyncio ^ as a side note from point 1, for such workflow orchestration tools: Azure Data Factory, Luigi, Apache Airflow, Google Cloud Composer, Amazon CloudFormation, Dagster
 - 3. InjectionState for LangGraph for metrics tracking:
 (InjectionState: https://python.langchain.com/docs/concepts/tools/)
 https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/ 
- 4. Adding Agent: https://langchain-ai.github.io/langgraph/tutorials/get-started/1-build-basic-chatbot/ 


# May 21 and 22 - Reading of LangChain Doc (zzz to wow)
- I discussed with ChatGPT 4o and it came up with the right word "LLM wrapper" — similar tools are LlamaIndex, Haystack, Semantic Kernel, CrewAI, Flowise etc. I choose LangChiain for job searching purpose
- LangChain LLMs need $ to run, for this development, we will try choosing from The Hugging Face LLMs that supports LangChain APIs

# May 24 - Readings and Pivots on this project
- I read (actually, quickly scan through): ReAct, Facilitating Multu-Trun Function Calling For LLMs Via Compositional Institutution Tuning, LoRA, Understanding Zero-Shot and Few-Shot in LLMs
- Thought: This project can focus on making LLM agent microservice-like:
    - 1. Configurable in and outside of pipeline 
    - 2. Runnable, test-able in and outside of pipeline 
    - 3. Configuration allows for features mention in several papers (i.e., prompt, LLM, Transformer or other training modules, memory, few or zero-shot).
    - 4. Monitoring, re-configuration, re-arrangement and benchmarking easy
    - 5. (I haven't read this part) Considers GPU and other hardware optimization

- Otherwise, I am thinking about demoing using LoRA with a customized transformer + ReAct on a smaller subet of chosen topic using few-shot training, or each having their own independent pipeline 

    