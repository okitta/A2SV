def list_method(given_list):
    new_list=[]
    for iterator in given_list:
        iterator = iterator.split(' ')
        if iterator[0] == 'insert':
            new_list.insert(int(iterator[1]),int(iterator[2]))
        elif iterator[0] == 'append':
            new_list.append(int(iterator[1]))
        elif iterator[0] == 'remove':
            new_list.remove(int(iterator[1]))
        elif iterator[0] == 'pop':
            new_list.pop()
        elif iterator[0] == 'print':
            print(new_list)
        elif iterator[0] == 'sort':
            for item in new_list:
                int(item)
            new_list.sort()
        elif iterator[0] == 'reverse':
            for item in new_list:
                int(item)
            new_list.reverse()


if __name__ == '__main__':
    input_number = int(input())
    given_list = [input() for iterator in range(input_number)]
    list_method(given_list)