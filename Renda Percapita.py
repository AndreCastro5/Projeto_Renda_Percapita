# Bibliotecas 
import numpy as np 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 
import os


#Lendo a base de dados 
Base_Dados = pd.read_excel('Dados_Pib.xlsx')

#Verificando
Base_Dados.head(10)

Base_Dados.groupby(by=['Territorialidades','Ano']).mean()

# Sistema de Grids 

# Cor do Fundo 
Cor_Fundo = '#f5f5f5'

# Criar o sistema de Grids 
Grid_Graficos = sns.FacetGrid( Base_Dados, col='Territorialidades', hue='Territorialidades',col_wrap=4)

# Adicionar linhas em cada gráfico 
Grid_Graficos = Grid_Graficos.map(plt.plot,'Ano','PIB per capita')

# Adiconar uma sombra + Ajuste do titulo
Grid_Graficos = Grid_Graficos.map( plt.fill_between,  'Ano', 'PIB per capita', alpha=0.2).set_titles('{col_name} Territorialidades')

# Filtro o titulo
Grid_Graficos = Grid_Graficos.set_titles('{col_name}')

# Adicionar um subtitulo
Grid_Graficos = Grid_Graficos.fig.suptitle (
    'Evolução da renda per capita por Estado',
      fontsize=18
)
# Ajustando 
plt.subplots_adjust(top=0.92)
print(plt.show())