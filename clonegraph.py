"""
https://leetcode.com/problems/clone-graph/
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""

class Node:
    
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors
        
def clone(node):
    
    if not node:
        return None
    
    s = [node]
    seen = {}
    while s:
        x = s.pop()
        if x not in seen:
            seen[x] = Node(x.val)
        for nei in x.neighbors:
            if nei not in seen:
                seen[nei] = Node(nei.val)
                s.append(nei)
            seen[x].neighbors.append(seen[nei])
            
    return seen[node]

"""
Time: O(V + E)
Space: O(V)
"""

x1 = Node(1)
x2 = Node(2)
x3 = Node(3)
x4 = Node(4)
x1.neighbors = [x2, x4]
x2.neighbors = [x1, x3]
x3.neighbors = [x2, x4]
x4.neighbors = [x1, x3]
ans = clone(x1)
print([a.val for a in ans.neighbors])