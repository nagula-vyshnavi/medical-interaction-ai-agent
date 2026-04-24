from langgraph.graph import StateGraph
from typing import TypedDict
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise Exception("GROQ_API_KEY missing")

client = Groq(api_key=api_key)

# STATE
class AgentState(TypedDict):
    input: str
    output: str
    sentiment: str
    followup: str
    hcp: str

# NODES
def log_interaction(state):
    text = state.get("input", "")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": text}]
    )
    return {
        "input": text,
        "output": response.choices[0].message.content
    }

def sentiment_tool(state):
    text = state.get("input", "")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"Classify sentiment: {text}"
        }]
    )
    return {
        "sentiment": response.choices[0].message.content
    }

def followup_tool(state):
    text = state.get("input", "")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"Suggest follow-up action: {text}"
        }]
    )
    return {
        "followup": response.choices[0].message.content
    }

def fetch_hcp(state):
    return {
        "hcp": "Fetched HCP details successfully"
    }

def edit_interaction(state):
    return {
        "input": state.get("input", ""),
        "output": state.get("output", ""),
        "sentiment": state.get("sentiment", ""),
        "followup": state.get("followup", ""),
        "hcp": state.get("hcp", "")
    }

# GRAPH
graph = StateGraph(AgentState)

graph.add_node("log", log_interaction)
graph.add_node("sentiment", sentiment_tool)
graph.add_node("followup", followup_tool)
graph.add_node("fetch", fetch_hcp)
graph.add_node("edit", edit_interaction)

graph.set_entry_point("log")

graph.add_edge("log", "sentiment")
graph.add_edge("sentiment", "followup")
graph.add_edge("followup", "fetch")
graph.add_edge("fetch", "edit")

app_graph = graph.compile()