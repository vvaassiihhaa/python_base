st = input()
c = st.count( "ра" )
if c == 0:
    print( -1 )
else:
    ind = -1
    for ii in range( c ):
        ind += 1
        ind = st.find( "ра", ind )
        print( str( ind ), end = " ")


# Барабанщик бил бой в барабан