from langchain.chat_models import init_chat_model
from langchain import agents
from langchain.tools import tool


def create_study_plan(query: str) -> str:
    return 'ok'

create_study_plan = tool('create_study_plan', description='Create plan')(create_study_plan)
llm = init_chat_model(model='llama2', model_provider='ollama')
agent = agents.create_agent(llm, tools=[create_study_plan], debug=True)
print('get_input_schema:', agent.get_input_schema())
print('get_input_jsonschema:', agent.get_input_jsonschema())
print('input_schema attr:', getattr(agent, 'input_schema', None))
print('get_output_schema:', agent.get_output_schema())
print('get_name:', agent.get_name())
print('schema_to_mapper', agent.schema_to_mapper)
