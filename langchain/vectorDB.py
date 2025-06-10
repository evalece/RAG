
# ref [7] + modified for the huggingface embedding model + chromaDB vector store 
# Purpose: testing of doc pre-embedding and presistant store on local via chroma
# Define Chroma DB and/ or other vector DB in one place
# Vector DB are optimized (sometimes in GPU level) retrival tools that uses word embeddings to retrieve top K relevant document, and/ or text. 

#Some DBs offer multinodal retrieval 

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os
# Reference: https://python.langchain.com/docs/integrations/vectorstores/chroma/ 




class VectorDB():
    def __init__(self):
        self.embedding_model= "sentence-transformers/all-MiniLM-L6-v2"

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "odyssey1.txt") #1 for debugging
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
    embeddings =  HuggingFaceEmbeddings( # change to  HuggingFaceEmbeddings free tier
        model=embedding_model
    )  # Update to a valid embedding model if needed
    print("\n--- Finished creating embeddings ---")

    # Create the vector store and persist it automatically
    print("\n--- Creating vector store ---")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Finished creating vector store ---")

else:
    print("Vector store already exists. No need to initialize.")