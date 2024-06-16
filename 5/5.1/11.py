n, m = map( int, input().split() )

while n % 2 == 0:
    n += 1

while n < m:
    print( n, end=" " )
    n += 2