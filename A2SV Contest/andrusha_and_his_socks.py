def pair_socks(each_socks):
    new_stack = []
    counter = 0
    max_number = 0
    for item in each_socks:
        if item in new_stack:
            new_stack.pop()
            if max_number < counter:
                max_number = counter
                counter = 0
        else:
            new_stack.append(item)
            counter+=1
    return max_number

if __name__ == "__main__":
    total_socks_number = int(input())
    each_socks_list = list(map(int,input().split()))
    print(pair_socks(each_socks_list))