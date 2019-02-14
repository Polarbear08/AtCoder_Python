# -*- coding: utf-8 -*-
"""
Standard I/O with sys library

@author: polarbear08
"""

# Input
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**7) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())