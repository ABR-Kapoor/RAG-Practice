# 🤖 RAG Practice - AI-Powered Resume Analyzer

A sophisticated **Retrieval-Augmented Generation (RAG)** system built with FastAPI and Streamlit that enables intelligent analysis of candidate resumes using Large Language Models and vector databases.

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-0.2.11-yellow.svg)](https://langchain.com)
[![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-orange.svg)](https://pinecone.io)

## 🌟 Features

- **📄 PDF Resume Processing**: Upload and analyze multiple PDF resumes
- **🧠 AI-Powered Analysis**: Uses Claude 3.5 Sonnet via OpenRouter for intelligent responses
- **🔍 Vector Search**: Pinecone-powered semantic search across resume content
- **💬 Interactive Chat**: Streamlit-based chat interface for querying resume data
- **🚀 REST API**: FastAPI backend with comprehensive API documentation
- **☁️ Cloud Ready**: Vercel deployment configuration included
- **📊 Document Chunking**: Intelligent text splitting for optimal retrieval
- **🎯 Specialized Prompting**: Custom-designed prompts for resume analysis

## 🏗️ Architecture

```
RAG-Practice/
├── 🖥️ server/                 # FastAPI Backend
│   ├── 📁 modules/
│   │   ├── llm.py             # LLM chain configuration
│   │   ├── load_verctorstore.py # Vector database operations
│   │   ├── pdf_handler.py     # PDF processing utilities
│   │   └── query_handlers.py  # Query processing logic
│   ├── 📁 routers/
│   │   ├── upload_pdfs.py     # PDF upload endpoints
│   │   └── ask_question.py    # Question answering endpoints
│   ├── 📁 middlewares/
│   │   └── exception_handlers.py # Error handling
│   ├── 📁 uploads_docs/       # Uploaded PDF storage
│   ├── main.py               # FastAPI application entry point
│   ├── logger.py             # Logging configuration
│   └── requirements.txt      # Python dependencies
├── 🎨 client/                 # Streamlit Frontend
│   ├── 📁 components/
│   │   ├── chatUI.py         # Chat interface component
│   │   ├── upload.py         # File upload component
│   │   └── history_download.py # Chat history management
│   ├── 📁 utils/
│   │   └── api.py            # API communication utilities
│   ├── app.py               # Streamlit application
│   ├── config.py            # Configuration settings
│   └── requirements.txt     # Frontend dependencies
├── 🌐 api/
│   └── index.py             # Vercel deployment entry point
├── vercel.json              # Vercel configuration
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13+ 
- OpenRouter API Key (for Claude 3.5 Sonnet)
- Pinecone API Key
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/ABR-Kapoor/Candidate_Analysis_RAG_App.git
cd Candidate_Analysis_RAG_App
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install backend dependencies
pip install -r server/requirements.txt

# Install additional packages
pip install streamlit python-multipart pinecone-client==5.0.1
```

### 4. Environment Configuration

Create a `.env` file in the `server/` directory:

```env
# OpenRouter Configuration
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Pinecone Configuration
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=babybot-medical-index
```

### 5. Start the Application

#### Terminal 1: Start FastAPI Backend
```bash
cd server
uvicorn main:app --reload
```
🌐 **Backend**: http://127.0.0.1:8000
📚 **API Docs**: http://127.0.0.1:8000/docs

#### Terminal 2: Start Streamlit Frontend
```bash
cd client
streamlit run app.py
```
🎨 **Frontend**: http://localhost:8501

## 🔧 Configuration

### OpenRouter Setup
1. Visit [OpenRouter](https://openrouter.ai)
2. Create an account and generate an API key
3. Add the key to your `.env` file

### Pinecone Setup
1. Visit [Pinecone](https://pinecone.io)
2. Create a project and get your API key
3. Create an index with:
   - **Dimensions**: 768
   - **Metric**: dotproduct
   - **Cloud**: AWS
   - **Region**: us-east-1

## 📖 Usage

### Upload and Analyze Resumes

1. **Upload PDFs**: Use the Streamlit interface to upload one or multiple PDF resumes
2. **Processing**: The system automatically:
   - Extracts text from PDFs
   - Chunks content for optimal retrieval
   - Creates embeddings using Sentence Transformers
   - Stores vectors in Pinecone
3. **Query**: Ask questions about the resumes using natural language

### Example Queries

```
"What is the candidate's name and email?"
"List all the technical skills mentioned"
"How many years of experience does the candidate have?"
"What certifications does the candidate hold?"
"Summarize the candidate's work experience"
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/upload_pdfs/` | POST | Upload PDF files for processing |
| `/ask_question/` | POST | Query the processed documents |
| `/docs` | GET | Interactive API documentation |

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **LangChain**: Framework for developing LLM applications
- **Pinecone**: Vector database for similarity search
- **Sentence Transformers**: For creating embeddings
- **PyPDF**: PDF text extraction
- **Uvicorn**: ASGI server

### Frontend
- **Streamlit**: Interactive web application framework
- **Requests**: HTTP client for API communication

### AI/ML
- **Claude 3.5 Sonnet**: Via OpenRouter for text generation
- **all-mpnet-base-v2**: Sentence transformer model for embeddings

### Deployment
- **Vercel**: Serverless deployment platform
- **Docker**: Containerization (configuration available)

## 🚢 Deployment

### Vercel Deployment

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel --prod
   ```

3. **Environment Variables**: Set in Vercel dashboard:
   - `OPENROUTER_API_KEY`
   - `PINECONE_API_KEY`
   - `PINECONE_INDEX_NAME`

### Local Production

```bash
# Build and run with production settings
uvicorn server.main:app --host 0.0.0.0 --port 8000
```

## 🧪 Testing

### Manual Testing
1. Start both backend and frontend servers
2. Upload a test PDF resume
3. Ask sample questions to verify responses

### API Testing
Use the FastAPI docs at `/docs` for interactive testing.

## 🔍 Troubleshooting

### Common Issues

**ModuleNotFoundError**: 
```bash
pip install -r server/requirements.txt
pip install python-multipart pinecone-client==5.0.1
```

**Pinecone Connection Issues**:
- Verify API key and index name
- Check index dimensions (should be 768)
- Ensure proper region configuration

**OpenRouter API Issues**:
- Verify API key is valid
- Check rate limits and usage
- Ensure proper model name: `anthropic/claude-3.5-sonnet`

**Streamlit Import Errors**:
```bash
pip install streamlit pandas numpy
```

## 📚 Advanced Features

### Custom Prompting
The system uses specialized prompts designed for resume analysis with:
- Structured extraction guidelines
- Professional formatting
- Error handling for missing information

### Vector Search Optimization
- Chunk size: Optimized for resume sections
- Overlap: Configured to maintain context
- Embedding model: High-quality sentence transformers

### Scalability
- Async FastAPI endpoints
- Efficient vector storage
- Modular architecture for easy expansion

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenRouter** for LLM API access
- **Pinecone** for vector database services
- **LangChain** for RAG framework
- **Streamlit** for rapid UI development
- **FastAPI** for modern API framework

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/ABR-Kapoor/RAG-Practice/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ABR-Kapoor/RAG-Practice/discussions)

---

⭐ **Star this repository if you find it helpful!**

Built with ❤️ by [ABR-Kapoor](https://github.com/ABR-Kapoor)
