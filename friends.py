"""
https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.
Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.
Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.
"""

class UnionFind:
    
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if self.rank[xroot] < self.rank[yroot]:
                self.root[xroot] = yroot
            elif self.rank[xroot] > self.rank[yroot]:
                self.root[yroot] = xroot
            else:
                self.root[yroot] = xroot
                self.rank[xroot] += 1
            return True
        return False
                
def friends(logs, n):
    
    # use union find to find when all nodes have the same group and return earliest timestamp
    uf = UnionFind(n)
    logs.sort(key=lambda x: x[0])
    groups = n
    
    for timestamp, x, y in logs:
        if uf.union(x, y):
            groups -= 1
        if groups == 1:
            return timestamp
        
    return -1

"""
Time: O(V + ElgE + E[alpha](V))
Space: O(V + E)
"""

logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
n = 6
ans = friends(logs, n)
print(ans)