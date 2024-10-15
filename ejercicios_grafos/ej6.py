import networkx as nx

# Crear un grafo
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])

# Calcular el centralidad
centralidad = nx.degree_centrality(G)

for nodo, central in centralidad.items():
    print(f"Nodo {nodo} tiene una centralidad de {central:.2f}.")