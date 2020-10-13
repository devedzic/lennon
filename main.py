# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# # Hello world: the print() built-in function and the + operator
# print('John Lennon')
# print('John Lennon' + ' was born in 1940.')
# print('John Lennon', 'was born in 1940.')
# print()
# print('John Lennon', 'was born in 1940.' + '\nHe was the greatest musician ever.')
# print('John Lennon', 'was born in', str(1940) + '.' + '\nHe was the greatest musician ever.')

# # The input() built-in function
# print('Enter John\'s full name: ', end='')
# john = input()
# print(john)
# print()
#
# john = input('Enter John\'s full name: ')       # no end='', the input happens at the end of the prompt
# print(john)

# # A simple function and function call
# def show_birth_year():
#     """John Lennon's birth year.
#     """
#
#     print('John Lennon\'s birth year')
#     # birth_year = input('The year: ')
#     birth_year = int(input('The year: '))
#     print(type(birth_year))
#     # print(f'John Lennon\'s birth year is {birth_year}.')
#     # print(f'John Lennon\'s birth year is', birth_year, '.')
#     print(f'John Lennon\'s birth year is', str(birth_year) + '.')
#
#
# show_birth_year()

# # A simple loop and the range() built-in function
# print(range(10))
# for i in range(10):
#     print(i)
# print(', '.join(str(x) for x in range(10)))

# # A simple list, accessing list elements, printing lists
# theBeatles = ['John', 'Paul', 'George', 'Ringo']
# print(theBeatles)
# print(theBeatles[0])
# print(', '.join(theBeatles))
# print()
#
# # Looping through list elements - for and enumerate()
# for beatle in theBeatles:
#     print(beatle)
# print()
# for i in range(len(theBeatles)):
#     print(theBeatles[i])
# print()
# print(enumerate(theBeatles))
# print(list(enumerate(theBeatles)))
# for i, v in list(enumerate(theBeatles)):
#     print(str(i + 1) + ':', v)

# Global variables: __name__, __file__, __doc__,...

from python import inception
inception.show_birth_year()
