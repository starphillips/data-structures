''' Exercise 7: Name that Shape
Write a program that determines the name of a shape from its number of sides. Read the
number of sides from the user and then report the appropriate name as part of a
meaningful message. Your program should support shapes with anywhere from 3 up to (and
including) 10 sides. If a number of sides outside of this range is entered then your program
should display an appropriate error message. '''


def shape_name(shape_sides):
    if shape_sides == 1:
        shape_is = 'Circle'
    elif shape_sides == 2:
        shape_is = 'Digon'
    elif shape_sides == 3:
        shape_is = 'Triangle'
    elif shape_sides == 4:
        shape_is = 'Square'
    elif shape_sides == 5:
        shape_is = 'Pentagon'
    elif shape_sides == 6:
        shape_is = 'Hexagon'
    elif shape_sides == 7:
        shape_is = 'Septagon'
    elif shape_sides == 8:
        shape_is = 'Hexagon'
    elif shape_sides == 9:
        shape_is = 'Nonagon'
    elif shape_sides == 10:
        shape_is = 'Decagon'
    return f'A shape with {shape_sides} sides would be a {shape_is}'


def main():
    try:
        shape_sides = int(input('Enter the number of sides your shape has: '))

        final = shape_name(shape_sides)

        print(final)

    except ValueError:
        print('Invalid input. Please enter an integer.')


if __name__ == '__main__':
    main()
