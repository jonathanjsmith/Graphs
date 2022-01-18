"""
https://leetcode.com/problems/all-paths-from-source-to-target/
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""

def allPaths(graph):
    
    # search all paths using DFS
    def dfs(v):
        path.append(v)
        
        if v == len(graph)-1:
            paths.append(path.copy())
            
        for nei in graph[v]:
            dfs(nei)
            path.pop()
            
    path = []
    paths = []
    dfs(0)
    
    return paths

"""
O(2^V * V)
O(2^V * V)
"""

graph = [[1,2],[3],[3],[]]
ans = allPaths(graph)
print(ans)

graph = [[4,3,1],[3,2,4],[3],[4],[]]
ans = allPaths(graph)
print(ans)