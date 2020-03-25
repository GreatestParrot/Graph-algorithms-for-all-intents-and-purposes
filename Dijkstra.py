# Need Start vertex number and Graph
# Graph structure:
# Grap = list of vetrexes
# Graph[vertex]=list of neighbour_vertexes
# neighbour_ver = list:
#     neighbour_ver[0] - number of vertex
#     neighbour_ver[1] - distanse frome origin_vertex to neighbour`
# Also required inf - "number that could be thought about as infinity"

def Dijkstra(Graph, start, inf):

    dist = list()
    prev = list()
    vertex = set()
    for i in range(len(Graph)):
        dist.append(inf)
        prev.append(-1)
        if len(Graph[i])!=0:
            vertex.add(i)

    dist[start]=0

    while (len(vertex)>0):

        u = vertex.pop()
        vertex.add(u)

    

        for i in vertex:
            if dist[i]<dist[u]:
                u=i
    
        vertex.remove(u)

        # print(str(u)+ "  " + str(dist[u]) + "  "+ str(Graph[u]))

        for neighbour_ver in Graph[u]:
            alt = dist[u]+neighbour_ver[1]
            if alt < dist[neighbour_ver[0]]:
                dist[neighbour_ver[0]] = alt
                prev[neighbour_ver[0]] = u

#return dist - list of distances from start vertex and prev - list of vertexes with "previous vertex in path"
    return dist, prev

