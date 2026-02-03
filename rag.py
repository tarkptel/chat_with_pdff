from langchain_groq import ChatGroq
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import pypdf
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()


os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

llm = ChatGroq(
    # api_key=API_KEY,
    model="llama-3.3-70b-versatile"
)



st.set_page_config(page_title="Chat with PDF (RAG)")
st.title("RAG")

pdf_file = st.file_uploader('Upload a PDF', type='pdf')
question = st.text_input("Ask a question about the PDF..")


if pdf_file:
    with st.spinner("reading and Processing PDF..."):
        with open("temp.pdf","wb") as f:
            f.write(pdf_file.read())


        loader = PyPDFLoader("temp.pdf")
        docs = loader.load()
        texts = [doc.page_content for doc in docs]


def main_chain(texts, question):

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100 )
        chunks = text_splitter.create_documents(texts)

        embedding_model = HuggingFaceEmbeddings(
                model_name="BAAI/bge-base-en-v1.5",
                model_kwargs={"device": "cpu"},
                encode_kwargs={"normalize_embeddings": True}
            )


        db = FAISS.from_documents(chunks, embedding_model)

        retriever = db.as_retriever(
                    search_type="similarity",
                    search_kwargs={"k":3}
                    )

        docs = retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in docs])


        prompt = f"""
                Answer ONLY using the context below.
                If the answer is not present, say "I don't know".

                Context:
                {context}

                Question:
                {question}

                """
      
        result = llm.invoke(prompt).content

        return result


if question:
     with st.spinner("Thinking..."):
          result = main_chain(texts, question)
          st.write(result)
        