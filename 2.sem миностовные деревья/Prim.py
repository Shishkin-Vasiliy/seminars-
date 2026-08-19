graph = {0:[(1,2), (2, 3)] ,1:[(0, 2), (3, 5), (2, 100)], 2: [(0, 3), (1, 100), (3, 200), (5, 400), (4, 300)], 3:[(1, 5), (2, 200), (4, 4)], 4:[(3, 4), (2, 300), (5,1)], 5:[(4,1), (2, 400)]}

def Prim(graph):
    V = len(graph)
    MST = []
    dist = [float('inf') for i in range(V)]
    dist[0] = 0
    prev = [None for i in range(V)]
    S = set()
    while len(S) != V:
        v = dist.index(min(dist))
        S.add(v)
        if prev[v] is not None:
            MST.append([prev[v], v])
        for u,w in graph[v]:
            if u not in S and dist[u] > w:
                prev[u] = v
                dist[u] = w
        dist[v] = float('inf')
    return MST                

print(Prim(graph))