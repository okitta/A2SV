given_inputs = int(input())
total_rooms = map(int,input().split())
room_list = list(total_rooms)
room_count = {}
for item in room_list:
    if item not in room_count.keys():
        room_count[item] = 0
    room_count[item]+=1
for each_item,each_index in room_count.items():
    if each_index == 1:
        print(each_item)