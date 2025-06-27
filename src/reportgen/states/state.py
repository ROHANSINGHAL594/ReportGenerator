from typing import Annotated,List
from typing_extensions import TypedDict

import operator

from src.reportgen.parsers.parser import Section

class State(TypedDict):
    topic : str
    sections : List[Section]
    completed_sections : Annotated[list , operator.add]
    final_report : str

class WorkerState(TypedDict):
    section : Section
    completed_sections : Annotated[list , operator.add]