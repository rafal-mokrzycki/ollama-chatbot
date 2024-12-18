import asyncio
import os

from langchain_community.document_loaders import PyPDFLoader


async def load_pdf():
    for file_name in os.listdir("data"):
        if file_name.endswith(".pdf"):
            filepath = os.path.abspath(os.path.join("data", file_name))
            loader = PyPDFLoader(filepath)
            pages = []
            async for page in loader.alazy_load():
                pages.append(page)
            print(f"{pages[0].metadata}\n")
            print(pages[0].page_content)


if __name__ == "__main__":
    # Run the async function
    asyncio.run(load_pdf())
