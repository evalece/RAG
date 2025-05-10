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
- [ ] Tool exploration 
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




## May 09- Kick Start on RAG


- Flow: Query + Document chunk -> Encoding (Sparse or Dense; cross-attention) -> Attention Score to calculate top relevant Document -> Decoder (selected Doc on masking) [1]
- Simplied version for now by excluding parts not included in initial RAG:
    - Document chunk -> Encoding (Sparse or Dense; cross-attention) -> Attention Score to calculate top relevant Document
    - *** For later, a fully encoder-decoder RAG should propogate decoder loss back to encoder for weight trainings, but I will leave this feature for later. 


- Reference 
  [1] F. Cuconasu et al., “The Power of Noise: Redefining retrieval for RAG systems,” Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp. 719–729, Jul. 2024, doi: 10.1145/3626772.3657834 https://dl.acm.org/doi/pdf/10.1145/3626772.3657834 .
## Contributor

<a href="https://github.com/evalece/RAG/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=evalece/RAG" />
</a>