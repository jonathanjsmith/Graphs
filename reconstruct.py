"""
https://leetcode.com/problems/reconstruct-itinerary/
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
"""
import collections

def itinerary(tickets):
    
    targets = collections.defaultdict(list)
    for source, dest in sorted(tickets)[::-1]:
        targets[source].append(dest)
    route = []
    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)
    visit("JFK")
    return route[::-1]

"""
Time: O(Elg(E))
Space: O(E)
"""

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
ans = itinerary(tickets)
print(ans)

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
ans = itinerary(tickets)
print(ans)