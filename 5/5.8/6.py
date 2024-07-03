N = int( input() )
lc = [
    [ j for i in range( N ) ]
    for j in range( N )
]
for line in lc:
  print( *line )

# print( lc )