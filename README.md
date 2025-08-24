# 🚀 LangGraph Email Agent

> **AI-Powered Email Automation System Built with LangGraph and RAG Technology**

A sophisticated email automation system that leverages AI agents to intelligently categorize, process, and respond to customer emails. Built with LangGraph for workflow orchestration and RAG (Retrieval-Augmented Generation) for accurate, context-aware responses.

## ✨ Features

### 🤖 **Intelligent Email Processing**
- **Real-time Gmail monitoring** with automatic email categorization
- **AI-powered classification** into customer complaint, product inquiry, feedback, or unrelated
- **Smart filtering** to maintain efficiency and focus on relevant communications

### 🧠 **Advanced AI Response Generation**
- **Multi-agent workflow** using LangGraph for coordinated email handling
- **RAG-powered responses** for accurate product/service information
- **Personalized content generation** tailored to each customer's needs
- **Quality assurance** with AI-powered formatting and relevance checks

### 🔄 **Automated Workflow**
- **Seamless email processing** from inbox to response
- **Multi-stage validation** ensuring high-quality outputs
- **Scalable architecture** ready for production deployment

## 🏗️ Architecture

The system uses a sophisticated LangGraph workflow with specialized AI agents:

1. **Email Monitor Agent** - Continuously checks Gmail inbox
2. **Categorization Agent** - Classifies emails by type and priority
3. **Response Generator Agent** - Creates personalized email drafts
4. **Quality Assurance Agent** - Validates and formats responses
5. **RAG Integration** - Retrieves accurate information from knowledge base

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Gmail API credentials
- Groq API key (for LLM access)
- Google Gemini API key (for embeddings)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/just-surviving/langgraph-email-agent.git
   cd langgraph-email-agent
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Configure Gmail API:**
   - Follow [Google's Gmail API setup guide](https://developers.google.com/gmail/api/quickstart/python)
   - Place your credentials file in the project root

### Running the Application

**Local Development:**
```bash
python main.py
```

**API Deployment:**
```bash
python deploy_api.py
```
Access the API at `http://localhost:8000` with docs at `/docs`

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
MY_EMAIL=your_email@gmail.com
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

### Knowledge Base Setup

To customize the system for your business:

1. Add your company documents to the `data/` folder
2. Run the indexing script:
   ```bash
   python create_index.py
   ```

## 🐳 Docker Deployment

### Build and Run Locally
```bash
docker build -t langgraph-email-agent .
docker run -p 8000:8000 --env-file .env langgraph-email-agent
```

### Deploy to Cloud Platforms

#### Render Deployment
1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn deploy_api:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`
5. Add environment variables in Render dashboard

#### Railway Deployment
1. Connect your GitHub repository to Railway
2. Railway will auto-detect Python and install dependencies
3. Set start command: `gunicorn deploy_api:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`
4. Add environment variables in Railway dashboard

## 🔧 Customization

### Modifying Agent Behavior
- Edit agent logic in `src/nodes.py`
- Customize prompts in `src/prompts.py`
- Adjust workflow in `src/graph.py`

### Adding New Features
- Extend the state schema in `src/state.py`
- Add new tools in `src/tools/`
- Integrate additional AI services

## 📁 Project Structure

```
langgraph-email-agent/
├── src/
│   ├── agents.py          # AI agent definitions
│   ├── graph.py           # LangGraph workflow
│   ├── nodes.py           # Workflow nodes
│   ├── prompts.py         # AI prompts
│   ├── state.py           # State management
│   ├── structure_outputs.py # Output formatting
│   └── tools/
│       └── GmailTools.py  # Gmail integration
├── data/                  # Knowledge base documents
├── db/                    # Vector database
├── main.py               # Local execution
├── deploy_api.py         # API deployment
├── create_index.py       # Knowledge base indexing
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
└── .env.example         # Environment template
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and modern AI technologies.

---

**Built with ❤️ by Abhinav

<!-- Last updated: 2025-08-15 -->

<!-- Last updated: 2025-08-15 -->
