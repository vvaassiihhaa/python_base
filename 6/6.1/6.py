s = input()
ss = s.split()
for i in range( len( ss ) ):
  ss[i] = ss[i].split( "=" )
d = dict( ss )

if "False" in d:
  del d["False"]

if "3" in d:
  del d["3"]

print( *sorted( d.items() ) )