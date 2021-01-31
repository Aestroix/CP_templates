# IN OUT TIME IN A NODE IN A GRAPH
# to find out if an element lies in the subtree of other node

'''
    the one condition to check for it is that the in time of the child is more than the root and out time is less
    than the out time of root

    problem link: https://www.codechef.com/problems/FIRESC ( it's not related to in out time though )

    - finding the number of connected components
    - counting the number of members in each connected components

'''


def dfs(n, mark):
    vis[n-1] = mark
    for i in conn[n]:
        if vis[i-1] == 0:
            dfs(i, mark)


conn = {}
for _ in range(int(input())):
    n , m = map(int, input().split())
    for i in range(1, n+1):
        conn.setdefault(i, [])

    for i in range(m):
        x ,y = map(int, input().split())
        conn[x].append(y)
        conn[y].append(x)

    vis = [0]*n
    mark = 0
    for i in range(n):
        if vis[i] == 0:
            mark += 1
            dfs(i+1, mark)
    print(mark, end=' ')
    count_the_connected_members = [0]*mark
    for i in range(n):
        count_the_connected_members[vis[i] - 1] += 1

    ans = 1
    for i in count_the_connected_members:
        ans *= i

    print(ans)







