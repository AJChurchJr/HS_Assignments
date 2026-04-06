"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM - ADD CODE TO OUTPUT"""
import math
def binomialCo(n,k):
    def factorial(num):
        total=num
        for i in range(num-1):total*=(num-1)-i
        if total==0:total=1
        return total
    return factorial(n)/(factorial(k) * factorial(n - k))
