"""
https://leetcode.com/problems/path-with-maximum-probability/
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
"""

import collections
import heapq

def maxProb(n, edges, succProb, start, end):
    
    # create adj list with weights
    graph = collections.defaultdict(dict)
    for i, (a, b) in enumerate(edges):
        graph[a][b] = graph[b][a] = succProb[i]
        
    # use dijkstras
    pq = [(-1, start)]
    dist = {}
    
    while pq:
        d, node = heapq.heappop(pq)
        if node not in dist:
            dist[node] = -d
            for nei in graph[node]:
                heapq.heappush(pq, (d * graph[node][nei], nei))
                
    return dist[end] if end in dist else 0

"""
Time: O(E * lgV)
Space: O(V + E)
"""

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

ans = maxProb(n, edges, succProb, start, end)
print(ans)
