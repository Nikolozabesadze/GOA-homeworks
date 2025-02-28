def count_words(text):
    words = text.split()
    return len(words)


text = "This is an example text for counting words."
print("Word count:", count_words(text)) 






def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."


number = float(input("Enter a number: "))
print(check_number(number))




def categorize_age(age):
    if age < 0:
        return "Invalid age."
    elif age < 13:
        return "Child."
    elif age < 20:
        return "Teenager."
    elif age < 65:
        return "Adult."
    else:
        return "Senior."


age = int(input("Enter your age: "))
print(categorize_age(age))



def separate_even_odd(numbers):
    evens = []
    odds = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens, odds


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = separate_even_odd(num_list)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)



def average_of_list(num_list):
    if len(num_list) == 0:
        return 0
    total = sum(num_list)
    average = total / len(num_list)
    return average



numbers = [1, 2, 3, 4, 5]
print("Average:", average_of_list(numbers))  










