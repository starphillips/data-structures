'''Exercise 6: Dog Years
Dogs reach adulthood in approximately two years. As a
result, some people believe that it is better to count each of the first two human years as
10.5 dog years, and then count each additional human year as 4 dog years. 

Write a program that implements the conversion from human years to dog years described 
in the previousparagraph. 

Ensure that your program works correctly for conversions of less than two
human years and for conversions of two or more human years. Your program should display
an appropriate error message if the user enters a negative number.'''


def year_conversion(human_years):
    # Dictionary to use conversion details
    details = {'first_two': 10.5,
               'there_after': 4}

    # Print error if wrongly inputted
    if human_years < 0:
        return 'The number of years cannot be less than 0'
    if human_years <= 2:
        dog_years = human_years * details["first_two"]
    else:
        dog_years = (2 * details["first_two"]) + \
            ((human_years - 2) * details["there_after"])

    return f"{human_years} human years is equivalent to {dog_years} dog years"


def main():
    try:
        # User to input the data
        human_years = float(
            input("Enter the number of human years for conversion: "))

        # Converting human to dog
        results = year_conversion(human_years)

        print(results)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == '__main__':
    main()
