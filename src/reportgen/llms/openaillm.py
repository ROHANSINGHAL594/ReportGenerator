import os 
import streamlit as st
from langchain_openai import ChatOpenAI
class OpenaiLLM:
    def __init__(self, user_control_inputs):
        self.user_control_inputs =user_control_inputs
    
    def get_llm_model(self):
        try:
            openai_api_key = self.user_control_inputs["OPENAI_API_KEY"]
            model = self.user_control_inputs["selected_model"]
            if openai_api_key =='' and os.environ["OPENAI_API_KEY"]=='':
                st.error("please input the api key")
            llm = ChatOpenAI(model=model,api_key=openai_api_key)
            
        except Exception as e :
            raise ValueError(f"Exception occured as {e}")
        return llm
