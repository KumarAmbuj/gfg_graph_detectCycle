from collections import defaultdict

class Pair:
    def __init__(self,u,l):
        self.u=u
        self.l=l

def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)


class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def isoddcycle(self):
        vis=[-1 for i in range(self.v)]
        queue=Queue()
        Enqueue(queue,Pair(0,0))

        while(Size(queue)):
            rem=Dequeue(queue)

            if vis[rem.u]!=-1:
                if vis[rem.u]!=rem.l:
                    return True
                continue

            vis[rem.u]=rem.l

            for v in self.graph[rem.u]:
                if vis[v]==-1:
                    Enqueue(queue,Pair(v,rem.l+1))
        return False


V = 4
G = [[0, 1, 0, 1],
     [1, 0, 1, 0],
     [0, 1, 0, 1],
     [1, 0, 1, 0]]
g=Graph(V)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(3,0)
g.addEdge(3,2)

if g.isoddcycle():
    print('odd length cycle found')
else:
    print('not found')

