from src.reportgen.states.state import State,WorkerState
from langgraph.graph import StateGraph,END,START
from langchain_core.messages import HumanMessage,SystemMessage
from langgraph.constants import Send
from src.reportgen.parsers.parser import list_sections
class Nodes:
    def __init__(self,model):
        self.llm =model
    
    def orchestor(self,state : State):
        result = self.llm.with_structured_output(list_sections).invoke([
        SystemMessage(content = " generate a plan for the report from the given topic."),
        HumanMessage(content=f" topic : {state['topic']}")
        ])
        return {"sections": result.sections}
    
    def llm_call(self,state : WorkerState):
    
        result = self.llm.invoke([
            SystemMessage(content = " generate the report section based on the name and description of the section given. include no preamble. use markdown format "),
            HumanMessage(content =f'here is the name : {state['section'].name} and the description : {state['section'].description}')
        ])
        return {'completed_sections' : [result.content]}
    
    def router(self,state : State):
        return [Send("llm_call",{"section" : s} ) for s in state['sections']]
    
    def synth(self,state :State):
        sections = state['completed_sections']
        final_report = "\n\n---\n\n".join(sections)
        return {"final_report" : final_report}

