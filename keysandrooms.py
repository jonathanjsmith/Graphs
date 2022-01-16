"""
https://leetcode.com/problems/keys-and-rooms/
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
"""

def canVisitAllRooms(rooms):
    # visit all rooms using DFS
    def dfs(v):
        visited[v] = 1
        for key in rooms[v]:
            if not visited[key]:
                dfs(key)
        
    visited = len(rooms)*[0]
    dfs(0)
    
    return 0 not in visited

"""
Time: O(V + E)
Space: O(V)
"""

rooms = [[1],[2],[3],[]]
ans = canVisitAllRooms(rooms)
print(ans)

rooms = [[1,3],[3,0,1],[2],[0]]
ans = canVisitAllRooms(rooms)
print(ans)
