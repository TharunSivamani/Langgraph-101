from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    messages: List[HumanMessage]

llm = ChatOllama(model="gemma3:4b")

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state['messages'])
    print(f"\nAI Response: {response.content}")
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

user_input = input("Enter something .... ")
agent.invoke({"messages": [HumanMessage(content=user_input)]})