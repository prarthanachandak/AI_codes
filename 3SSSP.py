def sssP(graph,node,d,distance,par):
    distance[node]=d
    for child in graph[node]:
        if child !=par:
            sssP(graph,child,distance[node]+1,distance,node)

edges = [['A','B'],['A','C'],['C','E'],['C','F'],['B','D'],['D','G'],['G','H'],['G','I']]
nodes = ['A','B','C','D','E','F','G','H','I']

graph = { }
distance = { }

for key in nodes:
    graph[key] = []
    distance[key] = None
for (u,v) in edges:
    graph[u].append(v)
    graph[v].append(u)

start = 'A'
distance[start] = 0
sssP(graph,start,0,distance,-1)
for key,value in distance.items():
    print(key,value)