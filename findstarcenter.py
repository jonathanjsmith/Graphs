"""
https://leetcode.com/problems/find-center-of-star-graph/
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
"""

def center(edges):
    # find a similar vertex in first two tuples
    x, y = edges[0][0], edges[0][1]
    
    if x in edges[1]:
        return x
    return y

"""
Time: O(1)
Space: O(1)
"""

input_1 = [[1,2],[2,3],[4,2]]

ans = center(input_1)
print(ans)