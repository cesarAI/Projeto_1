import openai
from dotenv import load_dotenv
import os

# Substitua 'YOUR_OPENAI_KEY' pela sua chave API real
load_dotenv(override=True)
print(os.getenv("OPENAI_API_KEY"))

# Cria uma instância do cliente
client = openai.OpenAI()

# Lista os modelos disponíveis
model_list = client.models.list()

# Imprime os IDs dos modelos disponíveis
for model in model_list.data:
    print(model.id)
