from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true" # Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Carefully understand and respond to user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit
st.title("Creating a simple Chatbot using Langchain")
input_text = st.text_input("What is your query?")

# --------------------------------------------------------------------------------------------------
# OpenAI LLM (Uncomment only if you have OpenAI API)
#llm = ChatOpenAI(model="gpt-3.5-turbo")
#output_parser = StrOutputParser
#chain = prompt | llm | output_parser

#if input_text:
#    st.write(chain.invoke({'question': input_text}))
# --------------------------------------------------------------------------------------------------


