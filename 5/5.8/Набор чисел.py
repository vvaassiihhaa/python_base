d_inp = input("Целые числа через пробел: ")

a = [int(d) for d in d_inp.split()]
print( a )

a = [d for d in d_inp.split()]
print( a )

# [1, 2, 3, 45]
# ['1', '2', '3', '45']

d_inp = list( map(int, input("Целые числа через пробел: ").split()) )
print( d_inp )