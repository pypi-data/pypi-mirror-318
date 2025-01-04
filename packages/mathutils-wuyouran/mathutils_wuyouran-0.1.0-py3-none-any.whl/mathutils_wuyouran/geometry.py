# mathutils/geometry.py
import math

def circle_area(radius):
    """返回半径为 radius 的圆的面积"""
    if radius < 0:
        raise ValueError("半径不能为负数")
    return math.pi * radius ** 2

def rectangle_area(length, width):
    """返回矩形的面积"""
    if length < 0 or width < 0:
        raise ValueError("长度和宽度不能为负数")
    return length * width

def triangle_area(base, height):
    """返回三角形的面积"""
    if base < 0 or height < 0:
        raise ValueError("底边和高度不能为负数")
    return 0.5 * base * height
