import repackage
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel  # Import BaseModel

repackage.up()
from models.ollama.main import handle_conversation  # Import the unified function

app = FastAPI()


# Define a Pydantic model for the request body
class QuestionRequest(BaseModel):
    question: str  # Expecting a field named 'question'


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
async def ask(request: QuestionRequest):  # Use the Pydantic model here
    global context
    answer = handle_conversation(context, request.question)  # Call the unified function
    context += f"\nUser: {request.question}\nAI: {answer}"
    return {"answer": answer}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
