# Drink containers holding one litre or less have a £0.25 deposit, and drink containers holding more
# than one litre have a £0.50 deposit. Write a program that reads the number of containers of each
# size received from the user. Your program should continue by computing and displaying the refund
# that will be received for returning those containers. Format the output so that it includes a £ sign
# and always displays exactly two decimal places.

small_container = 0.25
big_container = 0.5

users_small = float(
    input("Enter the number of containers that are less than 1 litres: "))
users_big = float(
    input("Enter the number of containers that are more than 1 litre: "))

refund = (users_small * small_container) + (users_big * big_container)

print(f'Your total refund is: £{refund:.2f}')
