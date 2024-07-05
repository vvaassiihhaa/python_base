from math import sqrt
num = list( map( int, input().split() ) )
N = int( sqrt( len( num ) ) )

a = [
  [ num[ i + j * N ] for i in range( N ) ]
  for j in range( N )
]

print( a )

# print( N )


# 1 2 3 4 5 6 7 8 9