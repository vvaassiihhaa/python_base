import math

# ввод данных
n, k = map(int, input().split())

# здесь продолжите программу
nf = math.factorial( n )
kf = math.factorial( k )
n_k =  math.factorial( n - k ) 
res = round( nf / kf / n_k )
print( res )