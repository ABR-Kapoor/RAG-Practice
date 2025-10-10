import os
import time
from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm
from pinecone import Pinecone, ServerlessSpec
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = "us-east-1"
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# Only set OPENAI_API_KEY if OPENROUTER_API_KEY is not None
if OPENROUTER_API_KEY:
    os.environ["OPENAI_API_KEY"] = OPENROUTER_API_KEY

UPLOAD_DIR = "./uploads_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
spec = ServerlessSpec(cloud="aws", region=PINECONE_ENV)
existing_indexes = [index.name for index in pc.list_indexes()]

if PINECONE_INDEX_NAME not in existing_indexes:
    print(f"Creating new index: {PINECONE_INDEX_NAME}")
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=768,
        metric="dotproduct",
        spec=spec
    )
    while not pc.describe_index(PINECONE_INDEX_NAME).status["ready"]:
        print("Waiting for index to be ready...")
        time.sleep(5)
else:
    print(f"Index {PINECONE_INDEX_NAME} already exists")

index = pc.Index(PINECONE_INDEX_NAME)

# load, split, and embed the documents

def load_vectorstore(uploaded_files):
    try:
        embedded_model = SentenceTransformerEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    except Exception as e:
        print(f"Embedding model failed: {e}")
        raise Exception("Please install sentence-transformers: pip install sentence-transformers")
    file_path =[]
    
    # 1. upload
    for file in uploaded_files:
        save_path = Path(UPLOAD_DIR) / file.filename 
        with open(save_path, "wb") as f:
            f.write(file.file.read())
        file_path.append(str(save_path))
        
    # 2. split
    for file_path in file_path:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
        )
        chunks = splitter.split_documents(documents) 
        
        texts = [chunk.page_content for chunk in chunks]
        # Add the actual text content to metadata so it can be retrieved
        metadata = []
        for chunk in chunks:
            chunk_metadata = chunk.metadata.copy()
            chunk_metadata["text"] = chunk.page_content  # Add the actual text content
            metadata.append(chunk_metadata)
        ids = [f"{Path(file_path).stem}_{i}" for i in range(len(chunks))]
        
    # 3. embed
    print("Embedding chunks...")
    embedding = embedded_model.embed_documents(texts)
    
    # 4. upsert to pinecone
    print("Upserting embedding...")
    with tqdm (total=len(embedding), desc = "Upserting embeddings to Pinecone") as progress:
        index.upsert(vectors = zip(ids, embedding, metadata))
        progress.update(len(embedding))
        
    print("Upload successfully! for file: ", file_path)