# llm-chatbot
Chatbot to get information from PDFs using LLMs

## Preparation

### Install Ollama

1. Go to (https://ollama.com/download)[https://ollama.com/download] and download Ollama for your OS.
2. Run the installation script.
3. For Windows make sure you added a system environmental variable `OLLAMA_MODELS`: `{folder}`.
4. Run `ollama pull mistral` in the command line inside virtual environment.
5. Run `ollama run llama3.2:1b` in order to install a language model.

### Install required libraries

Run `pip install -r requirements.txt`.

## Usage
