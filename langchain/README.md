
# Step 1: Create new venv (need python3.10 or above)
python3.10 -m venv newenv 
# Step 2: Activate
source newenv/bin/activate 
# Step 3: Reinstall packages
pip install -r requirements.txt

## RAG

- Provides LLMs to be used in RAG, delivered by LangChian via customized evaluation method.
- Lanchain may be abbreviated as LC hereafter.


## Planned Implementation and workflow 

Retrieval can be done by allowing various types of vector DB to search on input documents. But embedding documents on the fly is expansive. 

Hence, possible approaches are 

1. Selectively embed 

2. Recursive embed

## In-Development Notes:

- 1. See LLM models available at: https://python.langchain.com/docs/integrations/chat/ 
- 2. LangChian uses Pydanti, a tool to enforce type checking in classes in Python — : is required, = is optional with default
- 3. Common practice — Dictionary unpacking: 
    ```bash 

        user = User(**external_data)
        # is 
        user = User(name="Eva", age=0)
    ```
- 4. Tool calling alters user input and model output for UI/UX & refined search: https://python.langchain.com/docs/how_to/tool_results_pass_to_model/
    i.e., query = "What is 3 * 12? Also, what is 11 + 49?" tool calling: 'name': 'multiply', 'args': {'a': 3, 'b': 12}

    - Important: Use langchain-core == 0.2.19 and above to get LangChain Core for Tool calling message
- 5. Use cases of tool calling 
    - Evaluation of Upstream model that impacts downstream ones. (They can be injected with other values by Annotated) — but we can make an observation pipeline for the time being or see what LangGraph has to offer, otherwise, sampling Tool calling metrics within multinodal chain to present them in a graph databases by MVP submodule 


## GPT solution for WARNING: langchain 0.2.17 does not provide the extra 'google-vertexai'

```bash
pip install "pydantic<2.0"
pip install langchain langchain-community

```


## Other Tools to try

1. Poetry- environ setup, swapping env easy
2. Try chromaDB, FAISS and other vectorDB (On searching algorithm [4,5], mentioned on [6]) to serve retrieval. (ps, chroma free [1] but may be unstable, check [2] fpr compatibiliy with LangChain). 
3. Split document semantically is recommended [3]


## Langchain implementation tutorial (Python)

[7] LC kick start code + book/ reference source (from author's git repo)
[8] Tokenizer matters! 
side: GPT: embeddings usually not free to access, but some do
[9] The huggingface embeddings, with the following restriction:
[10] Embedding model: sentence-transformers/all-MiniLM-L6-v2
`A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.2.6 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.
`


## Thoughts
May 31
Probably look into how to work with The Huggingface on training an embedding model for specific search. This may involve JAX and other hardard optimization, which may sound interesting but will eventually enlarge the project scope. 

I saw the following skills being asked a lot, and are observed from several recent LLM and vector DB paper, I should also try 

Remote servers for training or fine tuning transformers (i.e. like ReAct) 

1. Colab (side: storage may be limited, if don't care on speed during pre-training, for example, few shots on small sets, then need checkpoints)
2. GCP (has TPUs but free tier for 1 month only)
^ (remember to always add sufficient shuffling to avoid covariant, dependent and etc related overfitting issues)

1. JAX: XLA 
2. Google T5 (TPU)
3. SmoothQuant
4. FlexGen (GPU offloading)

[1] https://www.trychroma.com/ 
[2] https://python.langchain.com/docs/integrations/vectorstores/ 
[3] https://research.trychroma.com/evaluating-chunking?utm_source=chatgpt.com 
[4] https://arxiv.org/abs/2111.08566 
[5] https://dl.acm.org/doi/10.1145/3600006.3613166 
[6] https://www.youtube.com/watch?v=1QdwYWd3S1g 
[7] https://www.youtube.com/watch?v=yF9kGESAi3M&t=10379s 
[8] https://huggingface.co/docs/transformers/main_classes/tokenizer
[9] https://api.python.langchain.com/en/latest/embeddings/langchain_community.embeddings.huggingface.HuggingFaceEmbeddings.html
[10] https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 
