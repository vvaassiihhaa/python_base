aa = input().split()

lst = [ [ aa[i], int( aa[i + 1] )  ]
    for i in range( 0, len( aa ), 2 )
]

print( lst )


# print( aa )