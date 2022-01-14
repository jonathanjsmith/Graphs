"""
https://leetcode.com/problems/find-the-town-judge/
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
    1. The town judge trusts nobody.
    2. Everybody (except for the town judge) trusts the town judge.
    3. There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""

def findJudge(n, trust):
    # one array to find judge
    # judge should have exactly n-1 trusts
    trusted = (n+1)*[0]
    
    for a,b in trust:
        trusted[a] -= 1
        trusted[b] += 1
        
    for i in range(1, n+1):
        if trusted[i] == n-1:
            return i
        
    return -1

"""
Time: O(E)
Space: O(n) -- number of people
"""

input_1 = [[1,3],[2,3],[1,2]]
input_2 = [[1,3],[2,3],[3,1]]

ans1 = findJudge(3, input_1)
ans2 = findJudge(3, input_2)

print(ans1)
print(ans2)


