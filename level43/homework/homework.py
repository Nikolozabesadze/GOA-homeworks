def count_items(item_list, item):
    count = 0
    for i in item_list:
        if i == item:
            count += 1
    return count

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(count_items(items, 'apple'))  






def sum_of_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total


numbers = [1, 2, 3, 4, 5]
print(sum_of_list(numbers)) 





def average_of_list(num_list):
    if len(num_list) == 0:
        return 0  
    total = sum_of_list(num_list)
    average = total / len(num_list)
    return average

print(average_of_list(numbers))  




def reverse_list(items):
    reversed_items = []
    for item in items:
        reversed_items.insert(0, item) 
    return reversed_items


print(reverse_list(numbers)) 









