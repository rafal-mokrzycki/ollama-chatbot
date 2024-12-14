from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

app = FastAPI()

# Initialize the model and prompt template
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Store conversation history in memory (for simplicity)
context = ""

# Serve static files (CSS) from the static directory
app.mount("/static", StaticFiles(directory="ui/static"), name="static")

# Set up Jinja2 templates for rendering HTML files
templates = Jinja2Templates(directory="ui/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/ask")
async def ask_bot(question: str):
    global context
    result = chain.invoke({"context": context, "question": question})
    context += f"\nUser: {question}\nAI: {result}"
    return {"answer": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
