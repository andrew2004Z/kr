def game(c1, c2):
    if c1 == c2:
        print('ничья')
    elif c1 == 'бумага' and c2 == 'камень':
        print('первый')
    elif c1 == 'бумага' and c2 == 'ножницы':
        print('второй')
    elif c2 == 'бумага' and c1 == 'камень':
        print('второй')
    elif c2 == 'бумага' and c1 == 'ножницы':
        print('первый')
    elif c1 == 'камень' and c2 == 'ножницы':
        print('первый')
    elif c1 == 'камень' and c2 == 'бумага':
        print('второй')
    elif c2 == 'камень' and c1 == 'ножницы':
        print('второй')
    elif c2 == 'камень' and c1 == 'бумага':
        print('первый')
    elif c1 == 'ножницы' and c2 == 'камень':
        print('второй')
    elif c1 == 'ножницы' and c2 == 'бумага':
        print('первый')
    elif c2 == 'ножницы' and c1 == 'камень':
        print('первый')
    elif c2 == 'ножницы' and c1 == 'бумага':
        print('второй')

c1 = input()
c2 = input()
game(c1, c2)