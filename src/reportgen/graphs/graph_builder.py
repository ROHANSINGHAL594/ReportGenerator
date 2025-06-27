from src.reportgen.states.state import State,WorkerState
from langgraph.graph import StateGraph,END,START
from src.reportgen.nodes.nodes import Nodes
class GraphBuilder:
    def __init__(self,model):
        self.graph_builder = StateGraph(State)
        self.llm = model
        

    def report_generation_bot(self):

        self.nodes = Nodes(self.llm)

        self.graph_builder.add_node("orchestor",self.nodes.orchestor)
        self.graph_builder.add_node("llm_call",self.nodes.llm_call)
        self.graph_builder.add_node("synth",self.nodes.synth)
        
        self.graph_builder.add_edge(START,"orchestor")
        self.graph_builder.add_conditional_edges("orchestor",self.nodes.router,["llm_call"])
        self.graph_builder.add_edge("llm_call","synth")
        self.graph_builder.add_edge("synth",END)
        return self.graph_builder.compile()

    