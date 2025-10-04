"""
This is a test comment. The purpose of the program is to
ask the user for three ingredients, the measurements in ounces,
the servings amount, and it will calculate the amount of ingredients required.
"""

user_name = input("Enter a username here: ")
user_age = int(input("What is the year of your birthday? Do not include letters. "))
age = 2025 - (user_age)

print("Welcome, " + str(user_name))
print("Age: " + str(age))
print()
print("Let's get started.")

print()
ingredientone = input("What is your first ingredient? ")
ingredientoneoz = int(input("How many ounces of this ingredient? "))
ingredienttwo = input("What is your second ingredient? ")
ingredienttwooz = int(input("How many ounces of this ingredient? "))
ingredientthree = input("What is your third ingredient? ")
ingredientthreeoz = int(input("How many ounces of this ingredient? "))
servingsnumber = int(input("How many servings? "))

total_one = ingredientoneoz / servingsnumber
total_two = ingredienttwooz / servingsnumber
total_three = ingredientthreeoz / servingsnumber

print("Total ounces of " + str(ingredientone) + " per serving is: " + str(total_one))
print("Total ounces of " + str(ingredienttwo) + " per serving is: " + str(total_two))
print("Total ounces of " + str(ingredientthree) + " per serving is: " + str(total_three))

print()
print("Complete!")
