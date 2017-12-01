from py2neo import Graph
graph = Graph("http://localhost:7474/db/data/")


def TopoSort(program_name):
    adjPair = graph.data("MATCH (m)-[:HasPrerequisite]->(n) \
        WHERE (m)-[:UnderProgram]->({name: 'Accounting (BS)'}) \
        and (n)-[:UnderProgram]->({name: 'Accounting (BS)'}) \
        RETURN m.id, n.id")
    # if you take m, must first take n
    courselist = []
    for i in adjPair:
        courselist += [i["m.id"], i["n.id"]]
    courselist = list(set(courselist))
    adjList = {i:[] for i in courselist}
    indegree = {i: 0 for i in courselist}
    # for post in adjList:
    #     for edge in adjPair:
    #         if edge["m.id"] == post:
    #             adjList[post].append(edge["n.id"])
    for edge in adjPair:
        adjList[edge["m.id"]].append(edge["n.id"])
        indegree[edge["n.id"]] += 1
    # startnodes = [i for i in adjList if len(adjList[i]) == 0]
    import queue
    queue = queue.Queue(maxsize = len(courselist))
    for i in adjList:
        if len(adjList[i]) == 0:
            queue.put(i)
    order = []
    while not queue.empty():
        node = queue.get()
        order.append(node)
        for x in adjList[node]:
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.put(x)

    return order


#Python program to print topological sorting of a DAG
from collections import defaultdict
 
#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self,v,visited,stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Push current vertex to stack which stores result
        stack.insert(0,v)
 
    # The function to do Topological Sort. It uses recursive 
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Print contents of stack
        print stack


def tp(self, v, visited, stack):
    visited[v] = True
    for i in adjList[courselist[v]]:
        if visited[v] == False:
            self.tp(i, visited, stack)
    stack.insert(0, v)

def ts(self):
    visited = [False] * len(courselist)
    stack = []
    for i in range(len(courselist)):
        if visited[i] == False:
            self.tp(i, visited, stack)


