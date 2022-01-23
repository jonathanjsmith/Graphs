"""
https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

import collections

def canFinish(numCourses, prerequisites):
    
    # create adjacency lsit of all edges in prerequisites
    graph = collections.defaultdict(list)
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[a].append(b)
        indegree[b] += 1
    
    # find a cycle in the graph using topological sort
    s = [i for i in range(numCourses) if indegree[i] == 0]
    for i in s:
        for j in graph[i]:
            indegree[j] -= 1
            if not indegree[j]:
                s.append(j)
                
    return len(s) == numCourses

"""
Time: O(V + E)
Space: O(V + E)
"""

numCourses = 2
prerequisites = [[1,0]]
ans = canFinish(numCourses, prerequisites)
print(ans)

numCourses = 2
prerequisites = [[1,0],[0,1]]
ans = canFinish(numCourses, prerequisites)
print(ans)


