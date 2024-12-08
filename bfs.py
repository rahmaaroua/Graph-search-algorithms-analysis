from collections import deque
from timeit import default_timer as timer


def breadth_first_search(graph, start, goal):
    start_time = timer()  # Début du chronométrage
   
    visited = set()  # Pour garder une trace des nœuds visités
    queue = deque([(start, [start], 0)])  # File (FIFO) contenant (nœud courant, chemin, coût)


    while queue:
        current_node, path, cost = queue.popleft()


        if current_node == goal:  # Si on atteint le but
            end_time = timer()  # Fin du chronométrage
            print(f"BFS - Chemin trouvé: {path}, Coût total: {cost}, Temps d'exécution: {end_time - start_time:.6f} secondes")
            return path, cost


        if current_node not in visited:
            visited.add(current_node)
            for neighbor, weight in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + weight))


    end_time = timer()
    print(f"BFS - Aucun chemin trouvé. Temps d'exécution: {end_time - start_time:.6f} secondes")
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




print("\n--- BFS ---")
bfs_result = breadth_first_search(graph, 'A', 'P')

