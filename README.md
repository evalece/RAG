# RAG 
![Last Commit](https://img.shields.io/github/last-commit/evalece/RAG)
- [x] In-Development 

# May 24 - Readings and Pivots on this project
- I read (actually, quickly scan through): ReAct, Facilitating Multu-Trun Function Calling For LLMs Via Compositional Institutution Tuning, LoRA, Understanding Zero-Shot and Few-Shot in LLMs
- Thought: This project can focus on making LLM agent microservice-like:
    - 1. Configurable in and outside of pipeline 
    - 2. Runnable, test-able in and outside of pipeline 
    - 3. Configuration allows for features mention in several papers (i.e., prompt, LLM, Transformer or other training modules, memory, few or zero-shot).
    - 4. Monitoring, re-configuration, re-arrangement and benchmarking easy
    - 5. (I haven't read this part) Considers GPU and other hardware optimization

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