# reference [9]

from langchain_huggingface.HuggingFaceEmbeddings import HuggingFaceEmbeddings

model_name = "hkunlp/instructor-large"
#model_kwargs = {'device': 'cpu'}
#encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    #model_kwargs=model_kwargs,
    #encode_kwargs=encode_kwargs
)