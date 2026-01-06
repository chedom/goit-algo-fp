import heapq


def dijkstra_path(graph, from_node) -> dict[(float, list[str])]:
    nodes = graph.nodes()
    # distance is represented by distance and path
    distances = {vertex: (float('infinity'), []) for vertex in nodes}
    distances[from_node] = (0, [from_node])
    unvisited = [(0, from_node)]  # heap to select closest node
    seen = set()  # track visited nodes

    while unvisited:
        # Find the vertex with min distance to `from_node`
        # distance is only used for heap
        _, current_vertex = heapq.heappop(unvisited)

        cur_distance, cur_path = distances[current_vertex]
        if cur_distance == float('infinity'):
            # all available routes have been checked
            break

        for neighbor in graph[current_vertex]:
            weight = graph[current_vertex][neighbor]["weight"]
            distance = cur_distance + weight  # new distance
            # If new distance is shorter than update shortest path
            if distance < distances[neighbor][0]:
                distances[neighbor] = (distance, cur_path+[neighbor])

            if neighbor not in seen:  # add neighbor node to heap with update distance
                heapq.heappush(unvisited, (distances[neighbor][0], neighbor))
        # remove current vertex from unvisited nodes
        seen.add(current_vertex)

    return distances
