lyrics = '{0} bottles of beer on the wall, {0} bottles of beer.\nTake one down and pass it around, {1} bottles of beer on the wall.\n'

for i in range(99, 0, -1):
    print(lyrics.format(i, i-1 if i!=1 else 'no more'))

print('No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')