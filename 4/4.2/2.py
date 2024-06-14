a, b, c = map( int, input().split() )
res = a
if b < res:
  res = b
if c < res:
  res = c
print( res )
  