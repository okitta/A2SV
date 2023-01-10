test_cases = int(input())
for iterator in range(test_cases):
    array = []
    minimum_cost = 0
    plant_number_and_cost = input().split()
    array_items = input().split()
    # print(array_items)
    for items in array_items:
        # print(array_items.count(items))
        if array_items.count(items) < int(plant_number_and_cost[1]):
            minimum_cost += 1
        else:
            if items not in array:
                minimum_cost += int(plant_number_and_cost[1])
                array.append(items)
            else:
                pass
    print(minimum_cost)