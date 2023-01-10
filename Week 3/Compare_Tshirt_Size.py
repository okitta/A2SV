test_cases= int(input())
for iterator in range(test_cases):
    given_size = input().split()
    if 'S' in given_size[0]:
        if 'L' in given_size[1] or 'M' in given_size[1]:
            print('<')
        else:
            if given_size[0].count('X') > given_size[1].count('X'):
                print('<')
            elif given_size[0].count('X') < given_size[1].count('X'):
                print('>')
            else:
                print('=')
    elif 'M' in given_size[0]:
        if 'L' in given_size[1]:
            print('<')
        elif 'S' in given_size[1]:
            print('>')
        else:
            if given_size[0].count('X') > given_size[1].count('X'):
                print('>')
            elif given_size[0].count('X') < given_size[1].count('X'):
                print('<')
            else:
                print('=')
    if 'L' in given_size[0]:
        if 'S' in given_size[1] or 'M' in given_size[1]:
            print('>')
        else:
            if given_size[0].count('X') > given_size[1].count('X'):
                print('>')
            elif given_size[0].count('X') < given_size[1].count('X'):
                print('<')
            else:
                print('=')