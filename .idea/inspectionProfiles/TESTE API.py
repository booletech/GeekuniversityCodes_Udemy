from Senha import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer OPENAI_{API_KEY}"}
Link = "https://api.openai.com/v1/models"
requisicao = requests.get(Link, headers=headers)

print(requisicao)
print(requisicao.text)
