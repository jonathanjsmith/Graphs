""""
https://leetcode.com/problems/network-delay-time/
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
"""

import collections
import heapq

def networkDelay(times, n, k):
    
    # create adj matrix
    graph = collections.defaultdict(dict)
    for u, v, w in times:
        graph[u][v] = w
        
    # create min priority queue to implement dijkstra's
    pq = [(0, k)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        if node not in dist:
            dist[node] = d
            for adj in graph[node]:
                heapq.heappush(pq, (d + graph[node][adj], adj))
    
    return max(dist.values()) if len(dist) == n else -1

"""
Time: O(E lgE)
Space: O(V + E)
"""

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
ans = networkDelay(times, n, k)
print(ans)

times = [[1,2,1]]
n = 2
k = 1
ans = networkDelay(times, n, k)
print(ans)

times = [[1,2,1]]
n = 2
k = 2
ans = networkDelay(times, n, k)
print(ans)