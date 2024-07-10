import math
d = {}
n = 1
while n > 0:
  n = int( input() )
  if n == 0:
    continue
  if n in d:
    print( f"значение из кэша: {d[n]}" )
  else:
    n_sqrt = round( math.sqrt( n ), 2 )
    d[n] = n_sqrt 
    print( d[n] )