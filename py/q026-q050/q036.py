# https://www.hackerrank.com/challenges/collections-counter/problem

shoe_number = int(input())
shoe_size_list = [int(x) for x in input().split()]
customer_count = int(input())
money_made = 0
for _ in range(customer_count):
    customer = [int(x) for x in input().split()]
    if customer[0] in shoe_size_list:
        shoe_size_list.remove(customer[0])
        money_made += customer[1]

print(money_made)