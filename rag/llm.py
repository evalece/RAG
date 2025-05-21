# https://python.langchain.com/docs/integrations/chat/ <- $$
# <- https://medium.com/@akshat.g_77864/free-and-paid-large-language-models-with-langchain-5950033b8c7d <- free tiers

# Ensure your VertexAI credentials are configured 

from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

hf_pipeline = pipeline("text-generation", model="sshleifer/tiny-gpt2")
llm = HuggingFacePipeline(pipeline=hf_pipeline)
response = llm.invoke("Hello, world!")
print(response)


