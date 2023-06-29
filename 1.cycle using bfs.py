def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,u,vis):
        queue=Queue()
        Enqueue(queue,u)

        while(Size(queue)):
            rem=Dequeue(queue)

            if vis[rem]==True:
                return True

            vis[rem]=True

            for v in self.graph[u]:
                if vis[v]==False:
                    Enqueue(queue,v)

    def iscycle(self):

        vis=[False for i in range(self.v)]

        for i in range(self.v):
            if vis[i]==False:
                if self.bfs(i,vis):
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
