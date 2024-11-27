import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
from langchain_core.output_parsers import StrOutputParser

os.environ["langchain_api"] = os.getenv("langchain_api")
os.environ["langchain_project"] = os.getenv("langchain_project")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain demo with Llama3.1")
input_text=st.text_input("How can I help you?")

llm = Ollama(model = "llama3.1")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))