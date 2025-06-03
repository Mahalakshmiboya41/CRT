class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices=num_vertices
        self.matrix=[[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self,u,v):
        self.matrix[u-1][v-1]=1
        self.matrix[v-1][u-1]=1  

    def display(self):
        print("Adjacency Matrix:")
        for row in self.matrix:
            print(" ".join(map(str, row)))

g=GraphMatrix(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.display()