#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

#path compression
def find(parent,x):
    if parent[x] == x:
        return x
    return find(parent,parent[x])

#union by rank
def union(parent,rank,x,y):
    xroot = find(parent,x)
    yroot = find(parent,y)
    
    if rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    elif rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        rank[xroot]+=1

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    sindex = sorted(range(len(g_weight)),key=g_weight.__getitem__)
    
    parent = []
    rank = []
    for i in range(g_nodes):
        parent.append(i)
        rank.append(0)
    e = 0
    i = 0
    min_cost = 0
    while e < g_nodes - 1:
        i+=1
        k = sindex.pop(0)
        x = find(parent, g_from[k]-1)
        y = find(parent, g_to[k]-1)
        if x != y:
            e += 1
            min_cost+=g_weight[k]
            union(parent,rank,x,y)
    return min_cost
            
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res))
    fptr.close()
