'''
    ONE OF THE APPROACH is to make DFS calls individually to each node of the tree and find the farthest
    node from there and the maximum distance is the answer
    Complexity: O ( n^2 )

    Better approach is to choose any arbitrary point and make a dfs call to find the most distant node
    from there and then make another dfs call from that new found node and then find the maximum distance
    from there.
    Complexity: O ( 2*n )

'''