n = int( input() )
prostoe = True
for ii in range( 2, n ):
    if n % ii == 0:
        prostoe = False
        break

if prostoe:
    print( "ДА" )
else:
    print( "НЕТ" )
