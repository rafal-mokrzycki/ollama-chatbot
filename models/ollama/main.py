from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation_decorator(func):
    def wrapper(context=None, question=None):
        if context is None and question is None:
            # CLI mode
            context = ""
            print("Welcome to the AI ChatBot! Type 'exit' to quit.")
            while True:
                user_input = input("You: ")
                if user_input.lower() == "exit":
                    break
                result = func(context, user_input)
                print("Bot: ", result)
                context += f"\nUser: {user_input}\nAI: {result}"
        else:
            # Web mode
            return func(context, question)

    return wrapper


@handle_conversation_decorator
def handle_conversation(context, question):
    result = chain.invoke({"context": context, "question": question})
    return result  # Return the result instead of printing it


if __name__ == "__main__":
    handle_conversation()  # Run in CLI mode
