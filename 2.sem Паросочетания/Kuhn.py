graph = {
    0: [3, 4],    # Кандидат 0 может пойти на вакансии 3 или 4
    1: [3],       # Кандидат 1 может только на 3
    2: [4, 5],    # Кандидат 2 может на 4 или 5
    3: [0, 1],    # Обратные связи для вакансий (нужны для bipartite)
    4: [0, 2],
    5: [2]
}


def bipartite(graph):

    V = len(graph.keys())
    colors = [-1] * V

    for start in range(V):
        if colors[start] == -1:  # -1 = отсутствие цвета
            queue = [start]
            colors[start] = 0

            while queue:
                v = queue.pop(0)
                for u in graph[v]:
                    if colors[u] == -1:
                        colors[u] = 1 - colors[v]
                        queue.append(u)
                        # если сосед уже окрашен в тот же цвет, то граф не двудольный
                    elif colors[u] == colors[v]:
                        return False, []    

    set1 = [i for i in range(V) if colors[i] == 0]
    set2 = [i for i in range(V) if colors[i] == 1]    

    return True, (set1, set2)

def Kuhn(graph):
    V = len(graph.keys())
    match = [-1] * V
    visited = [False] * V
    _, parts = bipartite(graph)
    
    if not _:
        return 0
    
    L = parts[0]
    def DFS(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] == -1 or DFS(match[u]):
                    match[u] = v
                    return True
        return False

    max_matching = 0
    for v in L:
        visited = [False] * V
        if DFS(v):
            max_matching += 1
    return max_matching            

   