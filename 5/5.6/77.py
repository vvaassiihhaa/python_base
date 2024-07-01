n = int( input() )

lst = []
powers_of_two = [ 64, 32, 16, 8, 4, 2, 1 ]

for power in powers_of_two:
    while n >= power:
        n -= power
        lst.append( power )

print( *lst )