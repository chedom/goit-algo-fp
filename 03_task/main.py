import networkx as nx

from metro_line import create_metro_graph
from dijkstra import dijkstra_path


def main():
    G = create_metro_graph()
    nodes = list(G.nodes())

    for node in nodes:
        got_shortest_paths = dijkstra_path(G, node)
        expected_shortest_paths = nx.single_source_dijkstra_path(G, source=node)
        shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source=node)
        # test that found path is expected
        for exp_node in expected_shortest_paths:
            expected_path = expected_shortest_paths[exp_node]
            got_distance, got_path = got_shortest_paths[exp_node]
            if not (expected_path == got_path):
                # "Found alternative path with the same distance"
                if got_distance != shortest_path_lengths[exp_node]:
                    raise Exception("Found path is not optimal")


if __name__ == "__main__":
    main()
