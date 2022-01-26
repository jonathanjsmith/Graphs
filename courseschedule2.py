"""
https://leetcode.com/problems/course-schedule-ii/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""

import collections

def order(numCourses, prerequisites):
    
    # create adj list of prerequisites
    graph = collections.defaultdict(list)
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[a].append(b)
        indegree[b] += 1
    
    # use topological sort
    order = []
    q = [i for i in range(numCourses) if indegree[i] == 0]
    while q:
        node = q.pop(0)
        order.insert(0, node)
        for adj in graph[node]:
            indegree[adj] -= 1
            if not indegree[adj]:
                q.append(adj)
    
    return order if len(order) == numCourses else []

"""
Time: O(V + E)
Space: O(V + E)
"""

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
ans = order(numCourses, prerequisites)
print(ans)