from openai import OpenAI
from dotenv import load_dotenv
import os

# Força a recarga do arquivo .env
load_dotenv(override=True)
print(os.getenv("OPENAI_API_KEY"))

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#, project="proj_UQWenLI5BHQJGuz9wueyq7OS")

model = "gpt-4"
temperature = 0
max_tokens = 200

def categoriza_produto(nome_produto, lista_categorias_possiveis):
    

    prompt_sistema = f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.

        # Lista de Categorias Válidas
        {lista_categorias_possiveis.split(",")}

        # Formato da Saída
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto

        # Exemplo de Saída
        Produto: Escova elétrica com recarga solar
        Categoria: Eletrônicos Verdes
    """

    resposta = cliente.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content": prompt_sistema
            },
            {
                "role":"user",
                "content": nome_produto
            }
        ],
        model = model,
        temperature = temperature,
        max_tokens = max_tokens,
    )

    return resposta.choices[0].message.content

categorias_validas = input("Informe as categorias válidas, separando por vírgula: ")

while True:
    nome_produto = input("Digite o nome do produto: ")
    texto_resposta = categoriza_produto(nome_produto, categorias_validas)
    print(texto_resposta)





