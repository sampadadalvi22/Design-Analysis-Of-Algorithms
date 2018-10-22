def floyd_warshall(graph):
    shortest_dist = []

   
    for i in graph:
        shortest_dist.append(i)

    
    V = len(graph) - 1

    
    for k in range(V+1):
        
        for i in range(V+1):
           
            for j in range(V+1):
               
                shortest_dist[i][j] = min(shortest_dist[i][j], shortest_dist[i][k] + shortest_dist[k][j])
    
    return shortest_dist

if __name__ == '__main__':
    INF = float('inf')
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF], 
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]]

    shortest_dist_matrix = floyd_warshall(graph)

    for i in shortest_dist_matrix:
        for j in i:
            if j != float('inf'):
                print(j, '\t', end='')
            else:
                print(j, end=' ')
print()
