import requests
import pandas as pd
from plyer import notification


def alerta(mensagem):
    notification.notify(
        title='Alerta de falha no carregamento de Dados',
        message=mensagem,
        app_name='Pipeline de Dados',
        timeout=10)


api_url = "https://restcountries.com/v3.1/all"

response = requests.get(api_url)

if response.status_code == 200:
    data_json = response.json()
else:
    alerta('Erro ao acessar a API')

names = []
capital = []
subregion = []

for pais in data_json:
    names.append(pais["name"]["common"])
    capital.append(pais["capital"][0] if "capital" in pais else "N/A")
    subregion.append(pais["subregion"] if "subregion" in pais else "N/A")

paises = pd.DataFrame({
    "Nome do País": names,
    "Capital": capital,
    "Sub Região": subregion
})

print(paises.head(10))
