N = int( input() )
l2 = []
for j in range( N ):
  l1 = []
  for i in range( N ) :
    if i == N - 1 :
      l1.append( 5 )
    else:
      l1.append( 1 )
  l2.append( l1 )

for row in l2:
  print( *row )