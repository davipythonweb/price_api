

# para importar arquivos
# from google.colab import files
# uploaded = files.upload()

import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/1576-mlops-machine-learning/aula-5/casas.csv'
# dados de preços de casas site ==> https://www.kaggle.com/c/house-prices-advanced-regression-techniques

dados = pd.read_csv(url)
dados.head()

# aplicando um filtro
#colunas = ['tamanho', 'preco']
#dataframe = dados[colunas]

#criando as variaveis explicativa e resposta
X = dados.drop('preco', axis=1)
y = dados['preco']


# pip install sklearn-0.0.post5
#divisão do modelo em base de treino e base de teste
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

X_train.head()


#ajuste do modelo em cima da base de treino
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X_train, y_train)

#coeficientes da regressão linear
 #uma variavel que é o parametro
modelo.coef_

# o ponto onde ele cruza
modelo.intercept_


#predição do preço da casa com o modelo, recebendo 3 valores:tamanho,ano,garagem
modelo.predict([[120,2001,2]])

{
    "tamanho":120,
    "ano":2001,
    "garagem":2
}

# biblipteca para salvar projeto
import pickle

# salvou o modelo de predicao no colab
pickle.dump(modelo, open('modelo.sav', 'wb'))

# files.download('modelo.sav')