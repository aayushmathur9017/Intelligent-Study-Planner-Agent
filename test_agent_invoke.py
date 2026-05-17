from langchain.chat_models import init_chat_model
from langchain import agents
from langchain.tools import tool
from langchain_core.messages import HumanMessage


def create_study_plan(query: str) -> str:
    return 'ok'

create_study_plan = tool('create_study_plan', description='Create plan')(create_study_plan)
llm = init_chat_model(model='llama2', model_provider='ollama')
agent = agents.create_agent(llm, tools=[create_study_plan], debug=True)
response = agent.invoke({'messages': [HumanMessage(content='Hello from user')]})
print(type(response))
print(response)
