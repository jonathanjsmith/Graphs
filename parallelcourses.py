"""
https://leetcode.com/problems/parallel-courses/
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.
In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.
Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.
"""

import collections

def minimumSemesters(n, relations):
    
    # create adj list
    graph = collections.defaultdict(list)
    indegree = [1] + [0] * n
    for a, b in relations:
        graph[a].append(b)
        indegree[b] += 1
    
    l = []
    q = [(1, i) for i in range(n+1) if indegree[i] == 0]
    max_dist = 0
    
    while q:
        d, node = q.pop(0)
        max_dist = max(max_dist, d)
        l.insert(0, node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if not indegree[nei]:
                q.append((d+1, nei))
                
    return max_dist if len(l) == n else -1

"""
Time: O(V + E)
Space: O(V + E)
"""

n = 3
relations = [[1,3],[2,3]]

ans = minimumSemesters(n, relations)
print(ans)
    