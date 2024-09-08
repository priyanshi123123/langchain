from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama 


import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. please response to the queries"),
        ("user","Question:{question}")
    ]
)

# streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text= st.text_input("Search the topic you want")


# openAI LLAma2

llm = Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
    