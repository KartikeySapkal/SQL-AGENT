import json
from my_database.db_connector import get_db_connection
get_db_connection()
from ollama import Client
client = Client(host='http://localhost:11434')

with open("schema_info.json", "r") as file:
    SCHEMA_INFO = json.load(file)

prompt = f'''
    Based on the following schema information, generate a context for the LLM, to generate better queries.
    {SCHEMA_INFO}
'''

stream = client.chat(model='llama3.2', messages=[
    {
    'role': 'user',
    'content':  prompt,
        },
    ],
    options={
        "temperature": 0.4,
        "top_p": 0.95,
        "max_tokens": 200,
        "stop": ["\n\n", "###"]
    },
    stream = True,
)

print(SCHEMA_INFO)