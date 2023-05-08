# PURPOSE OF PROGRAM: WE ARE GIVEN AN EDGE LIST. WE WILL THEN WANT TO CONVERT IT INTO AN ADJACENCY LIST (GRAPH)

# AFTER CONVERTING TO ADJACENCY LIST, YOU CAN BEGIN TO DESIGN FUNCTIONS. MAKE SURE TO ACCOUNT FOR CYCLES!

# edges of a graph. we need to build the graph now with the given edges. this graph CONTAINS cycles. a -> b -> a -> b ...
edges = [
    ['a','b'],
    ['k','i'] ,
    ['m','k'],
    ['k','l'],
    ['o','n']
]


def buildGraph(edges): # building an adjaceny list.
    graph = {}

    for edge in edges:

        [a,b] = edge # get the pair of edges

        # if a node is not in the graph yet, make a key for it.
        if(a not in graph): graph[a] = []
        if(b not in graph): graph[b] = []
        
        # a is a neighor of b and b is a neighbor of a.
        graph[a].append(b)
        graph[b].append(a)

    return graph

graph = buildGraph(edges) 

print(" GRAPH: ")

print(graph) # OUR BUILT GRAPH WITH ALL ITS NEIGHBORS BUILT

print(" ")

visited = []

def dfsHas( graph,source, target, visited): # function that will check youre able to get to target starting from your node.

    if(source == target):
        return True
    
    if(source in visited): # checking if we already visited a node.
        return False
    
    visited.append(source) # if we dont return, that means we didnt visit this node, so add it for next time.

    for neighbor in graph[source]: # all neihbors of current source
        if dfsHas(graph,neighbor,target,visited) == True:
            return True
    
    return False



def dfs( graph, source, visited ): # function that will iterate through adjacency list.

    if(source in visited):
        return
    
    visited.append(source)

    print(source)

    for neighbor in graph[source]:
        dfs( graph,neighbor,visited )



#hasPath = dfsHas(graph,'a','k',visited)

#print(hasPath)

dfs(graph,'k',visited) # printing all neighbors of k

print(" ")
