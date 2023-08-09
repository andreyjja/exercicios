import pandas as pd
import numpy as np
from datetime import datetime 
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC



uri = "https://gist.githubusercontent.com/guilhermesilveira/4d1d4a16ccbf6ea4e0a64a38a24ec884/raw/afd05cb0c796d18f3f5a6537053ded308ba94bf7/car-prices.csv"
dados = pd.read_csv(uri)

dados_renomear = {
          "mileage_per_year" : "milhas_por_ano",
          "model_year" : "ano_modelo",
          "price" : "preco",
          "sold" : "vendido"
                  
}

dados = dados.rename(columns=dados_renomear)


dados_yes = {
          "yes" : 1,
          "no" : 0                 
}
dados.vendido = dados.vendido.map(dados_yes)



ano_atual = datetime.today().year
dados['idade_do_carro'] = ano_atual - dados.ano_modelo

dados['km_ano'] = dados.milhas_por_ano * 1.60934

dados = dados.drop(columns = ['Unnamed: 0', "milhas_por_ano", "ano_modelo"], axis=1)




x = dados[["preco","idade_do_carro", "km_ano"]]
y = dados["vendido"]




SEED = 5

np.random.seed(SEED)
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size=0.25, stratify = y)



print(f"treinaremos com {len(treino_x)} e testaremos com {len(teste_x)}")


modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)



dummy = DummyClassifier()

dummy.fit(treino_x, treino_y)
previsoes = dummy.predict(teste_x)
acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia do dummy foi %.2f%%" % acuracia)




np.random.seed(SEED)
raw_treino_x, raw_teste_x, treino_y, teste_y = train_test_split(x, y, test_size = 0.25,
                                                         stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

scaler = StandardScaler()
scaler.fit(raw_treino_x)
treino_x = scaler.transform(raw_treino_x)
teste_x = scaler.transform(raw_teste_x)

modelo = SVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)
