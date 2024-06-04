import math

# ввод данных
a, b = map(int, input().split())

# здесь продолжите программу
res = a * a + b * b
res = round( math.sqrt( res ), 2 )
print( res )