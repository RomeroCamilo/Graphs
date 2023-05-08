# PURPOSE: DFS IMPLEMENTATION USING STACK OR RECURSION. HAS NOT ACCOUNTED FOR CYCLES. (add a set )


# depth first search. explore one direction as far as possible before moving directions
# RECOMMENED WHEN ANSWER IS FAR FROM THE SOURCE
def dfs(graph,source):
    stack = []
    stack.append(source)

    while(len(stack) > 0): # while the stack has a value
        # getting the current top of the stack and popping
        current = stack.pop()
        # printing value
        print(current)

        # now adding all nodes assoicated with the node we popped.
        for neighbor in graph[current]:
            stack.append(neighbor)


# a graph example for dfs utilzing a stack.
# a -> b -> d -> f -> NULL = completed a dfs. now will go to c and go as deep as it takes you.
graph = {
    'a' : ['c','b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f':[]
}

print("--DFS--")
dfs(graph,'a')
print(" ")

#another way for dfs a -> c -> e -> go back to b since c path finished and continue 
def dfs2(graph,source):
    print(source)

    for neighbor in graph[source]:
        dfs2(graph,neighbor)

print("--DFS--")
dfs2(graph,'a')


# dfs for checking if a node exists
def dfsHas(graph,source,target):
    print(source)
    if(source == target):
        print('Found')
        return True

    for neighbor in graph[source]:
        if dfsHas(graph,neighbor,target) == True: 
            return True
        
    return False # after iterating through a full path (for example a -> c -> e) and didnt find target in tht path

print(" ")
print("--DFS has Function--")

found = dfsHas(graph,'a','e') # calling function to check if target is found.




