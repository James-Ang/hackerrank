# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:58:51 2021

@author: James Ang
"""

def bfs(n, m, edges, s):    # Solution 1
    from collections import deque

    # Build graph
    graph = {}
    for num in range(1, n+1):
        graph[num] = set()
    for l, r in edges:
        graph[l].add(r)
        graph[r].add(l)
    
    reached = {}
    # Explore graph once
    frontier = deque([(s, 0)])
    seen = {s}

    while frontier:
        curr_node, curr_cost = frontier.popleft()
        for nbour in graph[curr_node]:
            if nbour not in seen:
                seen.add(nbour)
                reached[nbour] = curr_cost+6
                frontier.append((nbour, curr_cost+6))

    result = []
    for node in range(1, n+1):
        if s != node:
            result.append(reached.get(node, -1))
    
    return result

def bfs1(n, m, edges, s):   # solution 2
    queue = [s]
    visited = [s]
    dists = {s: 0}
    adjList = {}
    
    for i in range(len(edges)):
        
        edge = edges[i]
        x = edge[0]
        y = edge[1]
        
        if x in adjList:
            if y not in adjList[x]:
                adjList[x].append(y)
        else:
            adjList[x] = [y]
            
        if y in adjList:
            if x not in adjList[y]:
                adjList[y].append(x)
        else:
            adjList[y] = [x]
            
    while len(queue) > 0:
        
        node = queue.pop(0)
        if node in adjList:
            neighbors = adjList[node]
            for j in range(len(neighbors)):
                if neighbors[j] not in visited:
                    dists[neighbors[j]] = dists[node] + 6
                    visited.append(neighbors[j])
                    queue.append(neighbors[j])
                    
    res = []
    
    for i in range(1,n+1):
        
        if i not in dists:
            res.append(-1)
        elif dists[i] != 0:
            res.append(dists[i])
    return res

if __name__ == '__main__':
    
    n = 4
    m = 2
    edges = [[1,2],[1,3]]
    s = 1
    
    
    result = bfs1(n, m, edges, s)
    print(result)