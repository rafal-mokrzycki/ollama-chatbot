# llm-chatbot
Chatbot to get information from text files using LLMs

## Preparation

### For Windows

#### Prepare virtual environment

1. Create and activate virtual environment:

```
python -m venv .venv
.venv\Scripts\activate
```

2. Install required packages:

```
pip install -r requirements.txt
```
#### Install Ollama

1. Go to [https://ollama.com/download](https://ollama.com/download) and download Ollama for your OS.
2. Run the installation script.
3. For Windows make sure you added a system environmental variable `OLLAMA_MODELS`: `{folder}`.
4. Run `ollama pull mistral` in the command line inside virtual environment.
5. Run `ollama run llama3.2:1b` in order to install a language model.

### For Linux

#### Prepare virtual environment

1. Create and activate virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```
2. Install required packages:

```
pip3 install -r requirements.txt
```
#### Install Ollama

```
curl https://ollama.ai/install.sh | sh
ollama pull mistral
ollama run llama3.2:1b
```

## Usage

### GUI

#### For Windows

1. Activate virtual environment: `.venv\Scripts\activate`.
2. Run app: `python -m  ui.app`.
3. Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

#### For Linux

1. Activate virtual environment: `source venv/bin/activate`.
2. Run app: `python3 -m  ui.app`.
3. Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

### CLI

#### For Windows

1. Activate virtual environment: `.venv\Scripts\activate`.
2. Run app: `python models/ollama/main.py`

#### For Linux

1. Activate virtual environment: `source venv/bin/activate`.
2. Run app: `python3 models/ollama/main.py`

## Testing and Debugging

For testing purposes, run `pytest tests/test_logger.py`.
