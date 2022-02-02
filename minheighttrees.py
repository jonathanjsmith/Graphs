"""
https://leetcode.com/problems/minimum-height-trees/solution/
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""

import collections

def minHeightTrees(n, edges):
    
    graph = collections.defaultdict(list)
    indegree = [0] * n
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        indegree[a] += 1
        indegree[b] += 1
    
    # use topological sort and find length of longest physical path in graph
    l = []
    s = [(0, i) for i in range(n) if indegree[i] == 1]
    
    while s:
        d, node = s.pop(0)
        l.insert(0, (d, node))
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 1:
                s.append((d + 1, nei))
    
    return [node for d, node in l if d == l[0][0]] if n != 1 else [0]

"""
Time: O(V + E)
Space: O(V + E)
"""

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
ans = minHeightTrees(n, edges)
print(ans)