# mathutils/arithmetic.py

def add(a, b):
    """返回 a 和 b 的和"""
    return a + b

def subtract(a, b):
    """返回 a 和 b 的差"""
    return a - b

def multiply(a, b):
    """返回 a 和 b 的积"""
    return a * b

def divide(a, b):
    """返回 a 和 b 的商，如果 b 为 0，则抛出异常"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b
