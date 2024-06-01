# API com python ==> previsão de preço de casa

* usando um propio modelo machine learning de previsao com sklearn no endpoint(cotacao)
* usar o postman para USAR o metodo POST na API de cotação do preço da casa
* usando o metodo de serializaçao com a biblioteca pickle para carregar o modelo do ambiente de desenvolvimento colab e salvalo em arquivo e carregar na API para a predição

* autenticaçao basica com nome de usuario e senha com a biblioteca flask-basisauth
* usando virtualenv como ambiente virtual do projeto 
* salvando as dependecias no requirements

* arquivo request é a simulação para consumir a API de preço de casas com a biblioeca requests na url = 'http://localhost:8000/cotacao/'

-arquivo ==> modelo.sav 
-==> arquivo serializado com pickle da variavel de machine learning criada no google colab
-para treinar o modelo = treino_modelo.py

-criar ambiente ==> virtualenv -p python3 environment
-ativar ambiente==> source environment/bin/activate
-desativar ambiente==> deactivate
-instalar requirements==> pip install -r requirements.txt
-resolver erro do sklearn ==> pip install -U scikit-learn
-rodar arquivo da API ==> python main.py
-rodar arquivo do consumo API via requests ==> python request.py

* como usar

`url da api` url = 'http://127.0.0.1:8000/cotacao/'

`# dicionario enviado para a api`
dados = {
    "tamanho":120,
    "ano":2001,
    "garagem":2
}
