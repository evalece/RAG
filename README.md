# RAG 
![Last Commit](https://img.shields.io/github/last-commit/evalece/RAG)
- [x] In-Development 

### This project aims to implemnt retrieval of information as a trainable unit. In a transformer setting, input and queries/ or documents are processed in encoders where cross-attention helps identify the most relevant information. Decoders could be optimzed by training with cross-attention weights and weights on encoders as it generates output on masking. 

### In our case, the final goal is to back propogate generation loss throughtout the transformer model in a joint training [1].   

## Reference
[1] D. Bahdanau, K. Cho, and Y. Bengio, “Neural machine translation by jointly learning to align and translate,” arXiv.org, Sep. 01, 2014. https://arxiv.org/abs/1409.0473



<!-- ROADMAP -->
## Roadmap
- [x] Define Project Roadmap 
- [x] Tool exploration 
    - [ ] LLM model test 
    - [ ] Embedding 
    - [ ] Vector DB
    - [ ] Benchmark & Baseline testing
    - [ ] Test method 
- [ ] Simplified RAG test
- [ ] RAG + LLM benchmark as baseline 
    - [ ] Frozen RAG
    - [ ] Non-Frozen RAG + Encoder on input and document 
- [ ] Decoder into RAG to train encoders. 


# Prototype Plan

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



- Reference 
  [1] F. Cuconasu et al., “The Power of Noise: Redefining retrieval for RAG systems,” Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp. 719–729, Jul. 2024, doi: 10.1145/3626772.3657834 https://dl.acm.org/doi/pdf/10.1145/3626772.3657834 .

  [2] P. Zhao et al., “Retrieval-Augmented Generation for AI-Generated Content: a survey,” arXiv.org, Feb. 29, 2024. https://arxiv.org/abs/2402.19473
## Contributor

<a href="https://github.com/evalece/RAG/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=evalece/RAG" />
</a>