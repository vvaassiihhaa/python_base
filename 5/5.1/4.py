n = int ( input() )
S = 1
i = 1
while i < n:
    i += 1
    S += round( 1/i, 3 )
res = round( S, 3 )
print( res )