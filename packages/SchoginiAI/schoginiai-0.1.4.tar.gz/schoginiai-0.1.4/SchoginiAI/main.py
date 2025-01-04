"""
main.py - Core functionality for SchoginiAI with recursive chunking, embeddings, and RAG.
"""

from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document


class SchoginiAICore:
    """
    Original AI core template.
    """

    def __init__(self, model_name="default"):
        self.model_name = model_name

    def predict(self, input_data: str) -> str:
        return f"Prediction from {self.model_name} for: {input_data}"


class SchoginiAIRAG:
    """
    A retrieval-augmented generation (RAG) class using LangChain components.

    Steps:
      1. Split text into chunks (recursive).
      2. Embed chunks with OpenAI Embeddings.
      3. Store chunks in FAISS vector DB.
      4. Query with a RetrievalQA chain using gpt-3.5-turbo or similar.
    """

    def __init__(self, openai_api_key: str, model_name: str = "gpt-3.5-turbo"):
        self.api_key = openai_api_key
        self.model_name = model_name
        self._retriever = None

    def build_vector_store(self, text_data: str):
        """
        Splits text_data, embeds chunks, and builds a FAISS vector store.
        """
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        # Split text into Document chunks
        docs = [Document(page_content=chunk) for chunk in splitter.split_text(text_data)]

        # Embed with OpenAI
        embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)

        # Create a FAISS vector store
        vector_store = FAISS.from_documents(docs, embeddings)

        # Create a retriever for downstream queries
        self._retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    def ask_question(self, query: str) -> str:
        """
        Uses a RetrievalQA chain to answer questions with RAG.
        """
        if not self._retriever:
            raise ValueError("Vector store not built. Call build_vector_store() first.")

        llm = ChatOpenAI(
            model_name=self.model_name,
            openai_api_key=self.api_key
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self._retriever
        )

        result = qa_chain.run(query)
        return result

