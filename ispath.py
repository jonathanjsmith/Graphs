"""
https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
You want to determine if there is a valid path that exists from vertex start to vertex end.
Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.
"""

def isPath(n, edges, start, end):
    
    # create adjacency list of all edges
    graph = {}
    for u, v in edges:
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
            
    # BFS search to find paths from start node
    searched = set([start])
    q = [start]
    while q:
        v = q.pop(0)
        if v == end:
            return True
        
        for node in graph[v]:
            if node not in searched:
                searched.add(node)
                q.append(node)
                
    return False

"""
Time: O(V + E)
Space: O(V + E)
"""

n = 3
edges = [[0,1],[1,2],[2,0]]
start = 0
end = 2

ans = isPath(n, edges, start, end)
print(ans)

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
start = 0
end = 5

ans = isPath(n, edges, start, end)
print(ans)