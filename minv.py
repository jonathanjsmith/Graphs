"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.
Notice that you can return the vertices in any order.
"""

def minVertices(n, edges):
    # find number of edges with no in-degree
    unreachable = []
    
    indegree = n*[0]
    for u,v in edges:
        indegree[v] = 1
        
    for v,degree in enumerate(indegree):
        if not degree:
            unreachable.append(v)
    
    return unreachable

"""
Time: O(E)
Space: O(V)
"""

n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]

ans = minVertices(n, edges)
print(ans)

n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]

ans = minVertices(n, edges)
print(ans)