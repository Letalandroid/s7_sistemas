import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

grado = G.degree()

for nodo, g in grado:
    print(f"Nodo {nodo} tiene grado {g}.")