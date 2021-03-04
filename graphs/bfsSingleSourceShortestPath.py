'''

    BFS is Breadth first search and is just like a level-order-traversal of tree in which
    each node at a particular level is traveresed before proceeding to the next level child.

    -> It is implemented using QUEUE data structure i.e: FIFO paradigm unlike DFS that uses
     STACK data structure i.e: LIFO paradigm.



     NOTE VERY IMPORTANT:

     -> In python you can implement STACK simply by using list ( append and pop ) both using
     O(n) complexity.
     -> Similarly, Queue can be implemented by

        from queue import Queue ( or collections queue if you want )
        => it has 4 methods ( .put, .get, .full, .empty )

     -> put, get have usual meanings and complexity of O(n)

'''

'''

    HERE I HAVE DONE PROBLEM "MONK AND THE ISLANDS IN HACKERRANK", it is a standard BFS/ DFS problem
    where I have to find the minimum distance between 1 and n node.

'''
from queue import Queue
from collections import defaultdict
n, m = map(int, input().split())
adj = defaultdict()
for i in range(m):
    a, b = map(int, input().split())
    if a not in adj:
        adj[a] = [b]
    else:
        adj[a] += [b]
    if b not in adj:
        adj[b] = [a]
    else:
        adj[b] += [a]

vis = [0]*(n+1)
dist = [0]*(n+1)


def bfs(src):
    q = Queue()
    q.put(src)
    vis[src] = 1
    dist[src] = 0

    while not q.empty():
        curr = q.get()
        for child in adj[curr]:
            if vis[child] == 0:
                q.put(child)
                dist[child] = dist[curr] + 1
                vis[child] = 1

bfs(1)
print(dist[n])
