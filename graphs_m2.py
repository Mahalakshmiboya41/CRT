class GraphMatrix:
    def __init__(self,size=None,adj_matrix=None):
        if adj_matrix is not None:
            self.adj_matrix=adj_matrix
            self.size=len(adj_matrix)
        else:
            self.size=size
            self.adj_matrix=[[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self,u,v):
        if u<self.size and v<self.size:
           self.adj_matrix[u][v]=1
           self.adj_matrix[v][u]=1  

    def display(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))
adj_matrix=[
    [0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,1,0,0,1,0,0],
    [0,1,0,0,1,0,0],
    [0,0,1,1,0,1,0],
    [0,0,0,0,1,0,1],
    [0,0,0,0,0,1,1]
]

g=GraphMatrix(adj_matrix=adj_matrix)
g.display()