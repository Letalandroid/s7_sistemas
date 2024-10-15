import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Calcular el coeficiente de agrupamiento
coef_agrupamiento = nx.clustering(G)

for nodo, coef in coef_agrupamiento.items():
    print(f"Nodo {nodo} tiene un coeficiente de agrupamiento de {coef:.2f}.")