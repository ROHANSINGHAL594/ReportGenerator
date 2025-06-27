
import os 
import streamlit as st
from langchain_groq import ChatGroq
class GroqLLM:
    def __init__(self, user_control_inputs):
        self.user_control_inputs =user_control_inputs
    
    def get_llm_model(self):
        try:
            groq_api_key = self.user_control_inputs["GROQ_API_KEY"]
            model = self.user_control_inputs["selected_model"]
            if groq_api_key =='' and os.environ["GROQ_API_KEY"]=='':
                st.error("please input the api key")
            llm = ChatGroq(model=model,api_key=groq_api_key)
            
        except Exception as e :
            raise ValueError(f"Exception occured as {e}")
        return llm
