# PURPOSE OF THIS PROGRAM: THE PURPOSE OF THIS PROGRAM IS TO GET ALL THE COMPONENTS / ISLANDS BASED ON EDGES.

#ALGORITHM: FIRST BUILD THE GRAPH/ADJACENCY LIST. 

# HAVE A SET TO PREVENT CYCLES AND KEEP TRACK OF WHAT NODES YOU VISITED ALREADY

n = 5 # amount of nodes 

edges = [[0,1],[1,2],[3,4]]

graph = {}

def buildGraph(edges): # build our graph/adjacency list based on the edges provided.

    for edge in edges:

        [a,b] = edge

        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []

        graph[a].append(b)
        graph[b].append(a)


buildGraph(edges)


visited = set() # will increment count if we reached a visited node already. that means the end of a component

def dfs(graph,node):

    if(node in visited): # MARK FOR DUPLICATE / CYCLES PREVENTION
        return False

    visited.add(node)

    for neighbor in graph[node]: # exploring each neighbor of the current node.
        dfs(graph,neighbor)

    return True # FINISHED EXPLORING AN ENTIRE COMPONENT AS FAR AS POSSIBLE AS WE RAN OUT OF NODES in the for loop.

def getCount(graph): # PARENT FUNCTION FOR DFS WHICH WILL TRAVERSE A COMPONENT.

    count = 0

    for node in graph: # traverse a node that is located in a component
        if dfs(graph,node) == True: 
            count+=1
    
    return count

count = getCount(graph)

if(len(visited) != n): # if our set does not match the parameter n, that means there were nodes not included in the edge list.
    count+= n - len(visited)