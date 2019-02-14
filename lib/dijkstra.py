"""
ダイクストラ法
----------
input
    graph: 隣接リスト (list)
    start: 開始ノード番号
    INF  : distの最大値

output
    dist : startから各ノードへの距離 (list)
    
"""

from heapq import heappush, heappop

def dijkstra(graph: list, start, INF=float('inf')) -> list:
    n = len(graph)
    dist = [INF]*n
    visited = [False]*n
    
    dist[start] = 0
    que = [(0, start)]
    
    while que:
        cost, cur = heappop(que)
        
        if visited[cur]:
            continue
        
        visited[cur] = True
        
        for nextnode, edgecost in graph[cur]:
            nextcost = cost + edgecost
            if nextcost < dist[nextnode]:
                dist[nextnode] = nextcost
                heappush(que, (nextcost, nextnode))
      
    return dist


### Sample ###
#
# graph = [[(1, 1), (2, 4)],
#          [(2, 2), (3, 5)],
#          [(3, 1)],
#          []]
# start = 0
# INF = 1<<62
#   
# dist = dijkstra(graph, start, INF)
#   => dist = [0,1,3,4]

### Verify ###
#
# AOJ GRL_1_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A