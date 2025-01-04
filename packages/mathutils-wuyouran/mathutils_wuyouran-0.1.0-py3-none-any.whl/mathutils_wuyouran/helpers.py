# mathutils/helpers.py

def gcd(a, b):
    """返回 a 和 b 的最大公约数"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """返回 a 和 b 的最小公倍数"""
    return abs(a * b) // gcd(a, b)
