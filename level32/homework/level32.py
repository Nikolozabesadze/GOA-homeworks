def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


print(check_even_odd(4))  
print(check_even_odd(7))  





def negate_number():
    number = float(input("number: ")) 
    if number > 0:
        return -number 
    elif number < 0:
        return -number  
    else:
        return 0  


result = negate_number()
print(result)
