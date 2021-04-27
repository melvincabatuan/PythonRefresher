r'''
              ___________________________________________________
            /                                                    \
           |    _____________________________________________     |
           |   |                                             |    |
           |   |  >>> _                                      |    |
           |   |                                             |    |
           |   |             Python Refresher V              |    |
           |   |                                             |    |
           |   |                    for                      |    |
           |   |                                             |    |
           |   |                  Learners                   |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                     by                      |    |
           |   |                                             |    |
           |   |                     MKC                     |    |
           |   |_____________________________________________|    |
           |                                                      |
            \_____________________________________________________/
                   \_______________________________________/
                _______________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_
:-----------------------------------------------------------------------------:
`---._.-----------------------------------------------------------------._.---'


           ___   _      _              _    _
          / _ \ | |__  (_)  ___   ___ | |_ (_)__   __ ___  ___
         | | | || '_ \ | | / _ \ / __|| __|| |\ \ / // _ \/ __|
         | |_| || |_) || ||  __/| (__ | |_ | | \ V /|  __/\__ \
          \___/ |_.__/_/ | \___| \___| \__||_|  \_/  \___||___/
                     |__/


        • To review list data structure in Python and its operations:
          - append
          - clear
          - copy
          - count
          - extend
          - index
          - insert
          - pop
          - remove
          - reverse
          - sort

        • To familiarize 1-D list comprehension and compare it with
          the traditional list accumulation.

        • To review tuples or an ordered immutable collection of
          objects.






                          _      _       _
                         | |    (_) ___ | |_
                         | |    | |/ __|| __|
                         | |___ | |\__ \| |_
                         |_____||_||___/ \__|

          ordered mutable collection of (heterogenuous) objects

                0 first item
                1 second item
                2 third item
                ....




                    _____               _
                   |_   _|_   _  _ __  | |  ___
                     | | | | | || '_ \ | | / _ \
                     | | | |_| || |_) || ||  __/
                     |_|  \__,_|| .__/ |_| \___|
                                |_|
              ordered immutable collection of objects

                0 first item
                1 second item
                2 third item
                ....





========================================================================
Drill 1-0 Use help() to enumerate the Python list operations.
========================================================================
'''






r'''
                                              _   __  __
         __ _  _ __   _ __    ___  _ __    __| | / /  \ \
        / _` || '_ \ | '_ \  / _ \| '_ \  / _` || |    | |
       | (_| || |_) || |_) ||  __/| | | || (_| || |    | |
        \__,_|| .__/ | .__/  \___||_| |_| \__,_|| |    | |
              |_|    |_|                         \_\  /_/
              Append object to the end of the list.

========================================================================
Creating Lists and accessing elements

Drill 1-1 a) Create an empty list and append new items to it.


          b) Create a list of objects with [] notation and
             append new items to it.


          c) Create a list of numbers using the range() function



          d) Create a function that returns a list of integers
             from 0 to n. The number n must be a user input.






          e) Create a function that accepts a list of integers and
             returns a list of the squares of the given elements.






          f) Create a function that accepts a number and
             returns the sum of its digits.







          g) Create a function that accepts a string and
             returns a list of its characters.




          e) Create a function that accepts a list of integers and
             returns a list of even squares of the given elements.


========================================================================
'''


def number_sequence1():
  '''
  Returns a list of integers from 0 to n (inclusive).
  The number n must be a user input.
  '''
  n = int(input("Enter an integer: "))
  return list(range(n + 1))


def number_sequence2():
  '''
  Returns a list of integers from 0 to n (inclusive).
  The number n must be a user input.
  '''
  n = int(input("Enter an integer: "))
  result = []
  for i in range(n + 1):
    result.append(i)
  return result


def number_sequence3():
  '''
  Returns a list of integers from 0 to n (inclusive).
  The number n must be a user input.
  Using list comprehension: [expression for loop (if condition)]
  '''
  n = int(input("Enter an integer: "))
  return [i for i in range(n + 1)] # list comprehension



def squares1(input_list):
  '''
  Returns a list of the squares of the given elements
  '''
  result = []
  for i in input_list:
    result.append(i**2)
  return result




def squares2(input_list):
  '''
  Returns a list of the squares of the given elements
  '''
  return [i**2 for i in input_list]



def sum_digits1(n):
  '''
  Returns the sum of its digits of n
  '''
  total = 0
  while n > 0:
    total += n%10
    n //= 10
  return total


def sum_digits2(n):
  '''
  Returns the sum of its digits of n
  '''
  return sum(map(int, list(str(n))))


def convert2list(input_string):
  '''
  Returns a list of its characters.
  '''
  return list(input_string)



def even_squares1(input_list):
  '''
  Returns a list of the even squares of the given elements
  '''
  result = []
  for i in input_list:
    if (i**2) % 2 == 0:
      result.append(i**2)
  return result


def even_squares2(input_list):
  '''
  Returns a list of the even squares of the given elements
  (Using list comprehension)
  '''
  #    expression      for-loop         condition
  return [i**2 for i in input_list if (i**2) % 2 == 0]



r'''
                      _                      __  __
                 ___ | |  ___   __ _  _ __  / /  \ \
                / __|| | / _ \ / _` || '__|| |    | |
               | (__ | ||  __/| (_| || |   | |    | |
                \___||_| \___| \__,_||_|   | |    | |
                                            \_\  /_/
                     Remove all items from list.

========================================================================
Drill 1-2 a) Use clear() operation to empty the list above.
          b) Differentiate clear() operation with del in Python.
========================================================================
'''

# numbers = [1,2,3]
# print(numbers)
# del numbers
# numbers.append(99)
# print(numbers)





r'''
                                           __  __
                 ___  ___   _ __   _   _  / /  \ \
                / __|/ _ \ | '_ \ | | | || |    | |
               | (__| (_) || |_) || |_| || |    | |
                \___|\___/ | .__/  \__, || |    | |
                           |_|     |___/  \_\  /_/
                Return a shallow copy of the list.

========================================================================
Drill 1-3 Differentiate shallow vs deep copy in Python.
          Hint: Shallow copies the references to elements
          Documentation: docs.python.org/3/library/copy.html
========================================================================
'''

# import copy

# list1 = [['a','b','c'],2,3]
# list2 = list1.copy() # ShALLOW COPY
# list3 = copy.deepcopy(list1)
# print('id1=', id(list1[0]), 'id2=', id(list2[0]), 'id3=', id(list3[0]))







r'''
                                          _     __  __
                 ___  ___   _   _  _ __  | |_  / /  \ \
                / __|/ _ \ | | | || '_ \ | __|| |    | |
               | (__| (_) || |_| || | | || |_ | |    | |
                \___|\___/  \__,_||_| |_| \__|| |    | |
                                               \_\  /_/
                Return number of occurrences of value.

========================================================================
Drill 1-4 Use count to return the number of occurrences of an
          item in a list.
========================================================================
'''


r'''
                      _                    _   __  __
           ___ __  __| |_  ___  _ __    __| | / /  \ \
          / _ \\ \/ /| __|/ _ \| '_ \  / _` || |    | |
         |  __/ >  < | |_|  __/| | | || (_| || |    | |
          \___|/_/\_\ \__|\___||_| |_| \__,_|| |    | |
                                              \_\  /_/
          Extend list by appending elements from the iterable.

========================================================================
Drill 1-5 Use extend() to append elements from the iterable.
========================================================================
'''








r'''
              _             _               __  __
             (_) _ __    __| |  ___ __  __ / /  \ \
             | || '_ \  / _` | / _ \\ \/ /| |    | |
             | || | | || (_| ||  __/ >  < | |    | |
             |_||_| |_| \__,_| \___|/_/\_\| |    | |
                                           \_\  /_/
                Return first index of value.
          Raises ValueError if the value is not present.

========================================================================
Drill 1-6 Use index to check the indices of list elements.
========================================================================
'''







r'''
              _                          _     __  __
             (_) _ __   ___   ___  _ __ | |_  / /  \ \
             | || '_ \ / __| / _ \| '__|| __|| |    | |
             | || | | |\__ \|  __/| |   | |_ | |    | |
             |_||_| |_||___/ \___||_|    \__|| |    | |
                                              \_\  /_/
                    Insert object before index.

========================================================================
Drill 1-7 Insert an element in a list.
========================================================================
'''





r'''
                                        __  __
                  _ __    ___   _ __   / /  \ \
                 | '_ \  / _ \ | '_ \ | |    | |
                 | |_) || (_) || |_) || |    | |
                 | .__/  \___/ | .__/ | |    | |
                 |_|           |_|     \_\  /_/
                Remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range.

========================================================================
Drill 1-8 Demonstrate the default pop() and pop using  index.
========================================================================
'''






r'''
                                                   __  __
          _ __  ___  _ __ ___    ___ __   __ ___  / /  \ \
         | '__|/ _ \| '_ ` _ \  / _ \\ \ / // _ \| |    | |
         | |  |  __/| | | | | || (_) |\ V /|  __/| |    | |
         |_|   \___||_| |_| |_| \___/  \_/  \___|| |    | |
                                                  \_\  /_/
                Remove first occurrence of value.
          Raises ValueError if the value is not present.

========================================================================
Drill 1-9 Remove an element from the list.
========================================================================
'''




r'''
                                                 __  __
        _ __  ___ __   __ ___  _ __  ___   ___  / /  \ \
       | '__|/ _ \\ \ / // _ \| '__|/ __| / _ \| |    | |
       | |  |  __/ \ V /|  __/| |   \__ \|  __/| |    | |
       |_|   \___|  \_/  \___||_|   |___/ \___|| |    | |
                                                \_\  /_/
                  Reverse *IN PLACE*.

========================================================================
Drill 1-10 Reverse a list of numbers.
========================================================================
'''








r'''
                                    _     __  __
                  ___   ___   _ __ | |_  / /  \ \
                 / __| / _ \ | '__|| __|| |    | |
                 \__ \| (_) || |   | |_ | |    | |
                 |___/ \___/ |_|    \__|| |    | |
                                         \_\  /_/
                    Stable sort *IN PLACE*.

========================================================================
Drill 1-11 Sort a list of numbers.
========================================================================
'''


r'''

          ___   ___   __ _  _   _   ___  _ __    ___  ___
         / __| / _ \ / _` || | | | / _ \| '_ \  / __|/ _ \
         \__ \|  __/| (_| || |_| ||  __/| | | || (__|  __/
         |___/ \___| \__, | \__,_| \___||_| |_| \___|\___|
                        |_|
========================================================================
Drill 1-12 Review the list operations of a list.
          - Indexing
          - Slicing
          - Membership
          - Concatenation
          - Length
          - Iteration
          - Summation
          - Unpacking
          - Repetition
          - Sorting
========================================================================
'''





r'''
========================================================================
Drill 1-13 Implement a Python function that accepts an positive integer
and returns a list of strings that resembles binary counting starting
from zero up to the input number. A non-positive input integer must
return an empty list.
e.g. binary_counter(3) == ["0", "1", "10", "11"]
     binary_counter(0) == ["0"]
     binary_counter(-2) == []
========================================================================
'''

def binary_counter(n):
  '''
  Returns a list of strings that resembles binary counting starting
  from zero up to the input number.
  '''

  if type(n) is not int:
    raise TypeError("Please input an integer")
  if n < 0:
    return []
  else:
    return [bin(i)[2:] for i in range(n+1)]


def binary_counter2(n):
  '''
  Returns a list of strings that resembles binary counting starting
  from zero up to the input number.
  '''

  if type(n) is not int:
    raise TypeError("Please input an integer")

  result = []
  if n >= 0:
    for i in range(n+1):
      result.append(bin(i)[2:])
  return result



r'''
========================================================================
Drill 1-14  Given a positive n-digit number, write a Python function
that will return its rearranged digits such that the value of digits
are in descending order from left to right. For example, 87976 returns
98776 and 6740 returns 7640. Note: No import is allowed for this
problem.
========================================================================
'''

def numtomaxn(n):
    """This function rearranges the digits of a number to
       its maximum value possible
    """
    if type(n) is not int:
        raise TypeError("Input an integer only")
    digits = []
    while n > 0:
      digits.append(n%10)
      n //= 10
    digits.sort(reverse=True)
    result = 0
    for digit in digits:
      result += digit
      result *= 10
    return result//10



def numtomaxn2(n):
    """This function rearranges the digits of a number to
       its maximum value possible
    """
    if type(n) is not int:
        raise TypeError("Input an integer only")
    digits = list(str(n))
    digits.sort(reverse=True)
    return int(''.join(digits))





r'''
========================================================================
Drill 1-15   Create a Python function that returns a list of strings
that resembles a pyramidal shape if printed line-by-line, composed of
the two characters specified by its arguments. It must accept the
number of lines to generate, the character to display on the left
half of a single line and the character to display on the right
half of the same line. For example, if the input requires 5 lines
with the characters "[" and "]" to be displayed on the left and
right respectively for each line, the output returns a list
as shown below:

['    []    ', '   [[]]   ', '  [[[]]]  ', ' [[[[]]]] ', '[[[[[]]]]]']

or

print(generate_triangle(5, "{", "}"))

['    {}    ',   # 0
 '   {{}}   ',   # 1
 '  {{{}}}  ',
 ' {{{{}}}} ',
 '{{{{{}}}}}']

print(generate_triangle(5, "{", "8"))
['    {8    ',
 '   {{88   ',
 '  {{{888  ',
 ' {{{{8888 ',
 '{{{{{88888']
========================================================================
'''

def generate_triangle(n, left="/", right="\\"):
    """This function generates a list of strings which
       when printed resembles a triangle
    """
    if type(n) is not int:
        raise TypeError("Input an integer only")
    result = []
    for i in range(1, n+1):
      line = ' '*(n-i) + left*i + right*i + ' '*(n-i)
      result.append(line)
    return result


# print()
# for line in generate_triangle(10, "0", "]"):
#   print(line)





# my_list = ['a','b', 'c']

# for char in my_list:
#   print(char)
#   my_list.append('z')
#   DO NOT MODIFY THE OBJECT YOU ARE ITERATING
