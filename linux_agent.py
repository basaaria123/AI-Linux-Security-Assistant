import os
from typing import TypedDict, Annotated, List, Union
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage, ToolMessage
from langgraph.graph import StateGraph, END
from tools import explain_linux_command, check_linux_permissions, get_hardening_tips
from prompts import SYSTEM_PROMPT
from dotenv import load_dotenv

load_dotenv()

# Define the state
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], lambda x, y: x + y]

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# Define tools
tools = [explain_linux_command, check_linux_permissions, get_hardening_tips]
tool_map = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools)

# Define nodes
def call_model(state):
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

def call_tool(state):
    last_message = state['messages'][-1]
    tool_messages = []
    
    if not last_message.tool_calls:
        return {"messages": []}

    for tool_call in last_message.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_id = tool_call["id"]
        
        if tool_name in tool_map:
            response = tool_map[tool_name].invoke(tool_args)
            tool_messages.append(ToolMessage(content=str(response), tool_call_id=tool_id))
    
    return {"messages": tool_messages}

def should_continue(state):
    last_message = state['messages'][-1]
    if last_message.tool_calls:
        return "continue"
    return "end"

# Build the graph
workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", call_tool)

workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", should_continue, {"continue": "tools", "end": END})
workflow.add_edge("tools", "agent")

app_agent = workflow.compile()

def run_linux_assistant(user_input: str):
    inputs = {"messages": [HumanMessage(content=user_input)]}
    final_state = app_agent.invoke(inputs)
    return final_state["messages"][-1].content
