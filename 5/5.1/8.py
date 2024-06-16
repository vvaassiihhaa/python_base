n = int( input() )
a = 1
b = 1
print( "1 1", end=" " )
i = 2
while i < n:
    i += 1
    c = a + b
    a, b = b, c
    print( c, end=" ")

# 1 1 2 3