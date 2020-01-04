for i in range(99, 0, -1):
    print('{0} of beer on the wall, {0} of beer.'.format(f'{i} bottles' if i>1 else '1 bottle'))
    print('Take one down and pass it around, {0} of beer on the wall.\n'.format(f'{i-1} bottles' if i>2 else '1 bottle' if i==2 else 'no more bottles'))

print('No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')