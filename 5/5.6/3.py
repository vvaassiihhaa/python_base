n = int ( input() )
for i in range(2,n):
  prostoe = True
  for ii in range( 2, i // 2 + 1 ):
      if i % ii == 0:
          prostoe = False
  if prostoe:
      print( i, end = " " )