import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('dados.csv')

# Exibe as 5 primeiras linhas
print(df.head())
