m, n = map( int, input().split() )
if m % n == 0:
    print( int( m / n ) )
else:
    print( f"{m} на {n} нацело не делится" )