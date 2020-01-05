def beer(n):
    a = f'{n} bottles' if n>1 else '1 bottle'
    b = f'{n-1} bottles' if n>2 else '1 bottle' if n==2 else 'no more bottles'
    return f'{a} of beer on the wall, {a} of beer.\nTake one down and pass it around, {b} of beer on the wall.\n'


if __name__ == '__main__':
    for i in range(99, 0, -1):
        print(beer(i))

    print('No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')