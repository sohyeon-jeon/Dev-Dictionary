'''
https://leetcode.com/problems/reconstruct-itinerary/
'''
from collections import defaultdict

def findItinerary(tickets):
    routes=defaultdict(list)
    for a,b in tickets:
        routes[a].append(b)
        routes[a].sort()
    
    path=[]
    stack=['JFK']
    while stack:
        top=stack[-1]
        if top not in routes or len(routes[top])==0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop(0))
  
    print(path[::-1])
findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])


    
