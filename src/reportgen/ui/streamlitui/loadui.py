import streamlit as st
import os
from src.reportgen.ui.uiconfig import Config

class Ui:
    def __init__(self):
        self.config =Config()
        self.user_controls ={}
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_title(),layout="wide")
        st.header(self.config.get_title())
        with st.sidebar:
            llm_options = self.config.get_llms()
            self.user_controls["selected_llm"]=st.selectbox("SELECT LLM",llm_options)
            if(self.user_controls["selected_llm"]=='Groq'):
                model_options = self.config.get_groq_model()
                self.user_controls["selected_model"]=st.selectbox("SELECT MODEL",model_options)
                self.user_controls["GROQ_API_KEY"]=st.session_state["GROQ_API_KEY"]=st.text_input("API KEY",type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("PLEASE ENTER THE GROQ API KEY TO PROCEED")
            if(self.user_controls["selected_llm"]=='OpenAi'):
                model_options = self.config.get_openai_model()
                self.user_controls["selected_model"]=st.selectbox("SELECT MODEL",model_options)
                self.user_controls["OPENAI_API_KEY"]=st.session_state["OPENAI_API_KEY"]=st.text_input("API KEY",type="password")

                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning("PLEASE ENTER THE OPENAI API KEY TO PROCEED")

        return self.user_controls
