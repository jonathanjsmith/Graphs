"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""

def longestIncreasingPath(matrix):
    
    # calculate the indegree of each node
    m, n = len(matrix), len(matrix[0])
    indegree = [[0 for _ in range(n)] for _ in range(m)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for x in range(m):
        for y in range(n):
            for d in dirs:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] < matrix[x][y]:
                    indegree[x][y] += 1
    

    # use topological sort to count the longest chain of nodes
    q = [(x, y) for x in range(m) for y in range(n) if not indegree[x][y]]
    longest_path = 0
    while q:
        for _ in range(len(q)):
            x, y = q.pop(0)
            for d in dirs:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    indegree[nx][ny] -= 1
                    if not indegree[nx][ny]:
                        q.append((nx, ny))
        longest_path += 1
        
    return longest_path
    
"""
Time: O(m * n)
Space: O(m * n)
"""

matrix = [[9,9,4],[6,6,8],[2,1,1]]
ans = longestIncreasingPath(matrix)
print(ans)