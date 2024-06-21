import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

l = len( lst_in )

while l > 0:
    l -= 1    
    ind = lst_in[ l ].find( " " )
    if ind > 0:
        del lst_in[ l ]           

print( *lst_in )
