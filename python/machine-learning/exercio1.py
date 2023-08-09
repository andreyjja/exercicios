import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

seed = 20

uri = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
dados = pd.read_csv(uri)


x = dados[["home","how_it_works","contact"]]
y = dados["bought"]

treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, random_state = seed, test_size=0.25, stratify = y)


print(f"treinaremos com {len(treino_x)} e testaremos com {len(teste_x)}")

modelo = LinearSVC()

modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

taxa_de_acerto = accuracy_score(teste_y, previsoes)

print(f"o resultado é {taxa_de_acerto}")





