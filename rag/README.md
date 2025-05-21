
## RAG

- Provides LLMs to be used in RAG, delivered by LangChian via customized evaluation method.



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


# GPT solution for WARNING: langchain 0.2.17 does not provide the extra 'google-vertexai'

```bash
pip install "pydantic<2.0"
pip install langchain langchain-community

```