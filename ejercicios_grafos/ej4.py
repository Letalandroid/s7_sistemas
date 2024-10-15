import networkx as nx

# Crear un grafo
G = nx.Graph()
G.add_edges_from([(1, 2), (3, 4)])

# Encontrar componentes conexas
componentes = list(nx.connected_components(G))

print(f"Las componentes conexas son: {componentes}")