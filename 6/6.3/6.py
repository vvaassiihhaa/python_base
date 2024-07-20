students = input().split()
t = tuple( students )
t2 = ()
for person in students:
  if "ва" in person.lower():
    t2 += ( person.lower(), )
print( *t2 )
    