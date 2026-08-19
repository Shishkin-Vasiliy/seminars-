class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(self.n)]

    def find(self, v):
        if self.parent[v] == v:
            return v
        return self.find(self.parent[v]) 
    
    def ask(self, u, v):
        urep = self.find(u)
        vrep = self.find(v)
        if urep == vrep:
            return 'YES'
        else:
            return 'NO'

    def Union(self, u, v):
        urep = self.find(u)
        vrep = self.find(v)
        self.parent[vrep] = urep

edges = [(0, 1, 2), (0, 2, 3), (1, 2 , 100), (1, 3, 5), (2, 3, 200), (2, 5, 400), (2, 4, 300), (5, 4, 1), (3, 4, 4)]

def Kruskal(V, edges):
    MST = []
    sorted_edges = sorted(edges, key = lambda x: x[2])
    dsu = DSU(V)
    for u, v, s in sorted_edges:
        if dsu.find(v) != dsu.find(u):
            dsu.Union(u, v)
            MST.append([u, v])
    return MST

print(Kruskal(len(edges) + 1, edges)) 