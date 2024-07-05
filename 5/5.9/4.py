import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

A = [
    [ line[i] for line in lst_in ]  
    for i in range( len( lst_in[0] ) ) 
]

for row in A:
    print( *row )


# Sample Input:

# 1 2 3
# 4 5 6
# 7 8 9
# 5 4 3

# Sample Output:

# 1 4 7 5
# 2 5 8 4
# 3 6 9 3