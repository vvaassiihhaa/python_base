f = list( map( float, input().split() ) )
ls = [ f[i] for i in range( 0, len(f), 2 ) ]
print( *ls )