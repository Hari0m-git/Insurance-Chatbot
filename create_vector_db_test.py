import os
from langchain_community.document_loaders import PyPDFLoader  # Updated import
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma  # Updated import
import os

def create_or_update_vector_db(data_folder='data', db_folder='db1', batch_size=50):
    # BGE Embedding configuration
    model_name = "BAAI/bge-small-en-v1.5"
    encode_kwargs = {'normalize_embeddings': True}  # Set True to compute cosine similarity

    embedding_function = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cuda'},
        encode_kwargs=encode_kwargs,
    )

    # Load existing vector database or create a new one
    if os.path.exists(os.path.join(db_folder, 'index')):
        vectordb = Chroma(persist_directory=db_folder, embedding_function=embedding_function)
        print("Loaded existing vector database.")
    else:
        vectordb = None
        print("Creating a new vector database.")

    documents = []
    for pdf_file in os.listdir(data_folder):
        if pdf_file.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(data_folder, pdf_file))
            documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_documents = text_splitter.split_documents(documents)

    # If no vector database exists, create one
    if vectordb is None:
        vectordb = Chroma.from_documents(documents=split_documents[:batch_size], embedding_function=embedding_function, persist_directory=db_folder)
        print("Created a new vector database.")
    
    # If vector database exists, check for new documents and add them
    else:
        # Find new documents by comparing the number of existing vectors with new splits
        existing_vectors = vectordb._collection.count()
        new_splits = split_documents[existing_vectors:]

        if new_splits:
            print(f"Found {len(new_splits)} new document splits to add.")
            for i in range(0, len(new_splits), batch_size):
                batch = new_splits[i:i+batch_size]
                vectordb.add_documents(documents=batch)
    
    vectordb.persist()
    print("Vector database updated and persisted.")

if __name__ == "__main__":
    create_or_update_vector_db()
