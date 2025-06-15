# 🌐 Hello World Graph

```py
from typing import Dict, TypedDict
from langgraph.graph import StateGraph 

class AgentState(TypedDict): # our state schema
    message: str

def greeting_node(state: AgentState) -> AgentState:
    """
    Simple node that adds a greeting message to the state
    """

    state['message'] = "Hey " + state['message'] + ", how is your day going?"

    return state 

graph = StateGraph(AgentState)

graph.add_node("greeter", greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({"message": "Bob"})

{'message': 'Hey Bob, how is your day going?'}
```
<br>
<div align="center">
  <img src="graph.png" alt="Simple Node Graph" />
</div>