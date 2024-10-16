''' Exercise 7: Name that Shape
Write a program that determines the name of a shape from its number of sides. Read the
number of sides from the user and then report the appropriate name as part of a
meaningful message. Your program should support shapes with anywhere from 3 up to (and
including) 10 sides. If a number of sides outside of this range is entered then your program
should display an appropriate error message. '''


def shape_name(shape_sides):
    shapes = {
        3: 'Triangle',
        4: 'Quadrilateral',
        5: 'Pentagon',
        6: 'Hexagon',
        7: 'Septagon',
        8: 'Octagon',
        9: 'Nonagon',
        10: 'Decagon'
    }
    # Return shapes, if no key is given, return string
    return shapes.get(shape_sides, 'Invalid Shape')


def main():
    # Allow user to enter again if they have inputted an invalid integer
    while True:
        try:
            shape_sides = int(
                input('Enter the number of sides your shape has (between 3-10): '))

            if shape_sides < 3 or shape_sides > 10:
                print('Error: value entered must be between 3 and 10')

            else:
                final_shape_name = shape_name(shape_sides)
                print(
                    f'A shape with {shape_sides} sides would be a {final_shape_name}')
                break

        except ValueError:
            print('Invalid input. Please enter an integer.')


if __name__ == '__main__':
    main()
