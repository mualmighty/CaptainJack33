"""
演示怎样使用 Python 列表解析语法来产生列表 [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

print(list(2**i for i in range(0,9)))