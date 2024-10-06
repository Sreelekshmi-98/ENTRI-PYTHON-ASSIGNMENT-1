name = "Bob"
student_number = "ST1001"
email = "bob@gmail.com"

print(name)
print(student_number)
print(email)

print("Bob\nST1001\nbob@gmail.com")

num1 = 14
num2 = 7

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} / {num2} = {division}")

for i in range(1, 6):
    print(i)

print('"SDK" stands for "Software Development Kit", whereas\n"IDE" stands for "Integrated Development Environment".')

print("python is an \"awesome\" language.")

print("python\n\t2023")

print('I\'m from Entri.\b')

print("\65")

print("\x65")

print("Entri", "2023", sep="\n")

print("Entri", "2023", sep="\b")

print("Entri", "2023", sep="*", end="\b\b\b\b")

num = 23
textnum = "57"
decimal = 98.3

print(f'Type of num: {type(num)}')
print(f'Type of textnum: {type(textnum)}')
print(f'Type of decimal: {type(decimal)}')

sum_of_variables = num + int(textnum) + decimal

print(f'Sum of variables: {sum_of_variables}')
print(f'Type of the sum: {type(sum_of_variables)}')

days_in_year = 365  # In a non-leap year
hours_in_day = 24
minutes_in_hour = 60

total_minutes_in_year = days_in_year * hours_in_day * minutes_in_hour

print("This code calculates the total number of minutes in a year using the formula:")
print("Total minutes = No. of days in a year * Hours in a day * Minutes in an hour")

print(f"Total number of minutes in a year: {total_minutes_in_year}")

name = input("Please enter your name: Sreelekshmi")

print(f"Hi {name}, welcome to Python programming :)")

conversion_rate = 1.30  # Example rate: £1 = $1.30

pounds = float(input("Please enter amount in pounds: "))

dollars = pounds * conversion_rate

print(f"£{pounds} are ${dollars:.2f}")





