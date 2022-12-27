# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_english = int(input())
list_of_english_subscribers = set(map(int,input().split(' ')))
number_of_franch = int(input())
list_of_franch_subscribers = set(map(int,input().split(' ')))
print(len(list_of_english_subscribers.union(list_of_franch_subscribers)))