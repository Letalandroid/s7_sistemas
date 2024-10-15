import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import networkx as nx
import math
import sympy as sp

class NetworkTrafficAnalysis:
    def __init__(self, response_times):
        self.response_times = np.array(response_times)  # Matriz de tiempos de respuesta entre servidores (en ms)
        self.servers = len(response_times)  # Número de servidores
        self.symbol = sp.Symbol('x')

    # Operación básica con NumPy: Promedio de tiempos de respuesta
    def average_response_time(self):
        return np.mean(self.response_times)

    # Graficar la tendencia de los tiempos de respuesta
    def plot_response_trend(self):
        time_indices = np.arange(self.servers)
        avg_times = np.mean(self.response_times, axis=1)  # Promedio por servidor
        plt.plot(time_indices, avg_times, marker='o')
        plt.title('Average Response Time per Server')
        plt.xlabel('Server Index')
        plt.ylabel('Average Response Time (ms)')
        plt.grid(True)
        plt.show()

    # Mostrar tabla con los tiempos de respuesta y su logaritmo
    def show_response_table(self):
        table = PrettyTable()
        table.field_names = ["Server", "Avg Response Time (ms)", "Log Response Time"]
        avg_times = np.mean(self.response_times, axis=1)
        for i, time in enumerate(avg_times):
            table.add_row([f"Server {i+1}", round(time, 2), round(math.log(time), 2)])
        print(table)

    # Crear y mostrar un grafo de la topología de la red usando NetworkX
    def create_network_graph(self):
        G = nx.Graph()
        for i in range(self.servers):
            G.add_node(i, label=f'Server {i+1}')
        for i in range(self.servers):
            for j in range(i+1, self.servers):
                if self.response_times[i][j] < 200:  # Solo conectamos servidores con menos de 200 ms de latencia
                    G.add_edge(i, j, weight=self.response_times[i][j])
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Network Topology and Response Times")
        plt.show()

    # Graficar la función de carga en la red (hipotética) usando Sympy
    def plot_network_load(self):
        load_function = sp.sin(self.symbol) * sp.exp(-self.symbol/10)  # Función simbólica de la carga
        x_vals = np.linspace(0, 20, 100)
        f = sp.lambdify(self.symbol, load_function, "numpy")
        y_vals = f(x_vals)
        plt.plot(x_vals, y_vals)
        plt.title("Hypothetical Network Load Over Time")
        plt.xlabel('Time (s)')
        plt.ylabel('Load')
        plt.grid(True)
        plt.show()

# Ejemplo de uso en la vida real
response_times = [
    [0, 100, 150, 90],
    [100, 0, 160, 120],
    [150, 160, 0, 110],
    [90, 120, 110, 0]
]  # Matriz de tiempos de respuesta (en ms) entre servidores

network_analysis = NetworkTrafficAnalysis(response_times)

# Cálculo del tiempo promedio de respuesta
print("Promedio del tiempo de respuesta en la red (ms):", network_analysis.average_response_time())

# Graficar la tendencia de los tiempos de respuesta promedio
network_analysis.plot_response_trend()

# Mostrar una tabla con los tiempos de respuesta promedio y sus logaritmos
network_analysis.show_response_table()

# Crear un grafo que represente la topología de la red
network_analysis.create_network_graph()

# Graficar una función hipotética de la carga en la red
network_analysis.plot_network_load()