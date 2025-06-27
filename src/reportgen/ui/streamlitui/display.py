import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,graph,user_message):
        
        self.graph = graph
        self.user_message = user_message
    def display_result_on_ui(self):
        graph = self.graph
        user_message = self.user_message
        with st.spinner("generating report... ⏳"):
            try:
                with st.chat_message("user"):
                            st.write(user_message)
                result = graph.invoke({"topic": user_message})
                st.markdown(result["final_report"], unsafe_allow_html=True)
                
            except Exception as e:
                    st.error(f"An error occurred: {str(e)}")