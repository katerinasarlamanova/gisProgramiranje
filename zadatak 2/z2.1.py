# -*- coding: utf-8 -*-

from math import factorial

def factorial(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n = int(input("Unesite broj: "))
    s = factorial(n)
    print "Faktorijel broja", n,"je:", s

main()