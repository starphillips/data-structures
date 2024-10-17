''' Exercise 8: Season from Month and Day

The year is divided into four seasons: spring, summer, fall and winter. While the exact dates
that the seasons change vary a little bit from year to year because of the way that the
calendar is constructed, we will use the following dates for this exercise:

Season - First day
Spring - March 20
Summer - June 21
Fall - September 22
Winter - December 21

Create a program that reads a month and day from the user. The user will enter the name of
the month as a string, followed by the day within the month as an integer. Then your
program should display the season associated with the date that was entered. '''


def name_the_season(month, day):

    month = month.capitalize()

    if (month == "March" and day >= 20) or (month == "April") or (month == "May") or (month == "June" and day < 21):
        return 'Spring'
    elif (month == "June" and day >= 21) or (month == "July") or (month == "August") or (month == "September" and day < 22):
        return 'Summer'
    elif (month == "September" and day >= 22) or (month == "October") or (month == "November") or (month == "December" and day < 21):
        return 'Fall'
    elif (month == "December" and day >= 21) or (month == "January") or (month == "February") or (month == "March" and day < 20):
        return 'Winter'
    else:
        return 'Invalid Date'


def is_valid(month, day):
    max_date = {
        "January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,
        "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31
    }

    month = month.capitalize()

    if month not in max_date:
        print('Error: Invalid month.')
        return False

    if 1 <= day <= max_date[month]:
        return True
    else:
        print(f"Error: {month} does not have {day} days.")
        return False


def main():
    while True:

        month = input('Enter month of the year: ').strip()
        try:
            day = int(input('Enter the day: '))

            if is_valid(month, day):
                season = name_the_season(month, day)
                print(f'The season on {month} {day} is: {season}')
                break
            else:
                print("Please enter a valid date.")

        except ValueError:
            print('Error: Please enter a valid integer for the day.')


if __name__ == '__main__':
    main()
