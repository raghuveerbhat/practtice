#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#


    

def bfs(n, m, edges, s):
    # Write your code here
    visited = [False] * n
    cost = 6
    queue = []
    
    edg = defaultdict(list)
    for i in edges:
        edg[i[0]].append(i[1])
        edg[i[1]].append(i[0])
    
    
    answer = [-1] * n
    queue.append(s)
    visited[s-1] = True
    nlayer = 1
    layer = 0
    while queue:
        j = queue.pop(0)
        answer[j-1] = cost * layer
        nlayer-=1
        for i in edg[j]:
            if visited[i-1] == False:
                visited[i-1] = True
                queue.append(i)
        if nlayer == 0:
            layer += 1
            nlayer = len(queue)
    answer.pop(s-1)
    return answer
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
