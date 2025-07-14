import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_litellm import ChatLiteLLM

load_dotenv()

llm = ChatLiteLLM(
    model="litellm_proxy/ollama/llama3.1:8b",
    api_base=os.environ["LITELLM_PROXY_API_BASE"],
    api_key=os.environ["LITELLM_PROXY_API_KEY"],
)

prompt = """
You are a helpful assistant.  
1) Think about whether you need to call get_weather(city).  
2) If yes, call the get_weather(city) tool with the city from the user.  
3) Immediately reply back with the answer from the first tool call. Do not call the weather tool again, or any other tool.
"""


def get_weather(city: str) -> str:
    """Return a weather summary for the given city."""
    return f"It's always sunny in {city}!"


agent = create_react_agent(model=llm, tools=[get_weather], prompt=prompt)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What’s the weather in SF?"}]},
    config={"recursion_limit": 50},
)

print(result)