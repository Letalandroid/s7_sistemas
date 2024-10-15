import networkx as nx

G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

ruta_corta = nx.shortest_path(G, source=1, target=4)

print(f"La ruta más corta de 1 a 4 es: {ruta_corta}")