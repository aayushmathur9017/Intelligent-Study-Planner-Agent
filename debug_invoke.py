import inspect
from langchain.chat_models import init_chat_model
from langchain import agents
from langchain.tools import tool

def echo(text: str) -> str:
    return text

echo = tool("echo", description="Echo")(echo)
llm = init_chat_model(model="llama2", model_provider="ollama")
agent = agents.create_agent(llm, tools=[echo], debug=True)
print(type(agent))
print(inspect.signature(agent.invoke))
print('has run', hasattr(agent, 'run'))
print('has invoke', hasattr(agent, 'invoke'))
print('has predict', hasattr(agent, 'predict'))
print('has __call__', hasattr(agent, '__call__'))
