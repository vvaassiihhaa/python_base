import sys

s = sys.stdin.readlines()
lst_in = [ list(map( int, x.strip().split() )) for x in s ]

res = "ДА"

for i in range( 0, 5 ):
    for j in range( 0, 5 ):
        if i != j:
            if lst_in[i][j] != lst_in[j][i]:
                res = "НЕТ"
print( res )