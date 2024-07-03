n = int( input() )
lc = [ _ for _ in range( 1, n + 1 ) if n % _ == 0 ]
print( *lc )