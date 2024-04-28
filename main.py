from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# Força a recarga do arquivo .env
load_dotenv(override=True)
print(os.getenv("OPENAI_API_KEY"))
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content":"Listar apenas os nomes dos produtos, sem considerar descrição."
        },
        {
            "role":"user",
            "content":"Liste 3 produtos sustentáveis"
        }
    ],
    model="gpt-3.5-turbo"
)

print(resposta.choices[0].message.content)



