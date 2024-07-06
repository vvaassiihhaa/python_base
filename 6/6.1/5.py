s = input()
ss = s.split()
for i in range( len( ss ) ):
    ss[i] = ss[i].split( "=" )
d = dict( ss )
if "house" in d and "True" in d and "5" in d:
    print( "ДА" )
else:
    print( "НЕТ" )   