from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,u,vis,recstack):

        vis[u]=True
        recstack[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                if self.dfs(v,vis,recstack):
                    return True
            elif recstack[v]==True:
                return True
        recstack[u]=False
        return False

    def iscycle(self):

        vis=[False for i in range(self.v)]
        recstack=[False for i in range(self.v)]

        for i in range(self.v):
            if vis[i]==False:
                if self.dfs(i,vis,recstack):
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
