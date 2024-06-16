S = 1000
n = int( input() )
while n > 0:
    n -= 1
    S += S * 0.05
res = round( S, 2 )
print( res )