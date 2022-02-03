"""
https://leetcode.com/problems/the-maze-iii/
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls onto the hole.
Given the m x n maze, the ball's position ball and the hole's position hole, where ball = [ballrow, ballcol] and hole = [holerow, holecol], return a string instructions of all the instructions that the ball should follow to drop in the hole with the shortest distance possible. If there are multiple valid instructions, return the lexicographically minimum one. If the ball can't drop in the hole, return "impossible".
If there is a way for the ball to drop in the hole, the answer instructions should contain the characters 'u' (i.e., up), 'd' (i.e., down), 'l' (i.e., left), and 'r' (i.e., right).
The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).
You may assume that the borders of the maze are all walls (see examples).
"""

import heapq

def shortestPath(maze, ball, hole):
    
    m, n = len(maze), len(maze[0])
    pq = [(0, "", *ball)]
    dirs = [(-1,0,"u"),(1,0,"d"),(0,-1,"l"),(0,1,"r")]
    shortest = float('inf')
    res = []
    
    # use breadth first search and heap to calculate shortest path to each vertex on path to goal
    while pq:
        dist, directions, x, y = heapq.heappop(pq)
        if [x, y] == hole and dist <= shortest:
            heapq.heappush(res, directions)
            shortest = dist
        maze[x][y] = 2
        for d in dirs:
            nx, ny = x, y
            moves = 0
            while 0 <= nx+d[0] < m and 0 <= ny+d[1] < n and maze[nx+d[0]][ny+d[1]] != 1:
                if [nx, ny] == hole:
                    break
                nx, ny, moves = nx + d[0], ny + d[1], moves + 1
            if maze[nx][ny] == 0:
                heapq.heappush(pq, (dist+moves, directions+d[2], nx, ny))
                
    return heapq.heappop(res) if res else "impossible"

"""
Time: O(n*lgn)
Space: O(n)
"""

maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
ball = [4,3]
hole = [0,1]

ans = shortestPath(maze, ball, hole)
print(ans)


    
