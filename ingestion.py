import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader, PyMuPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from consts import INDEX_NAME

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

folder_name = "i-verve"


def ingest_docs():
    pdf_search = Path("i-verve").glob("*.pdf")
    pdf_files = [str(file.absolute()) for file in pdf_search]
    for pdf_file in pdf_files:
        print(f'Loading {pdf_file} pdf file...')
        loader = PyMuPDFLoader(pdf_file)

        raw_documents = loader.load()
        print(f"loaded {len(raw_documents)} documents")

        text_splitter = RecursiveCharacterTextSplitter()
        documents = text_splitter.split_documents(raw_documents)
        for doc in documents:
            source = doc.metadata["source"]
            doc_name = source.split('/')[-1]
            doc.metadata.update({"source": doc_name})

        print(f"Going to add {len(documents)} to Pinecone")
        PineconeVectorStore.from_documents(documents, embeddings, index_name=INDEX_NAME)
        print("****Loading to vectorstore done ***")


def ingest_docs2() -> None:
    from langchain_community.document_loaders.firecrawl import FireCrawlLoader

    langchain_documents_base_urls = [
        "https://python.langchain.com/docs/integrations/chat//",
        "https://python.langchain.com/docs/integrations/llms/",
        "https://python.langchain.com/docs/integrations/text_embedding/",
        "https://python.langchain.com/docs/integrations/document_loaders/",
        "https://python.langchain.com/docs/integrations/document_transformers/",
        "https://python.langchain.com/docs/integrations/vectorstores/",
        "https://python.langchain.com/docs/integrations/retrievers/",
        "https://python.langchain.com/docs/integrations/tools/",
        "https://python.langchain.com/docs/integrations/stores/",
        "https://python.langchain.com/docs/integrations/llm_caching/",
        "https://python.langchain.com/docs/integrations/graphs/",
        "https://python.langchain.com/docs/integrations/memory/",
        "https://python.langchain.com/docs/integrations/callbacks/",
        "https://python.langchain.com/docs/integrations/chat_loaders/",
        "https://python.langchain.com/docs/concepts/",
    ]

    langchain_documents_base_urls2 = [
        "https://i-verve.com/"
        # "https://protobots.ai/"
    ]
    for url in langchain_documents_base_urls2:
        print(f"FireCrawling {url=}")
        loader = FireCrawlLoader(
            url=url,
            mode="scrape",
        )
        docs = loader.load()

        print(f"Going to add {len(docs)} documents to Pinecone")
        PineconeVectorStore.from_documents(
            docs, embeddings, index_name="langchain-doc-index"
        )
        print(f"****Loading {url}* to vectorstore done ***")


if __name__ == "__main__":
    ingest_docs()
    # ingest_docs2()
