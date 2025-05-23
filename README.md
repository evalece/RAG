# RAG 
![Last Commit](https://img.shields.io/github/last-commit/evalece/RAG)
- [x] In-Development 

This project aims to implement retrieval of information as a trainable unit while enabling modularized decoder, tracking, and learning modules for latency optimization. 
 
This is a speculative RAG [2] with additional metrics to measure model confidence. It aims to leverage cache and document retrival with low latency when decoder training is disabled. 

While similar to Logit-based RAG in evaluating confidence [2], the training set does not contain any generator output.

In our case, the final goal is to back propagate generation loss throughout the transformer model in a joint training [1].   


# May 21 and 22 - Reading of LangChain Doc (zzz to wow)
- I discussed with ChatGPT 4o and it came up with the right word "LLM wrapper" — similar tools are LlamaIndex, Haystack, Semantic Kernel, CrewAI, Flowise etc. I choose LangChiain for job searching purpose
- LangChain LLMs need $ to run, for this development, we will try choosing from The Hugging Face LLMs that supports LangChain APIs

<!-- ROADMAP -->
## Roadmap
- [x] Define Project Roadmap 
- [x] Tool exploration 
    - [x] LLM model test 
    - [ ] Embedding 
    - [ ] Vector DB
    - [ ] Benchmark & Baseline testing
    - [ ] Test method 
- [ ] Simplified RAG test
- [ ] RAG + LLM benchmark as baseline 
    - [ ] Frozen RAG
    - [ ] Non-Frozen RAG + Encoder on input and document 
- [ ] Decoder into RAG to train encoders. 


## Prototype Plan

- A possible prototype: 
    - Speculative RAG 
        - Decoupled decoder in non-training usage for low latency. 
        - Implement Semantic Cache, reference GPTCache [1] 
        - Similar Approach: REALM by Google [1]
    - Observation of RAG during training and testing 
        - Learning off means model do not learn from the operation for retrieval 
        -  (Learning off on generation+document sets*) Logit RAG in pipeline to produce model confidence on each retrieval and response. 
        - Store learning + toggle feature to run the model with and without learning on 
            - retrieval 
            - decoder backprop (for later) 
        - Stat tracking (i.e., recall, precision, confidence etc )
    
*In Logit-Based RAG, generator and retrieval output gets map to a softmax tensor, representing probabilities. In our case, we do not wish to combine generator output to train RAG. -- check if confidence LLM exists, if not, calculating it.


## Reference
  [1] D. Bahdanau, K. Cho, and Y. Bengio, “Neural machine translation by jointly learning to align and translate,” arXiv.org, Sep. 01, 2014. https://arxiv.org/abs/1409.0473

  [2] P. Zhao et al., “Retrieval-Augmented Generation for AI-Generated Content: a survey,” arXiv.org, Feb. 29, 2024. https://arxiv.org/abs/2402.19473
## Contributor

<a href="https://github.com/evalece/RAG/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=evalece/RAG" />
</a>