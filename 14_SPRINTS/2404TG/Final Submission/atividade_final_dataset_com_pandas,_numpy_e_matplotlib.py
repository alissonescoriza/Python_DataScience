# -*- coding: utf-8 -*-
"""Atividade Final - Dataset com pandas, numpy e matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mZZPbsXrh-1LRpFYYn9-q904aJ-FDzLZ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('tmsp.csv', encoding='ISO-8859-1', sep=';')

dados

dados.drop("OUTRAS REMUNERAÇÕES", axis=1, inplace=True)

# Verificar o tamanho do conjunto de dados
print("Tamanho do conjunto de dados:", dados.shape)

# Verificar os tipos de dados de cada coluna
print("\nTipos de dados de cada coluna:")
print(dados.dtypes)

# Verificar se há valores ausentes
print("\nValores ausentes por coluna:")
print(dados.isnull().sum())

# Obter estatísticas descritivas das variáveis numéricas
print("\nEstatísticas descritivas das variáveis numéricas:")
print(dados.describe())

# Explorar a distribuição das variáveis categóricas
print("\nDistribuição das variáveis categóricas:")
for column in dados.select_dtypes(include=['object']).columns:
    print("\n", column)
    print(dados[column].value_counts())

dados_agrupados = dados.groupby("CARGO")
dados_agrupados.head()



# Substituindo vírgulas por vazio na coluna "vencimento"
dados["VENCIMENTOS"] = dados["VENCIMENTOS"].str.replace(",", "")

# Convertendo a coluna "vencimento" para tipo numérico
dados["VENCIMENTOS"] = pd.to_numeric(dados["VENCIMENTOS"], errors='coerce')

#Calculando o Desvio Padrão para Verificar a Dispersão
desvio_padrao_cargo = dados_agrupados["VENCIMENTOS"].std()
amplitude_cargo = dados_agrupados["VENCIMENTOS"].max() - dados_agrupados["VENCIMENTOS"].min()

salario_media = dados['VENCIMENTOS'].mean()
salario_moda = dados['VENCIMENTOS'].mode()
salario_mediana = dados['VENCIMENTOS'].median()

for cargo, valores in dados_agrupados:
    print(f"\nCargo: {cargo}")
    print(f"Média Salarial: {salario_media:.2f}")
    print(f"Mediana Salarial: {salario_mediana:.2f}")
    print(f"Moda Salarial: {salario_moda}")
    print(f"Desvio Padrão Salarial: {desvio_padrao_cargo[cargo]:.2f}")
    print(f"Amplitude Salarial: {amplitude_cargo[cargo]:.2f}")

dados.head()

# Obter informações descritivas da coluna
print(dados["CARGO"].describe())

# Visualizar os primeiros valores da coluna
print(dados["CARGO"].head())

# Verificar o tipo de dados da coluna
print(dados["CARGO"].dtype)

# Obter valores únicos da coluna
print(dados["CARGO"].unique())

# Contar a frequência de cada valor único
print(dados["CARGO"].value_counts())

# Criar um dicionário de mapeamento para converter categorias em valores inteiros
dicionario_cargo = {
    "PROFESSOR DE ORQUESTRA": 1,
    "ASSESSOR I": 2,
    "ASSESSOR II": 3,
    "ASSESSOR III": 4,
    "ASSESSOR IV": 5,
    "ASSESSOR VI": 6,
    "SUPERVISOR": 7,
    "CHEFE DE NUCLEO I": 8,
    "DIRETOR II": 9,
    "CANTOR DE CORAL": 10,
    "AGENTE DE APOIO": 11,
    "PROFESSOR DE DANÇA": 12,
    "PROFESSOR DE QUARTETO DE CORDAS": 13,
    "ASS. GESTÃO DE POLÍTICAS PÚBLICAS": 14,
    "DIRETOR GERAL": 15,
}

dados["CARGO"] = dados["CARGO"].replace(dicionario_cargo)
dados.head()

# Calcule a distribuição de frequência da coluna 'CARGO'
frequencia_cargos = dados['CARGO'].value_counts()

# Crie o histograma
plt.figure(figsize=(10, 6))
frequencia_cargos.plot(kind="bar", color=plt.cm.viridis.colors)
plt.xlabel("CARGO")
plt.ylabel("VENCIMENTOS")
plt.title("Distribuição de Cargos")
plt.xticks(rotation=45, ha="right")  # Gire os rótulos dos cargos para melhor visualização
plt.tight_layout()
plt.show()

# Crie um box plot para a coluna "VENCIMENTOS"
dados["VENCIMENTOS"].plot(kind="box")

# Adicionando nomes para as labels e títulos
plt.xlabel("Salários")
plt.ylabel("Valor")
plt.title("Boxplot dos Salários")

# Mostrar a planilha
plt.show()

dados_agrupados = dados.groupby("CARGO")
media_salarial_cargo = dados_agrupados["VENCIMENTOS"].mean()
media_salarial_cargo

cargo_maior_media = media_salarial_cargo.idxmax()
maior_media_salarial = media_salarial_cargo[cargo_maior_media]
print(f"Cargo com a maior média salarial: {cargo_maior_media}")
print(f"Média salarial do cargo com a maior média: {maior_media_salarial:.2f}")

# Calcula a média salarial para cada posição
mediana_salarial_cargo = dados_agrupados["VENCIMENTOS"].median()

# Identifica o índice da posição com a maior média salarial
cargo_maior_mediana = mediana_salarial_cargo.idxmax()

# Obtenha o valor real do salário médio mais alto
maior_mediana_salarial = mediana_salarial_cargo[cargo_maior_mediana]

# Printar os resultados
print(f"\nCargo com maior mediana salarial: {cargo_maior_mediana}")
print(f"Maior mediana salarial: {maior_mediana_salarial}")

# Informações adicionais sobre o cargo com o maior salário médio
cargo_info = dados[dados["CARGO"] == cargo_maior_mediana]


print(f"\nInformações adicionais sobre o cargo {cargo_maior_mediana}:")
print(cargo_info.describe())