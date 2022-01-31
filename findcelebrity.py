"""
https://leetcode.com/problems/find-the-celebrity/
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) that tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.
Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.
"""

def knows(a, b):
    return graph[a][b]

def findCelebrity(n):
    
    # find a candidate by looking for a person that does not know anyone
    candidate = 0
    for i in range(n):
        if knows(candidate, i):
            candidate = i
    
    # check if the candidate is a celebrity
    for i in range(n):
        if candidate == i:
            continue
        
        if not knows(i, candidate) or knows(candidate, i):
            return -1
        
    return candidate

"""
Time: O(n)
Space: O(1)
"""

n = 4
graph = [[1,1,1,1],[0,1,1,0],[0,0,1,0],[1,0,1,1]]
ans = findCelebrity(n)
print(ans)
