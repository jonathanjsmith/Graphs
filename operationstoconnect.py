"""
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.
You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.
Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
"""

import collections

def operations(n, connections):
    
    # network needs n - 1 connections to reach all computers
    if len(connections)+1 < n:
        return -1
    
    # create adj list of all connections
    graph = collections.defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
        
    # count number of connected components
    seen = [0] * n
    def dfs(i):
        if seen[i]:
            return 0
        seen[i] = 1
        for adj in graph[i]:
            dfs(adj)
        return 1
    
    return sum(dfs(i) for i in range(n)) - 1

"""
Time: O(V + E)
Space: O(V + E)
"""

n = 4
connections = [[0,1],[0,2],[1,2]]
ans = operations(n, connections)
print(ans)