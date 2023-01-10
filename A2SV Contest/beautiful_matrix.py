def beautiful_materix(matrix):
    for iterator,item in enumerate(matrix):
        for iterator2,main_item in enumerate(item):
            if main_item == 1:
                print(abs(iterator-2)+abs(iterator2-2))    
if __name__ == '__main__':
    matrix = [list(map(int,input().split())) for iterator in range(5)]
    beautiful_materix(matrix)