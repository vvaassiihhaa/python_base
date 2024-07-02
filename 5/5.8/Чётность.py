N = 10
a = [ _ % 2 == 0 for _ in range( N ) ]
print( a )

a = [ .5 * x + 1 for x in range(N)]
print( a )

# [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
# [True, False, True, False, True, False, True, False, True, False]

a = [d for d in "python"]
print( a )
# ['p', 'y', 't', 'h', 'o', 'n']

a = [ord(d) for d in ("pyt"
                      "hon")]
print( a )

t = ["Я", "б", "Python", "выучил", "только", "за", "то", "что", "есть", "он", "на", "этом", "канале"]
a = [d for d in t]
print( a )

a = [len(d) for d in t]
print( a )