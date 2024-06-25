fd = list( map( float, input().split() ) )
for i, d in enumerate( fd ):
  if d < 0:
    fd[i] = float( -1 )
print( *fd )