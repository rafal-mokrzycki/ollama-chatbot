# llm-chatbot
Chatbot to get information from PDFs using LLMs

## Preparation

### Install Ollama

1. Go to [https://ollama.com/download](https://ollama.com/download) and download Ollama for your OS.
2. Run the installation script.
3. For Windows make sure you added a system environmental variable `OLLAMA_MODELS`: `{folder}`.
4. Run `ollama pull mistral` in the command line inside virtual environment.
5. Run `ollama run llama3.2:1b` in order to install a language model.

### Install required packages

Run `pip install -r requirements.txt`.

## Usage

### GUI

1. Activate virtual environment: `.venv\Scripts\activate`.
2. Run app: `python -m  ui.app`.
3. Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

### CLI

1. Activate virtual environment: `.venv\Scripts\activate`.
2. Run app: `python models/ollama/main.py`

## Testing and Debugging

For testing purposes, run `pytest tests/test_logger.py`.
