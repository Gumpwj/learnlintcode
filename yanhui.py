#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import deque

def yanhui(k):
    
    q = deque([1])
    
    for i in range(k):
        for _ in range(i):
            q.append(q.popleft() + q[0])
        q.append(1)
    return list(q) 

result = yanhui(3)
print result   