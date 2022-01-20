"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/?currentPage=1&orderBy=most_votes&query=
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
"""

# Bellman Ford
def cheapestPrice(n, flights, src, dst, k):
    
    costs = n*[float('inf')]
    costs[src] = 0
    
    for _ in range(k+1):
        temp = costs.copy()
        for u, v, price in flights:
            temp[v] = min(temp[v], costs[u] + price)
        costs = temp
        
    return -1 if costs[dst] == float('inf') else costs[dst]

"""
Time: O(V*E)
Space: O(V)
"""

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
ans = cheapestPrice(n, flights, src, dst, k)
print(ans)

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
ans = cheapestPrice(n, flights, src, dst, k)
print(ans)