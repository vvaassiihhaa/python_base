s = "one=1 two=2 three=3"
ss = s.split()
for i in range( len( ss ) ):
    ss[i] = ss[i].split( "=" )
    ss[i][1] = int( ss[i][1] )
d = dict( ss )
print( *sorted( d.items() ) )


#    print( ss[i] )    

# s = "one=1 two=2 three=3"
# sss = s.split()
# sss = input().split()
# print( sss )
# for i in range( len( sss ) ):
    # sss[i] = sss[i].split( "=" )
# d = dict( sss )
# print( *sorted( d.items() ) )


# print( sss )

# for ss in sss:   

# sss = sss.split("=")
# print( sss )

# ss = "one=1"
#a = ss.split("=")
# print( a )

# lst = input()
# print( lst )
# d = dict( lst )
# print(*sorted(d.items()))

# one=1 two=2 three=3
