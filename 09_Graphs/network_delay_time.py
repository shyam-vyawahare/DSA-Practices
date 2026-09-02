"""
Problem: Network Delay Time

You are given a directed, weighted graph representing a network.

times[i] = [u, v, w]

means a signal takes w units of time to travel
from node u to node v.

A signal is sent from node k.

Return the minimum time required for the signal to reach
all nodes.

If some node cannot be reached, return -1.

Example:

Input:
times = [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1]
]

n = 4
k = 2

Graph:

        1
    2 ------> 1
    |
    | 1
    ↓
    3 -----> 4
       1

Shortest distances from node 2:

2 -> 1 = 1
