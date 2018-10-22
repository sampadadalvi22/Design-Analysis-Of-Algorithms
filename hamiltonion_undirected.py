from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, frm, to):
      
        self.graph[frm].append([to, False])

        if self.directed is False:
            self.graph[to].append([frm, False])
        else:
            self.graph[to] = self.graph[to]

    def findParent(self, sets, v):
        if sets[v] == -1:
            return v
        else:
            return self.findParent(sets, sets[v])

    def union(self, sets, x, y):
        x_set = self.findParent(sets, x)
        y_set = self.findParent(sets, y)
        sets[x_set] = y_set

    def isCyclic(self):
      
        sets = {i: -1 for i in self.graph}

        for v in self.graph:
            for e in self.graph[v]:
       
                if e[1] is True:
                    continue

             
                e[1] = True

                for i in self.graph[e[0]]:
                    if i[0] == v:
                        i[1] = True
                        break

                
                x = self.findParent(sets, v)
                y = self.findParent(sets, e[0])

                
                if x == y:
                    return True
               
                self.union(sets, x, y)

     
        return False


if __name__ == '__main__':
   
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)

    if graph.isCyclic():
        print("Cycle exists in the graph")
    else:
        print("No cycle in the graph")

