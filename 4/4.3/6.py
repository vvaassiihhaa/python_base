m = ['#до', 'ре', 'ми', '#фа', 'соль', 'ля', 'си']
n1, n2, n3 = ( b - 1 for b in map(int, input().split()) )
print( m[n1], m[n2], m[n3] )


