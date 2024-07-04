# g( u( x + 1 ) ) = ( x + 1 ) ^ 2

g = [
    u ** 2
    for u in
    [ x + 1 for x in range( 5 ) ]   
]
print( g ) # [1, 4, 9, 16, 25]

A = [
    [ 1,  2,  3,  4 ],
    [ 5,  6,  7,  8 ],
    [ 9, 10, 11, 12 ] 
]
# for line in A:
    # print( *line )
# print()

A = [
    [ row[i] for row in A ]
    for i in range( len( A[0] ) )
]

# for line in A:
    # print( *line )
# print()



A = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
A = [
    [ x ** 2 for x in row ]
    for row in A
]
A = [
    [ _ ** 2 for _ in line ]
    for line in A
]

# print( A )

M, N = 3, 4
matrix = [
    [ a + b * 3 for a in range( M ) ]
    for b in range( N )
]
# print( matrix )

# [ [ещё один генератор списка]
#   for <переменная> in <итерируемый объект>   
# ]

# [<оператор> for <счётчик> in <итерируемый объект>]

a = [ ( i, j )
      for i in range( 3 )
      for j in range( 4 )
]
# print( a )

a = [ ( i, j )
      for i in range( 3 ) if i % 3 == 0
      for j in range( 4 ) if j % 2 != 0
]
# print( a )

a = [ f"{i} * {j} = {i*j}"
    for i in range( 1, 4 )
    for j in range( 1, 4 )     
]
# for line in a:
#   print( line )

matrix = [ [  0,  1,  2,  3 ],
           [ 10, 11, 12, 13 ],
           [ 20, 21, 22, 23 ] ]
a = [ _
      for line in matrix
      for _ in line
]
# print( *a )

