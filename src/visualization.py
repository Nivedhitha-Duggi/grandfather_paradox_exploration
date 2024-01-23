import matplotlib.pyplot as plt
import networkx as nx
from utils import calculate_paradox_risk

def dynamic_visualization_enhanced(timeline, exploration_depth, energy_budget):
    G = timeline.graph
    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 6))

    for i in range(exploration_depth):
        current_timestamp = 0
        plt.scatter(pos[current_timestamp][0], pos[current_timestamp][1], color='red', s=200, label='Current Position')
        
        for node in G.nodes:
            if node == current_timestamp:
                continue

          
            paradox_risk = calculate_paradox_risk(node)

            plt.scatter(pos[node][0], pos[node][1], c=[[paradox_risk]], cmap='viridis', s=100)

        plt.title(f"Dynamic Visualization - Step {i + 1}")
        plt.legend()
        plt.show()

