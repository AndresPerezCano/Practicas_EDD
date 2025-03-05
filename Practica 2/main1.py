import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

archivo = "Practica 2/Datos vias.xlsx"  
df = pd.read_excel(archivo)  
df.columns = ["Origen","Destino","KM","Minutos"]
df = df.drop(0)
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
coso = pd.DataFrame(matriz_adyacencia,index=nodos,columns=nodos)
#print("Matriz de adyacencia 1:")
#print(coso.to_string())
#print("Matriz de adyacencia 2:")
#print(matriz_adyacencia2)
Grafo = nx.Graph()
Grafo.add_nodes_from(nodos)
for i in range(matriz_adyacencia.shape[0]):
  for j in range(matriz_adyacencia.shape[0]):
    if matriz_adyacencia[i,j] != 0:
      Grafo.add_edge(nodos[i],nodos[j],km=matriz_adyacencia[i,j],minutos=matriz_adyacencia2[i,j])
#pesos = nx.get_edge_attributes(Grafo,"km")
#print("KM:",pesos)
#pesos1 = nx.get_edge_attributes(Grafo,"minutos")
#print("minutos:",pesos1)
import heapq
import sys

def initialize_single_source(G, s):
    d = {u: sys.maxsize for u in G}
    d[s] = 0
    pi = {u: None for u in G}
    return d, pi

def relax(u, v, W, d, pi):
    if d[v] > d[u] + W[u][v]:
        d[v] = d[u] + W[u][v]
        pi[v] = u

def DIJKSTRA(G, W, s): 
    Sv = []
    Q = [(0, s)] 
    d, pi = initialize_single_source(G, s)

    while Q:
        _, u = heapq.heappop(Q)
        if u in Sv: 
            continue
        Sv.append(u)
        
        for v in G[u]:
            relax(u, v, W, d, pi)
            heapq.heappush(Q, (d[v], v)) 

    return d, pi

G = {node: list(Grafo.neighbors(node)) for node in Grafo.nodes}
WKm = {node: {neighbor: Grafo[node][neighbor]['km'] for neighbor in Grafo.neighbors(node)} for node in Grafo.nodes}
WMin = {node: {neighbor: Grafo[node][neighbor]['minutos'] for neighbor in Grafo.neighbors(node)} for node in Grafo.nodes}
def camino_Mas_corto_KM(Origen,Destino):
  valores, predecesores =  DIJKSTRA(G,WKm,Origen)
  print(f"La distancia mas corta en Km entre {Origen} y {Destino} es: {valores[Destino]}")
  camino = []
  valor = Destino
  while True:
    if valor != Origen:
      camino.insert(0,valor)
      valor = predecesores[valor]
    else:
      camino.insert(0,Origen)
      break
  print("El recorrido es: [",end="")
  for ciudad in camino:
    if ciudad == Destino:
      print(f"{ciudad}]")
    else:
      print(f"{ciudad} - ",end="")
  
def camino_Mas_corto_Minutos(Origen,Destino):
  valores, predecesores =  DIJKSTRA(G,WMin,Origen)
  print(f"El tiempo en minutos del camino mas entre {Origen} y {Destino} es: {valores[Destino]}")
  camino = []
  valor = Destino
  while True:
    if valor != Origen:
      camino.insert(0,valor)
      valor = predecesores[valor]
    else:
      camino.insert(0,Origen)
      break
  print("El recorrido es: [",end="")
  for ciudad in camino:
    if ciudad == Destino:
      print(f"{ciudad}]")
    else:
      print(f"{ciudad} - ",end="")
#Pedir al usuario:
while True:
    print("Que busqueda desea realizar: ")
    print("1.......")
    print("2.Determinar el camino más corto(Km) entre A Y B: ")
    print("3.Determinar el camino más corto(Minutos) entre A Y B: ")
    print("4.Salir")
    indice = int(input("Ingrese indice: "))
    if indice == 1:
        pass
    
    elif indice == 2:
        origen = input("Ingrese la ciudad de origen: ")
        destino = input("Ingrese la ciudad de destino: ")
        camino_Mas_corto_KM(origen,destino)

        indice1 = input("Desea realizar otra acción(si/no): ")
        if indice1 == "si":
            pass
        else: 
            break
    
    elif indice == 3:
        origen = input("Ingrese la ciudad de origen: ")
        destino = input("Ingrese la ciudad de destino: ")
        camino_Mas_corto_Minutos(origen,destino)

        indice1 = input("Desea realizar otra acción(si/no): ")
        if indice1 == "si":
            pass
        else: 
            break
    
    elif indice == 4:
        break
