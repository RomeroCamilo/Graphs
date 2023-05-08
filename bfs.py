#BFS IS RECOMMEND WHEN ANSWER IS CLOSE TO THE SOURCE

#using queue. first print all neighbors of a. after print neighbors of c (e) and b (d). repeat the process.
def bfs(graph,source):
    queue = [source]
    while(len(queue)>0):
        current = queue.pop(0) # removes the first element in the queue.
        #print(current)
        print('neightbors of ', current)
        for neighbor in graph[current]: # add every neighbor of current to the queue
            print(neighbor)
            queue.extend([neighbor]) # latest push goes to the back of the queue. its like a supreme shop line.


#using queue. first print all neighbors of a. after print neighbors of c (e) and b (d). repeat the process.
def bfsHas(graph,source,target):
    queue = [source]
    while(len(queue)>0):
        current = queue.pop(0) # removes the first element in the queue.
        print(current)
        # if we found the target
        if(current == target):
            print('True')
            return True
        for neighbor in graph[current]:
            queue.extend([neighbor]) # latest push goes to the back of the queue.
    return False

graph = {
    'a' : ['c','b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f':[]
}

print("--BFS--")
bfs(graph,'a')

print("--BFS has--")
bfsHas(graph,'a','b')