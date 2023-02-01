if __name__ == "__main__":
    total_input = int(input())
    given_inputs = list(map(int,input().split()))
    counter = 0
    max_value = given_inputs[0]
    min_value = given_inputs[0]
    for item in given_inputs:
        if item > max_value:
            max_value = item
            counter+=1
        elif item < min_value:
            min_value = item
            counter+=1
    print(counter)