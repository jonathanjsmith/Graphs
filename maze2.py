"""
https://leetcode.com/problems/the-maze-ii/
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.
The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).
You may assume that the borders of the maze are all walls (see examples).
"""

import heapq

def shortestDistance(maze, start, destination):
    
    m, n = len(maze), len(maze[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    seen = set()
    size = 0
    
    # use dijkstra's to calculate shortest path
    pq = [(0, *start)]
    while pq:
        dist, x, y = heapq.heappop(pq)
        if [x,y] == destination:
            return dist
        if (x, y) not in seen:
            seen.add((x,y))
            for d in dirs:
                nx, ny = x, y
                moves = 0
                while 0 <= nx+d[0] < m and 0 <= ny+d[1] < n and not maze[nx+d[0]][ny+d[1]]:
                    nx, ny = nx + d[0], ny + d[1]
                    moves += 1
                if moves: # conditional not required but saves time
                    heapq.heappush(pq, (dist + moves, nx, ny))
    return -1

"""
Time: O(mn*lg(mn))
Space: O(mn)
"""

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
ans = shortestDistance(maze, start, destination)
print(ans)
                
