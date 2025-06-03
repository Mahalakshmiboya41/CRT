class GraphList:
    def __init__(self):
        self.graph={}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        
        #Add the node v if it's not in the graph
        if v not in self.graph:
            self.graph[v]=[]
        #Since it's an undirected graph, add each to the other's list
        self.graph[u].append(v)
        self.graph[v].append(u)
    def display(self):
        print("Adjancey List:")
        for i in self.graph:
            print(f"{i}-->{self.graph[i]}")
    def bfs(self,start):
        visited=set()
        queue=[start]
        while queue:
            vertex=queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex,end=' ')
                for i in self.graph[vertex]:
                     if i not in visited:
                          queue.append(i)
    def dfs(self,start,visited=None):
            if visited is None:
                visited=set()
            visited.add(start)
            print(start,end=' ')
            for i in self.graph[start]:
                if i not in visited:
                    self.dfs(i,visited)
#inserting nodes
g=GraphList()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,2)
g.add_edge(2,3)
g.add_edge(3,2)
g.add_edge(3,4)
g.add_edge(4,5)
#display the adjancey list
g.display()
g.bfs(4)
print("\nDFS:")
g.dfs(4)