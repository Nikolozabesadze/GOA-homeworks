def simple_calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "error: its not possible to devide to 0"
        return num1 / num2
    else:
        return "error: incorrect operation"


print(simple_calculator(10, 5, "+"))  
print(simple_calculator(10, 5, "-")) 
print(simple_calculator(10, 5, "*"))   
print(simple_calculator(10, 0, "/"))        
print(simple_calculator(10, 5, "/"))         
print(simple_calculator(10, 5, "incorrect"))       