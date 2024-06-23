n = int( input() )
S = 0
for ii in range( n ):
    if ii % 3 == 0 or ii % 5 == 0:
        S += ii
print( S )