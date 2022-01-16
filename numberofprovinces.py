"""
https://leetcode.com/problems/number-of-provinces/
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.
"""

def countProvinces(connections):
    # DFS to visit all neighbors, count all provinces
    def dfs(v):
        for city,neighbor in enumerate(connections[v]):
            if neighbor and not visited[city]:
                visited[city] = 1
                dfs(city)
                
    visited = len(connections)*[0]
    provinces = 0
    for city in range(len(connections)):
        if not visited[city]:
            dfs(city)
            provinces += 1
            
    return provinces

"""
Time: O(V^2)
Space: O(V)
"""

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
ans = countProvinces(isConnected)
print(ans)

isConnected = [[1,0,0],[0,1,0],[0,0,1]]
ans = countProvinces(isConnected)
print(ans)
                
    