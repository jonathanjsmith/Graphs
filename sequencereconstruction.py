"""
https://leetcode.com/problems/sequence-reconstruction/
You are given an integer array nums of length n where nums is a permutation of the integers in the range [1, n]. You are also given a 2D integer array sequences where sequences[i] is a subsequence of nums.
Check if nums is the shortest possible and the only supersequence. The shortest supersequence is a sequence with the shortest length and has all sequences[i] as subsequences. There could be multiple valid supersequences for the given array sequences.
    For example, for sequences = [[1,2],[1,3]], there are two shortest supersequences, [1,2,3] and [1,3,2].
    While for sequences = [[1,2],[1,3],[1,2,3]], the only shortest supersequence possible is [1,2,3]. [1,2,3,4] is a possible supersequence but not the shortest.
Return true if nums is the only shortest supersequence for sequences, or false otherwise.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""

import collections

def sequenceReconstruction(nums, sequences):
    
    n = len(nums)
    graph = collections.defaultdict(list)
    indegree = {x: 0 for x in range(1, n+1)}
    for s in sequences:
        for a, b in zip(s, s[1:]):
            if b not in graph[a]:
                graph[a].append(b)
                indegree[b] += 1
    
    # use topological sort to find shortest subsequence
    q = [i for i in indegree if indegree[i] == 0]
    l = []
    
    while q:
        # ensure that there is only one possible sequence
        if len(q) > 1:
            return False
        
        node = q.pop(0)
        l.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if not indegree[nei]:
                q.append(nei)
                
    return l == nums

"""
Time: O(V + E)
Space: O(V + E)
"""

nums = [1,2,3]
sequences = [[1,2],[1,3],[2,3]]
ans = sequenceReconstruction(nums, sequences)
print(ans)