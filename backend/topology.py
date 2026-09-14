# topology.py

import networkx as nx


def create_network():

    network = nx.Graph()

    # Add devices
    devices = ["R1", "R2", "R3", "R4"]

    network.add_nodes_from(devices)

    # Add network connections
    network.add_edges_from([
        ("R1", "R2"),
        ("R2", "R3"),
        ("R3", "R4")
    ])

    return network
