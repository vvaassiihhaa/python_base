n = int ( input() )
strn = str( n )
lenn = len( strn )
i = 0
res = 1
while i < lenn:
    res *= int( strn[i] )
    i += 1
print( res )

# 821