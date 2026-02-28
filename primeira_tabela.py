import pandas as pd

dados = {
    'Produto': ['Playstation 5', 'Xbox series S', 'Nintendo Switch 2'],
    'Preço': [3000.00, 2700.00, 2800.00],
    'Estoque': [10,12,5]
}

df = pd.DataFrame(dados)
print(df)