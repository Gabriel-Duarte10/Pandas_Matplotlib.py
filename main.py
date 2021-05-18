import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv")

op = input("Digite o pais da Sua escolha: ")

df2 = df[df['location'] == op]

df2.to_csv('C:/teste/csv_EX02.csv')

df3 = pd.Series([
    df.loc[df['total_cases'] == df['total_cases'].max(), 'location'].head(1).to_string(),
    df.loc[df['total_cases'] == df['total_cases'].min(), 'location'].head(1).to_string(),
    df.loc[df['new_cases'] == df['new_cases'].max(), 'location'].head(1).to_string(),
    df.loc[df['new_cases'] == df['new_cases'].min(), 'location'].head(1).to_string(),
], index=['Max total cases', 'Min total cases', 'Max new cases', 'Min new cases'])

df3.to_csv('C:/teste/csv_EX03.csv')

pa = input("Digite o pais 1 para o grafico: ")

pa2 = input("Digite o pais 2 para o grafico: ")

con = input("Digite a coluna: ")

dat1 = input("Digite a data 1: EX(AAAA-MM-DD): ")

dat2 = input("Digite a data 2: EX(AAAA-MM-DD): ")

pais1 = df.loc[(df['location'] == pa) & (df['date'] >= dat1) & (df['date'] <= dat2)]

pais2 = df.loc[(df['location'] == pa2) & (df['date'] >= dat1) & (df['date'] <= dat2)]

plt.plot(pais1.date, pais1[con] / pais1[con].iloc[0] * 100)
plt.plot(pais2.date, pais2[con] / pais2[con].iloc[0] * 100)
plt.title("Covid " + con)
plt.xlabel('date')
plt.ylabel(con)
plt.legend([pa, pa2])
plt.show()


