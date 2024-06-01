
from flask import Flask
import requests


app = Flask(__name__)

# consumir api via requests

# url da api
url = 'http://127.0.0.1:8000/cotacao/'

# dicionario enviado para a api
dados = {
    "tamanho":100,
    "ano":2001,
    "garagem":3
}

# dados para autenticacao simples
auth = requests.auth.HTTPBasicAuth('API-HOUSE','12345678')

# resposta da api em json
response = requests.post(url, json=dados, auth=auth)

# mostrar codigo da resposta e resposta em json
print('codigo:' ,response.status_code, response.json())

# rodar request para API
app.run(debug=True, port=7502)