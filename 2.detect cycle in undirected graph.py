from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,vis,par):

        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                if self.dfs(v,vis,u):
                    return True
            elif par!=v:
                return True

    def iscycle(self):

        vis=[False for i in range(self.v)]

        for u in range(self.v):
            if vis[u]==False:
                if self.dfs(u,vis,-1):
                    print('cycle found')
                    break
        else:
            print('not found')


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.iscycle()