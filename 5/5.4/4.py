ll = list( map( int, input(). split() ) )
for ii, dd in enumerate( ll ):
  ll[ ii ] = dd * dd
print( *ll )  


# индекс, значение = enumerate(объект)
# for i, d in enumerate(digs):