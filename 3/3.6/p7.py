marks = list( map( int, input().split() ) )
средний_балл = round( sum( marks ) / len( marks ), 1 )
print( средний_балл )