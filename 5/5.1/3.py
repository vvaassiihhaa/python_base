cost = float( input() )
i = 1
while i < 10:
    i += 1
    res = round( cost * i, 1 )
    print( res, end=" " )