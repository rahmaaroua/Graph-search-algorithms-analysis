from timeit import default_timer as timer


def depth_first_search(graph, start, goal):
    start_time = timer()  # Démarre la mesure avec précision


    stack = [(start, [start], 0)]  # Pile pour DFS
    visited = set()


    while stack:
        current_node, path, cost = stack.pop()
        if current_node == goal:
            end_time = timer()  # Fin de la mesure
            elapsed_time = end_time - start_time
            print(f"DFS - Chemin trouvé: {path}, Coût total: {cost}, Temps d'exécution: {elapsed_time:.9f} secondes")
            return path, cost


        if current_node not in visited:
            visited.add(current_node)
            for neighbor, weight in graph[current_node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + weight))


    end_time = timer()
    elapsed_time = end_time - start_time
    print(f"DFS - Aucun chemin trouvé, Temps d'exécution: {elapsed_time:.9f} secondes")
    return None, float('inf')






graph = {
    'A': [('B', 5), ('C', 2), ('D', 8)],
    'B': [('A', 5), ('E', 10), ('F', 3)],
    'C': [('A', 2), ('G', 4), ('H', 7)],
    'D': [('A', 8), ('I', 6), ('J', 12)],
    'E': [('B', 10), ('K', 3)],
    'F': [('B', 3), ('L', 6)],
    'G': [('C', 4), ('M', 2)],
    'H': [('C', 7), ('N', 5)],
    'I': [('D', 6), ('O', 8)],
    'J': [('D', 12), ('P', 15)],
    'K': [('E', 3)],
    'L': [('F', 6)],
    'M': [('G', 2)],
    'N': [('H', 5)],
    'O': [('I', 8)],
    'P': [('J', 15)]
}




print("\n--- DFS ---")
dfs_result = depth_first_search(graph, 'A', 'P')


