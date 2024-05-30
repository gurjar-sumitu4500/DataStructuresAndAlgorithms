class Graph:
    def __init__(self):
        self.adj_list = {}

    def printGraph(self):
        for vertex in self.adj_list:
            print(vertex, ' ', self.adj_list[vertex])

    def addVertext(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def addEdge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def removeEdge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def removeVertex(self, vertex):
        if vertex in self.adj_list.keys():
            for otherVertex in self.adj_list[vertex]:
                self.adj_list[otherVertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

# myGraph = Graph()
# myGraph.addVertext('A')
# myGraph.addVertext('B')
# myGraph.addVertext('C')
# myGraph.addVertext('D')
# myGraph.addEdge('A', 'B')
# myGraph.addEdge('B', 'C')
# myGraph.addEdge('C', 'A')
# myGraph.addEdge('A', 'D')
# myGraph.addEdge('B', 'D')
# myGraph.addEdge('C', 'D')
# # myGraph.removeEdge('A', 'D')
# myGraph.printGraph()
# myGraph.removeVertex('D')
# myGraph.printGraph()