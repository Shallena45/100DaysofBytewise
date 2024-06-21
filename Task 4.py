"""QuickSort Algorithm
Write a program to implement the QuickSort algorithm.
Expected Output: If the input array is [3, 6, 8, 10, 1, 2, 1], the output should be [1, 1, 2, 3, 6, 8, 10].
"""
print(" QuickSort Algorithm")
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = []
    right = []
        
    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right) 

array = [3, 6, 8, 10, 1, 2, 1]
sorted = quick_sort(array)
print("Sorted array:", sorted)   
print("\n")

"""Knapsack Problem
Write a program to solve the 0/1 Knapsack Problem using dynamic programming.
Expected Output: If the input weights are [1, 3, 4, 5], values are [1, 4, 5, 7], and the maximum capacity is 7, the output should be 9.
"""
print(" Knapsack Problem")
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

max_value = knapsack(weights, values, capacity)
print("Maximum value in Knapsack:", max_value)
print("\n")

"""Graph Traversal (BFS and DFS)
Implement Breadth-First Search (BFS) and Depth-First Search (DFS) for graph traversal.
Expected Output: If the input graph is {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}, the BFS starting from node 2 should return [2, 0, 3, 1], and the DFS starting from node 2 should return [2, 0, 1, 3].
"""
print(" Graph Traversal")
def bfs(graph, start):
    visited = set()
    queue = [start]
    bfs_result = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            bfs_result.append(node)
            queue.extend(graph[node])

    return bfs_result

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_result.extend(dfs(graph, neighbor, visited))
    
    return dfs_result

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

start_node = 2

bfs_result = bfs(graph, start_node)
dfs_result = dfs(graph, start_node)

print(f"BFS starting from node {start_node}: {bfs_result}")
print(f"DFS starting from node {start_node}: {dfs_result}")

print("\n")

"""Dijkstra's Algorithm
Write a program to implement Dijkstra's algorithm for finding the shortest path in a graph.
Expected Output: If the input graph is {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}} and the starting node is A, the output should be {'A': 0, 'B': 1, 'C': 3, 'D': 4}.
"""
print(" Dijkstra's Algorithm")
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    
    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)
        
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
print("\n")

"""Longest Common Subsequence (LCS)
Write a program to find the longest common subsequence between two strings.
Expected Output: If the input strings are AGGTAB and GXTXAYB, the output should be GTAB.
"""
print(" Logest Common Subsequence")
def lcs(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    i = m
    j = n
    lcs_str = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_str))

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
print("The Longest Common Subsequence is", lcs(X, Y))
