n1 = list( map( int, input().split() ) )
n2 = list( map( int, input().split() ) )
lc = [ n1[ i ] + n2[ i ] for i in range( len( n1 ) ) ]
print( *lc )
