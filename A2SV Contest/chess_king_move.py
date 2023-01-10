def king_movment(king_position):
    if king_position[0][1] == '1' or king_position[0][1] == '8':
        if king_position[0][0] == 'a' or king_position[0][0] == 'h':
            print(3)
        else:
            print(5)
    elif king_position[0][0] == 'a' or king_position[0][0] == 'h':
            if king_position[0][1] != '1' and king_position[0][1] != '8':
                print(5)
    else:
        print(8)
if __name__ =='__main__':
    king_position = input().split()
    king_movment(king_position)
    