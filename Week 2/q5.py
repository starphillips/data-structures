# A bakery sells loaves of bread for £1.49 each. Day old bread is discounted by 60 percent.
# Write a program that begins by reading the number of loaves of day old bread being
# purchased from the user. Then your program should display the regular price for the bread,
# the discount because it is a day old, and the total price. All of the values should be displayed
# using two decimal places, and the decimal points in all of the numbers should be aligned
# when reasonable values are entered by the user.

bread = 1.49

sixty = bread * 0.6

disBread = bread - sixty

# print(f"{disBread:.2f}")

total_loaf = int(input('How many loafs are you buying?'))

ori_price = total_loaf * bread

dis_price = total_loaf * disBread

print(f"Original price per unit: {bread:.2f}")

print(f"Original total: {ori_price:.2f}")

print(f"Discounted price per unit: {disBread: .2f}")

print(f"Your new total is : {dis_price: .2f}")
