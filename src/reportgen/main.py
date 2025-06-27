import streamlit as st
from src.reportgen.ui.streamlitui.loadui import Ui
from src.reportgen.llms.groqllm import GroqLLM
from src.reportgen.llms.openaillm import OpenaiLLM
from src.reportgen.graphs.graph_builder import GraphBuilder
from src.reportgen.ui.streamlitui.display import DisplayResultStreamlit

def load_langraph_agentic_app():


    UI =Ui()
    user_input = UI.load_streamlit_ui()
    if not user_input:
        st.error("FAILED TO  LOAD USER INPUT")

    user_message =st.chat_input("ENTER YOUR MESSAGE :")
    if user_message:
        try:
            if(user_input["selected_llm"]=="Groq"):
                object_llm_config=GroqLLM(user_input)
                model = object_llm_config.get_llm_model()
                if not model:
                    st.error("Model could not be fetched")
                    return
                graph_builder = GraphBuilder(model)

                try:
                    graph = graph_builder.report_generation_bot()
                    DisplayResultStreamlit(graph,user_message).display_result_on_ui()


                except Exception as e:
                    st.error("Graph setup failed -{e}")
                    return
            elif(user_input["selected_llm"]=="OpenAi"):
                object_llm_config=OpenaiLLM(user_input)
                model = object_llm_config.get_llm_model()
                if not model:
                    st.error("Model could not be fetched")
                    return
                graph_builder = GraphBuilder(model)

                try:
                    graph = graph_builder.report_generation_bot()
                    DisplayResultStreamlit(graph,user_message).display_result_on_ui()


                except Exception as e:
                    st.error("Graph setup failed -{e}")
                    return

        except Exception as e:
            st.error("user message not detected")
            return
            

