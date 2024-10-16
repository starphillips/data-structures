'''Pretend that you have just opened a new savings account that earns 4 percent interest per year. The
interest that you earn is paid at the end of the year, and is added to the balance of the savings
account. Write a program that begins by reading the amount of money deposited into the account
from the user. Then your program should compute and display the amount in the savings account
after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places'''


interest = 0.04

deposit = float(input("Enter the deposting amount: "))

first_year = deposit + (deposit * interest)
second_year = first_year + (first_year * interest)
third_year = second_year + (second_year * interest)

print(f"First year: {first_year:.2f}")
print(f"Second year: {second_year:.2f}")
print(f"Third year: {third_year:.2f}")
