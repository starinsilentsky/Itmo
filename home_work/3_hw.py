# Task 1
def max_number(num1, num2):
    print(max(num1, num2))

max_number(5, 10)

# Task 2
def check_difference(num1, num2):
    if abs(num1 - num2) == 135:
        print("yes")
    else:
        print("No")

check_difference(200, 65)

# Task 3
def season_of_year(month):
    if month in [12, 1, 2]:
        print("Winter")
    elif month in [3, 4, 5]:
        print("Spring")
    elif month in [6, 7, 8]:
        print("Summer")
    elif month in [9, 10, 11]:
        print("Autumn")

season_of_year(7)

# Task 4
def check_numbers(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        print("yes")
    else:
        print("no")

check_numbers(15, 20, 5)
# Task 5
def count_positive_numbers(numbers):
    count = sum(1 for num in numbers if num > 0)
    print(count)

count_positive_numbers([-1, 5, -3, 10, 20])

# Task 6
def calculate_days(years, months):
    days = years * 12 * 29 + months * 29
    print(days)

calculate_days(2, 3)