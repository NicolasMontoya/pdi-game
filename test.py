#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:51:35 2019

@author: nicolas
"""
import random
from multiprocessing import Process, Queue

def af(q):
    while True:
        q.put(random.randint(0,1000))

def bf(q):
    while True:
        if not q.empty():
            print (q.get())

def main():
    a = Queue()  
    p = Process(target=af, args=(a,))
    c = Process(target=bf, args=(a,))
    p.start()
    c.start()
    p.join()
    c.join()


if __name__ == "__main__":
    main()