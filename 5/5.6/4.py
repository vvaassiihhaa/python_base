import sys

s = sys.stdin.readlines()
lst_in = [ list(map( int, x.strip().split() )) for x in s ]

res = "ДА"

for i in range( 0, 5 ):
    for j in range( 0, 5 ):
        if lst_in[i][j] == 1:
            for di in range( -1, 2 ):
                for dj in range( -1, 2 ):
                    if not ( di == 0 and dj == 0 ):
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < 5 and 0 <= nj < 5 :
                            if lst_in[ni][nj] == 1:
                                res = "НЕТ"
print( res )


        # print( lst_in[i][j] )