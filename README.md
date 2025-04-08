# FolderGPT

**FolderGPT** is a lightweight CLI tool that leverages an LLM (like LLaMA 3 via Ollama) to interpret natural language commands for managing folders.

## 💡 Features

- ✅ Create folders using natural language
- 🗑️ Delete folders easily
- 📂 List existing directories
- ✏️ Rename folders by describing the action

## 🛠️ Tech Stack

- Python
- Ollama (LLaMA 3.1)
- Local LLM interaction via subprocess
- JSON parsing and custom folder utilities

## 🚀 Example

```bash
You: create a folder named reports
LLaMA: {
  "response": "Creating folder 'reports'",
  "data": {
    "process": "create",
    "folder_name": "reports"
  }
}
```

# Clone the repository

git clone https://github.com/devcusn/llm-llama-directory-agent.git
cd llm-llama-directory-agent

# Run the CLI

python init.py
