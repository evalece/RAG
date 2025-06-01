# https://python.langchain.com/docs/integrations/chat/ <- $$
# <- https://medium.com/@akshat.g_77864/free-and-paid-large-language-models-with-langchain-5950033b8c7d <- free tiers

# Ensure your VertexAI credentials are configured 

from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
#from langchain_community.vectorstores import Chroma
from vectorDB import chromaDB  # basic initialization 

from langchain_openai import OpenAIEmbeddings

hf_pipeline = pipeline("text-generation", model="sshleifer/tiny-gpt2")
llm = HuggingFacePipeline(pipeline=hf_pipeline)
response = llm.invoke("Hello, world!")
print(response)


# Reference: https://github.com/bhancockio/langchain-crash-course/blob/main/4_rag/1a_rag_basics.py
# # Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "odyssey.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Check if the Chroma vector store already exists
if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    # Read the text content from the file
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split the document into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Display information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")
    print(f"Sample chunk:\n{docs[0].page_content}\n")

    # Create embeddings
    print("\n--- Creating embeddings ---")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )  # Update to a valid embedding model if needed
    print("\n--- Finished creating embeddings ---")

    # Create the vector store and persist it automatically
    print("\n--- Creating vector store ---")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Finished creating vector store ---")

else:
    print("Vector store already exists. No need to initialize.")