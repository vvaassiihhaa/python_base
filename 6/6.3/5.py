cities = input().split()
t = tuple( cities )
t2 = ()
for city in t:
  if not city == "Ульяновск":
    t2 += ( city, )
print( *t2 )   