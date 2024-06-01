import app
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

from sklearn.linear_model import LinearRegression
import pickle
import os
from dotenv import load_dotenv

load_dotenv()


# dados para previsao do modelo treinado
colunas = ['tamanho', 'ano', 'garagem']

# serializacao com pickle  para carregar a variavel criada no google colab
modelo = pickle.load(open('app/modelo.sav', 'rb'))

# intanciando o app flask
app = Flask(__name__)

# configuracao e autenticacao simples
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('AUTH_PASSWORD')
basic_auth = BasicAuth(app)

# endpoint '/' da API
@app.route('/')
def home():
    return "Seja Bem vindo a API price-house"

# endpoint API previsao do preco da casa , dado o tamanho,ano,garagem da casa.
@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    resposta = request.get_json()
    resposta_input = [resposta[col] for col in colunas]
    preco = modelo.predict([resposta_input])
    
    return jsonify(preco=preco[0].round(2))



# rodar API
if __name__ == "__main__":
    app.run( debug=True,port=8000)