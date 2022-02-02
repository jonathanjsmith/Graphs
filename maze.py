"""
https://leetcode.com/problems/the-maze/
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.
You may assume that the borders of the maze are all walls (see examples).
"""

def hasPath(maze, start, destination):
    
    m, n = len(maze), len(maze[0])
    s = [start]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # use stack to implement DFS
    # find and mark all possible destinations
    while s:
        x, y = s.pop()
        
        if [x,y] == destination:
            return True
        
        maze[x][y] = 2
        for d in dirs:
            nx, ny = x, y
            while 0 <= nx + d[0] < m and 0 <= ny + d[1] < n and maze[nx+d[0]][ny+d[1]] != 1:
                nx, ny = nx + d[0], ny + d[1]
            if maze[nx][ny] == 0:
                s.append([nx,ny])
                
    return False

"""
Time: O(mn)
Space: O(mn)
"""

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
ans = hasPath(maze, start, destination)
print(ans)