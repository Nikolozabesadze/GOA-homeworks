x = int(input('enter x: '))
y = int(input('enter y: '))
k = int(input('enter k: '))
z = int(input('enter z: '))

print(x + y)
print(y + k)
print(k + x)
print(x + y)
print(y + k)
print(k + x)

print(x - y)
print(y - k)
print(k - x)
print(x - y)
print(y - k)
print(k - x)

print(x * y)
print(y * k)
print(k * x)
print(x * y)
print(y * k)
print(k * x)

print(x / y)
print(y / k)
print(k / x)
print(x / y)
print(y / k)
print(k / x)



# Input the ages of family members
family_ages = [int(age) for age in input("Enter the ages of family members separated by spaces: ").split()]

# Calculate and output the ages after 20 years
future_ages = [age + 20 for age in family_ages]
print("Ages of family members after 20 years:", future_ages)


name = input(' name: ')
surname = input('surname: ')
age = input('age: ')
city = input('city:')
country = input('country:')
favourite_color = input('favourite_color:')
favourite_car = input('favourite_car:')
favourite_food = input('favourite_food:')
favourite_sport = input('favourite_sport')


print('hello my name is',name ,surname, 'i am ' ,age, 'years old. i live in ' ,country , city, 'my favourite color is' ,favourite_color, 'and my favourite sport is a' , favourite_sport, 'and also my favourite food ia a' ,favourite_food, )

# Ask the user to enter their name
name = input("Please enter your name: ")

# Print a greeting message using their name
print("Hello," ,name, "Welcome! happy birthday to you now you are 13 years old be good and also healthy happy birthday again")
