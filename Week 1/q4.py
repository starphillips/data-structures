# Consider the software that runs on a self-checkout machine. One task that it must be able to
# perform is to determine how much change to provide when the shopper pays for a purchase with
# cash. Write a program that begins by reading a number of pence from the user as an integer.

# Then your program should compute and display the denominations of the coins that should be used to
# give that amount of change to the shopper.

# The change should be given using as few coins as possible. Assume that the machine is loaded with
# all types of coins ranging from 1p to £2.

# Note the machine is able to accept up to £20 in any combinations of currency. Payments in pounds
# should be converted into pence for processing purposes, i.e. £1 = 100 pence and £20 = 2000 pence.
# The machine can only give change in coins.

userChange = float(input('How much change do I owe ya?  £'))

conChange = round(userChange * 100)


two_pounds = 0
one_pound = 0
fifty_pence = 0
twenty_pence = 0
ten_pence = 0
five_pence = 0
two_pence = 0
one_pence = 0


if conChange >= 200:
    two_pounds = conChange // 200
    conChange = conChange % 200

if conChange >= 100:
    one_pound = conChange // 100
    conChange = conChange % 100

if conChange >= 50:
    fifty_pence = conChange // 50
    conChange = conChange % 50

if conChange >= 20:
    twenty_pence = conChange // 20
    conChange = conChange % 20

if conChange >= 10:
    ten_pence = conChange // 10
    conChange = conChange % 10

if conChange >= 5:
    five_pence = conChange // 5
    conChange = conChange % 5

if conChange >= 2:
    two_pence = conChange // 2
    conChange = conChange % 2

if conChange >= 1:
    one_pence = conChange // 1
    conChange = conChange % 1

print("You need:")
if two_pounds > 0:
    print(f"£2 coins: {two_pounds}")
if one_pound > 0:
    print(f"£1 coins: {one_pound}")
if fifty_pence > 0:
    print(f"50p coins: {fifty_pence}")
if twenty_pence > 0:
    print(f"20p coins: {twenty_pence}")
if ten_pence > 0:
    print(f"10p coins: {ten_pence}")
if two_pence > 0:
    print(f"2p coins: {two_pence}")
if one_pence > 0:
    print(f"1p coins: {one_pence}")
