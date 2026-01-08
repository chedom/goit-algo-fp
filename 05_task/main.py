import uuid
import heapq
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, algo_name: str):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    fig = plt.figure(figsize=(8, 5))
    # added displayed title
    fig.canvas.manager.set_window_title(f"{algo_name} Visualization")
    plt.title(f"Traverse tree: {algo_name}")

    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)


def generate_gradient(start_color, end_color, steps):
    """
    Generates a list of RGB colors between two given colors.
    Steps corresponds to the number of nodes
    """
    gradient = []

    for i in range(steps):
        t = i / (steps - 1)  # the mixing factor
        # interpolate each channel
        r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
        # Normalize by dividing by 255.0 to get range 0.0 - 1.0
        gradient.append((r/255.0, g/255.0, b/255.0))

    return gradient


def dfs_colors(root: Node, gradient):
    """
    Change the color of nodes according DFS algorithm
    """
    if root is None:
        return

    stack = [root]
    step = 0

    while stack:
        node = stack.pop()
        node.color = gradient[step]
        step += 1

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


def bfs_colors(root: Node, gradient):
    """
    Change the color of nodes according BFS algorithm
    """
    if root is None:
        return

    queue = deque([root])
    step = 0

    while queue:
        node = queue.popleft()
        node.color = gradient[step]
        step += 1

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


def convert_heap_to_tree(heap):
    if not heap:  # empty heap
        return
    # preinitialize nodes without left/right children
    nodes = [Node(val) for val in heap]
    size = len(nodes)

    idx = 0
    last_parent_idx = (size - 2) / 2

    while idx <= last_parent_idx:
        # 2i + 1 - left element
        # 2i + 2 - right element
        left_idx = 2*idx + 1
        rigth_idx = 2*idx + 2

        nodes[idx].left = nodes[left_idx]
        # rigth child could be absent
        if rigth_idx <= size - 1:
            nodes[idx].right = nodes[rigth_idx]

        idx += 1

    return nodes[0]  # return head


def demo():
    """
    Draw 2 figures: 1 - DFS visualization, 2 - BFS visualization
    """
    dark_color = (0, 0, 65)  # Dark blue (start)
    light_color = (200, 230, 255)  # Light blue (end)

    heap = [0, 4, 5, 10, 1, 3]
    heapq.heapify(heap)
    print(heap)
    root = convert_heap_to_tree(heap)

    gradient = generate_gradient(dark_color, light_color, len(heap))

    dfs_colors(root, gradient)
    draw_tree(root, "DFS")
    bfs_colors(root, gradient)
    draw_tree(root, "BFS")
    plt.show()


def main():
    demo()


if __name__ == "__main__":
    main()
