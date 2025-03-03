import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 📌 1. Cargar el archivo Excel
archivo = "Practica 2/Datos vias.xlsx"  # Nombre del archivo
df = pd.read_excel(archivo)  # Leer la hoja "datos"
df.columns = ["Origen","Destino","KM","Minutos"]
df = df.drop(0)
#origen = pd.Series(df["Origen"].unique())
#destino = pd.Series(df["Destino"].unique())
#concatenar = pd.concat([origen,destino]).drop_duplicates().reset_index(drop=True)
nodos = np.unique(np.concatenate((df["Origen"],df["Destino"])))
matriz_adyacencia = np.zeros((len(nodos),len(nodos)))
matriz_adyacencia2 = np.zeros((len(nodos),len(nodos)))
for index, row in df.iterrows():
  origen = row["Origen"]
  destino = row["Destino"]
  peso1 = row["KM"]
  peso2 = row["Minutos"]
  indice_origen = np.where(nodos == origen)[0][0]
  indice_destino = np.where(nodos == destino)[0][0]
  matriz_adyacencia[indice_origen,indice_destino] = peso1
  matriz_adyacencia[indice_destino, indice_origen] = peso1
  matriz_adyacencia2[indice_origen, indice_destino] = peso2
  matriz_adyacencia2[indice_destino, indice_origen] = peso2
#coso = pd.DataFrame(matriz_adyacencia,index=nodos,columns=nodos)
#print("Matriz de adyacencia 1:")
#print(coso.to_string())
#print("Matriz de adyacencia 2:")
#print(matriz_adyacencia2)
