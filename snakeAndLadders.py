#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def findDistance(parent, j):
    Path_len = 1
    if parent[j] == -1 and j < 100 : #Base Case : If j is source
        return 0 # when parent[-1] then path length = 0    
    l = findDistance(parent , parent[j])

    #increment path length
    Path_len = l + Path_len
    return Path_len
    
def findShortestDistance(vertex,src,dest):
    visited = [False] * 100
    parent = [-1] * 100
    
    # Create a queue for BFS
    queue=[]

    # Mark the source node as visited and enqueue it
    queue.append(src)
    visited[src] = True

    while queue :
            
        # Dequeue a vertex from queue 
        s = queue.pop(0)
            
        # if s = dest then print the path and return
        if s == dest:
            print(parent)
            return findDistance(parent, s)
                

        # Get all adjacent vertices of the dequeued vertex s
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for i in vertex[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                parent[i] = s
    return -1
    

def quickestWayUp(ladders, snakes):
    # Write your code here
    vertex = defaultdict(list)
    for i in range(99):
        for j in range(6,0,-1):
            if j+i <= 99:
                vertex[i].append(j+i)
            else:
                vertex[i].append(i)
    print(vertex)
    #update for laders
    for ladder in ladders:
        m,n = ladder[0],ladder[1]
        index = 0
        for i in range(m-1-6,m-1,1):
            if i>=0 and len(vertex[i]) != 0:
                vertex[i][index]=n-1
            index+=1
        vertex[m-1] = []
    #update for snakes
    # print(vertex)
    for snake in snakes:
        m,n = snake[0],snake[1]
        index = 0
        # print("m=",m-1)
        # print("n=",n-1)
        for i in range(m-1-6,m-1,1):
            # print("index",i,index)
            if i>=0 and len(vertex[i]) != 0:
                vertex[i][index]=n-1
            index+=1
        vertex[m-1] = []
    
    print(vertex)
    return findShortestDistance(vertex,0,99)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
