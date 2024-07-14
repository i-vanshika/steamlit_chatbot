import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text, api_key):
  llm = OpenAI(temperature=0.7, openai_api_key=api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  
  if submitted:
    if not openai_api_key.startswith('sk-'):
      st.warning('Please enter a valid OpenAI API key!', icon='⚠')
    else:
      generate_response(text, openai_api_key)