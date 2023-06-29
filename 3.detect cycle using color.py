from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,u,vis):

        vis[u]='g'

        for v in self.graph[u]:
            if vis[v]=='w':
                if self.dfs(v,vis):
                    return True
            elif vis[v]=='g':
                return True
        vis[u]='b'
        return False

    def iscycle(self):

        vis=['w' for i in range(self.v)]

        for i in range(self.v):
            if vis[i]=='w':
                if self.dfs(i,vis):
                    print('cycle found')
                    break
        else:
            print('not found')

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.iscycle()