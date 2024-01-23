import networkx as nx

class Timeline:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_event(self, timestamp, description):
        self.graph.add_node(timestamp, description=description)

    def add_relationship(self, source, destination):
        self.graph.add_edge(source, destination)

