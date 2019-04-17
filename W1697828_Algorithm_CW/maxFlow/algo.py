import copy
import networkx as nx
import matplotlib.pyplot as plt
import random

def bfs(resGraph, s, t, pathMap):
    visitedList = [s]  # list to hold the visited elements
    queueList = [s]  # Queue to store the values to do breadth first search

    while queueList:
        u = queueList.pop(0)
        for i in range(len(resGraph)):
            if resGraph[u][i] > 0 and (i not in visitedList):  # check whether node is already visited OR not,
                queueList.append(i)
                pathMap[i] = u
                visitedList.append(i)

    print("VisitedSet : ", visitedList)
    print("queueList : ", queueList)
    print("pathMap Dictionary : ", pathMap)

    return True if t in visitedList else False   # returns TRUE if Sink(destination Node) is visited.


def draw_Graph(G,graph,edgeLabel):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] > 0:
                G.add_path([i, j])  # Drawing Graph  adding path
                edgeLabel.update({(i, j): graph[i][j]})


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

graph2 = [[0, 5, 7, 0],
          [0, 0, 0, 12],
          [0, 3, 0, 4],
          [0, 0, 0, 0]]

graph3 = [[0, 10, 5, 15, 0, 0, 0, 0],
          [0, 0, 4, 0, 9, 15, 0, 0],
          [0, 0, 0, 4, 0, 8, 0, 0],
          [0, 0, 0, 0, 0, 0, 16, 0],
          [0, 0, 0, 0, 0, 15, 0, 10],
          [0, 0, 0, 0, 0, 0, 15, 10],
          [0, 0, 6, 0, 0, 0, 0, 10],
          [0, 0, 0, 0, 0, 0, 0, 0]]
print("Enter 1 to generate Random nodes\nEnter 2 to Input no of nodes ")
num = int(input("Enter 1 or 2 :"))
if num == 1:
    nodeRange = random.randint(6, 10)
else:
    nodeRange = int(input("Number of nodes : "))
print("Number of nodes : ", nodeRange)
random.randint(5, 21)
graph = [[0] * nodeRange for _ in range(nodeRange)]
for i in range(len(graph)):
    for j in range(len(graph)):
        if i != j:
            graph[i][j] = random.randint(5, 20)
        if i == len(graph)-1:
            graph[i][j] = 0
        if j == 0:
            graph[i][j] = 0

pathMap = {}
s = 0
t = len(graph) - 1  # destination of the graph.. end point.
maxFlow = 0
lastResGraph = [[]]
G = nx.DiGraph()

while bfs(graph, s, t, pathMap):
    print("path map getting...", pathMap.get(t))
    y = t
    flowPath = [y]
    x = True
    while x:
        y = pathMap.get(y)
        flowPath.append(y)
        if y == 0:
            x = False
    size = len(flowPath) - 1
    print("Flow Path LIST :", flowPath)
    # for i in range(len(flowPath) - 1):
    #     G.add_edge(flowPath[i], flowPath[i+1], color='r')

    residualCap = 25
    res = 0
    nest = True
    for i in graph:
        for j in i:
            while nest:
                if size != 0:
                    res = graph[flowPath[size]][flowPath[size-1]]
                    # print("residual capacity : ", res)
                    if res < residualCap:
                        residualCap = res
                        # print("residual capacity IN IF : ", res)
                size -= 1
                if size == 0:
                    nest = False
    # print("SIZE : ", size)
    print("residual capacity for each Time : ", residualCap)
    maxFlow += residualCap
    size = len(flowPath) - 1
    # print("NOW size :", size)
    flowPath = flowPath[::-1]  # Reversing the Flow List
    # print("NOW flow path :", flowPath)

    while size != 0:
        u = size - 1
        graph[flowPath[u]][flowPath[size]] -= residualCap   # generating new Residual Graph
        graph[flowPath[size]][flowPath[u]] += residualCap
        # graph[u][size] += residualCap
        size -= 1
        # print('while Size:', size)



    print("MAX FLOW : ", maxFlow)
    graph = copy.deepcopy(graph)  # for repetition..
    for i in graph:  # printing Residual Graph... For each time
        for j in i:
            print(j, end=' ')
        print()
    edgeLabel = {}
    draw_Graph(G, graph, edgeLabel)
    # for i in range(len(flowPath) - 1):
    #     G.add_edge(flowPath[i], flowPath[i+1], color='r')
    pos = nx.spring_layout(G)
    # edge_color = [G[u][v]['color'] for u, v in G.edges()]
    plt.title('Residual Graph')
    nx.draw(G, pos=pos, edges=G.edges(), with_labels=True, labels={node: node for node in G.nodes()})
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabel, font_color='red')
    plt.draw()
    plt.show()


print("Final Maximum Flow : ", maxFlow)
print("******************************")



