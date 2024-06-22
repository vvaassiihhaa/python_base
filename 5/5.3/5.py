l = list( map( int, input().split() ) )
res = 0
for ii in l:
    if ii % 2 == 0:
        continue
    res += ii
print( res )

# 8 11 -2 4 0 13 19 12 7