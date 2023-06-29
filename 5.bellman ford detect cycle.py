def bellmanford(v,edges,src):
    dist=[999 for i in range(v)]

    dist[src]=0

    for i in range(v-1):

        for edge in edges:
            u=edge[0]
            v=edge[1]
            w=edge[2]

            if dist[u]!=999 and dist[v]>dist[u]+w:
                dist[v]=dist[u]+w

    for edge in edges:
        u=edge[0]
        v=edge[1]
        w=edge[2]

        if dist[u]!=999 and dist[v]>dist[u]+w:
            return True
    return False


V = 5;  # Number of vertices in graph
E = 8;  # Number of edges in graph
edges=[[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]

if bellmanford(V,edges,0):
    print('cycle found')
else:
    print('not found')