import networkx as nx
from utils import calculate_paradox_risk

def explore_timeline(timeline, exploration_depth, energy_budget):
    G = timeline.graph
    current_timestamp = 0

    for i in range(exploration_depth):
        
        energy_budget -= 5

        
        neighbors = list(G.successors(current_timestamp))
        if neighbors:
            next_timestamp = neighbors[0]  
            current_timestamp = next_timestamp

            
            paradox_risk = calculate_paradox_risk(current_timestamp)

           
            print(f"Step {i + 1}: Moved to timestamp {current_timestamp}, Paradox Risk: {paradox_risk}")

        
        if energy_budget <= 0:
            print("Exploration terminated due to exhausted energy budget")
            break
def check_ethical_constraints(timestamp, ethical_constraints):
    
    return timestamp not in ethical_constraints
