r'''
              ___________________________________________________
            /                                                    \
           |    _____________________________________________     |
           |   |                                             |    |
           |   |  >>> _                                      |    |
           |   |                                             |    |
           |   |             Python Refresher IV             |    |
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


        • To familiarize and utilize the Python range object and
          generate a sequence.

        • To review sequences and iteration along with their
          basic operations:

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

        • To apply the aforementioned operations in string (immutable),
          lists (mutable), and tuple (immutable) data types.

        • To create functions with parameters and return values.







          ____
         / ___|   ___   __ _  _   _   ___  _ __    ___  ___
         \___ \  / _ \ / _` || | | | / _ \| '_ \  / __|/ _ \
          ___) ||  __/| (_| || |_| ||  __/| | | || (__|  __/
         |____/  \___| \__, | \__,_| \___||_| |_| \___|\___|
                          |_|
          a sequence is an enumerated collection of objects
          in which repetitions are allowed and order matters











                                               ____
              _ __  __ _  _ __    __ _   ___  / /\ \
             | '__|/ _` || '_ \  / _` | / _ \| |  | |
             | |  | (_| || | | || (_| ||  __/| |  | |
             |_|   \__,_||_| |_| \__, | \___|| |  | |
                                 |___/        \_\/_/
                    range(start, stop[, step])
        Return an object that produces a sequence of integers
        from start (inclusive) to stop (exclusive) by step.



========================================================================
Drill 1-0 Using both (while) iteration and range object, generate the ff.:
          a) a sequence of integers, 1 to 10.
          b) a sequence of even integers, 1 to 10.
          c) a sequence of odd integers, 1 to 10.
          d) a sequence of integers, 10 to 1.
========================================================================
'''
### USING WHILE

## a sequence of integers, 1 to 10.

# count = 1
# while count <= 10:
#   print(count)
#   count += 1

## a sequence of even integers, 1 to 10.

# count = 2
# while count <= 10:
#   print(count)
#   count += 2


## a sequence of odd integers, 1 to 10.
# count = 1
# while count <= 10:
#   print(count)
#   count += 2

## a sequence of odd integers, 1 to 10. (Alternative)
# count = 1
# while count <= 10:
#   if count%2:
#     print(count)
#   count += 1


## a sequence of integers, 10 to 1.
# count = 10
# while count >= 1:
#   print(count)
#   count -= 1


### USING RANGE OBJECT

## a sequence of integers, 1 to 10.

# for i in range(1, 10+1):
#   print(i)


# a sequence of even integers, 1 to 10.
# for i in range(2, 10+1, 2):
#   print(i)


## a sequence of odd integers, 1 to 10.
# for i in range(1, 10+1, 2):
#   print(i)


## a sequence of integers, 10 to 1.
# for i in range(10, 0, -1):
#   print(i)

# Alternative method
# for i in reversed(range(1, 10+1)):
#   print(i)




#
# DEFINITION
def greet():
  print("Hello")



def add2num(first_number, second_number):
  print("START OF FUNCTION")
  return first_number + second_number
  print("END OF FUNCTION")


# total = add2num(1,2)
# print(total)



r'''
                                                    _   ____
        _ __  ___ __   __ ___  _ __  ___   ___   __| | / /\ \
       | '__|/ _ \\ \ / // _ \| '__|/ __| / _ \ / _` || |  | |
       | |  |  __/ \ V /|  __/| |   \__ \|  __/| (_| || |  | |
       |_|   \___|  \_/  \___||_|   |___/ \___| \__,_|| |  | |
                                                       \_\/_/




                             _
                  _ __  ___ | |_  _   _  _ __  _ __
                 | '__|/ _ \| __|| | | || '__|| '_ \
                 | |  |  __/| |_ | |_| || |   | | | |
                 |_|   \___| \__| \__,_||_|   |_| |_|

                end the execution of the function call
                          return the result

========================================================================
Drill 1-1 Using both (while) iteration and range object, create functions
          that generate and return a list of each of the ff.:
          a) a sequence of integers, 1 to 10.
          b) a sequence of even integers, 1 to 10.
          c) a sequence of odd integers, 1 to 10.
          d) a sequence of integers, 10 to 1.

          Create a function that computes the sum and average of
          the sequence.
========================================================================
'''

# ACCUMULATION

def sequence_1to10_while():
  '''
  Returns a sequence of integers, 1 to 10 (using while).
  '''
  count = 1
  result = []
  while count <= 10:
    # print(count)
    result.append(count)
    count += 1
  return result


# print(sequence_1to10_while())

def sequence_1to10_range():
  '''
  Returns a sequence of integers, 1 to 10 (using range).
  '''
  return list(range(1,10+1))

# print(sequence_1to10_range())



def even_1to10_while():
  '''
  Returns a sequence of even integers, 1 to 10 (using while).
  '''
  count = 2
  result = []
  while count <= 10:
    # print(count)
    result.append(count)
    count += 2
  return result

# print(sequence_1to10_while())


def even_1to10_range():
  '''
  Returns a sequence of even integers, 1 to 10 (using range).
  '''
  return list(range(2, 10+1, 2))


# print(even_1to10_range())




def odd_1to10_while():
  '''
  Returns a sequence of odd integers, 1 to 10 (using while).
  '''
  count = 1
  result = []
  while count <= 10:
    # print(count)
    result.append(count)
    count += 2
  return result

# print(odd_1to10_while())



def odd_1to10_range():
  '''
  Returns a sequence of odd integers, 1 to 10 (using range).
  '''
  return list(range(1, 11, 2))

# print(odd_1to10_range())


def sequence_10to1_while():
  '''
  Returns a sequence of integers, 1 to 10 (using while).
  '''
  count = 10
  result = []
  while count > 0:
    result.append(count)
    count -= 1
  return result


# print(sequence_10to1_while())


def sequence_10to1_range():
  '''
  Returns a sequence of integers, 1 to 10 (using range).
  '''
  return list(range(10,0,-1))

# print(sequence_10to1_range())




def compute_sum(sequence):
  '''
  Computes the sum of the elements in the sequence
  '''
  total = 0
  for i in sequence:
    total += i
  return total

# my_sequence = sequence_10to1_range()
# print(compute_sum(my_sequence))
# print(sum(my_sequence))


def average(sequence):
  '''
  Returns the mean of sequence elements
  '''
  return sum(sequence)/len(sequence)


# my_sequence = sequence_10to1_range()
# print(average(my_sequence))




r'''
                      _  _       _     ____
                     | |(_) ___ | |_  / /\ \
                     | || |/ __|| __|| |  | |
                     | || |\__ \| |_ | |  | |
                     |_||_||___/ \__|| |  | |
                                      \_\/_/

          sequence - enumerated collection of objects,
          mutable, heterogeneous container of elements

========================================================================
Drill 1-2 Demonstrate the ff. basic sequence operations in a list:
          - Indexing ([+]/[-])
          - Slicing ([lower:upper])
          - Membership (in)
          - Concatenation (+)
          - Length (len)
          - Iteration (for + in)
          - Summation (sum)(limited to numbers, i.e. int float)
          - Unpacking (=)
          - Repetition (*)
          - Sorting (sorted)
========================================================================
'''







r'''
            _                  _         ____
           | |_  _   _  _ __  | |  ___  / /\ \
           | __|| | | || '_ \ | | / _ \| |  | |
           | |_ | |_| || |_) || ||  __/| |  | |
            \__| \__,_|| .__/ |_| \___|| |  | |
                       |_|              \_\/_/
          sequence - enumerated collection of objects,
          immutable, heterogeneous container of elements

========================================================================
Drill 1-3 Demonstrate the ff. basic sequence operations in a tuple():
          - Indexing (+/-)
          - Slicing (upper:lower)
          - Membership (in)
          - Concatenation (+)
          - Length (len)
          - Iteration (for + in)
          - Summation (sum)
          - Unpacking (=)
          - Repetition (*)
          - Sorting (sorted)
========================================================================
'''

# YOUR CODE HERE








r'''
========================================================================
Drill 1-4 Which of the following sequence operations can be performed
          to a range object?
          - Indexing (+/-)
          - Slicing (upper:lower)
          - Membership (in)
          - Concatenation (+)
          - Length (len)
          - Iteration (for + in)
          - Summation (sum)
          - Unpacking (=)
          - Repetition (*)
          - Sorting (sorted)
========================================================================
'''










r'''
                       _           ____
                  ___ | |_  _ __  / /\ \
                 / __|| __|| '__|| |  | |
                 \__ \| |_ | |   | |  | |
                 |___/ \__||_|   | |  | |
                                  \_\/_/

                         String
        sequence - enumerated collection of characters,
                       immutable

========================================================================
Drill 1-5 Demonstrate the supported sequence operations in a string:
          - Indexing (+/-)
          - Slicing (upper:lower)
          - Membership (in)
          - Concatenation (+)
          - Length (len)
          - Iteration (for + in)
          - Summation (sum)
          - Unpacking (=)
          - Repetition (*)
          - Sorting (sorted)
========================================================================
'''

# YOUR CODE HERE








r'''
========================================================================
Drill 1-6 Write a Python program that prints the following box pattern:
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height and width as function input parameters

e.g. 50x5 box

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
========================================================================
'''

import random
import string

def put_char():
  '''
  Returns a random uppercase letter (Refer to Refresher II)
  '''
  return random.choice(string.ascii_uppercase)


def box(width, height):
  '''
  Prints the box pattern
  '''
  print()
  for row in range(height):
    print(put_char() * width) # repetition


# Call with parameters
# box(40, 10)




r'''
========================================================================
Drill 1-7 Write a Python program that prints the following hollow box
pattern:
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height and width as function input parameters
========================================================================
e.g.

          GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
          K                                      K
          H                                      H
          A                                      A
          Z                                      Z
          X                                      X
          Z                                      Z
          E                                      E
          D                                      D
          IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

========================================================================
'''

def hollow_box(width, height):
  '''
  Prints the  hollow box pattern
  '''
  print()
  for row in range(height):
    if row > 0 and row < height - 1:
      print(put_char() + ' '*(width-2) + put_char())
    else:
      print(put_char() * width)


# hollow_box(40, 5)


r'''
========================================================================
Drill 1-8 Write a Python program that prints the following right triangle
pattern:
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height as function input parameter
========================================================================
e.g. height = 10

J
AA
WWW
XXXX
NNNNN
KKKKKK
PPPPPPP
LLLLLLLL
BBBBBBBBB
CCCCCCCCCC
========================================================================
'''



def right_triangle_L(height):
  '''
  Prints right triangle with L-like pattern
  '''
  print()
  for row in range(1, height+1):
    print(put_char()*row)


# right_triangle_L(5)

r'''
========================================================================
Drill 1-9 Write a Python program that prints the following hollow right
triangle pattern:
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height as function input parameter
========================================================================
e.g. height = 10
  I
  EE
  F F
  U  U
  N   N
  D    D
  Y     Y
  W      W
  K       K
  YYYYYYYYYY
========================================================================
'''


def hollow_right_triangle_L(height):
  '''
  Prints hollow right triangle with L-like pattern
  '''
  print()
  for row in range(1, height+1):
    if row > 2 and row < height:
      print(put_char() + ' '*(row-2) + put_char())
    else:
      print(put_char()*row)


# hollow_right_triangle_L(10)


r'''
========================================================================
Drill 1-10 Write a Python program that prints the following inverted right
triangle pattern:
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height as function input parameter
========================================================================
e.g. height = 10

  EEEEEEEEEE
  AAAAAAAAA
  BBBBBBBB
  NNNNNNN
  XXXXXX
  OOOOO
  HHHH
  YYY
  OO
  K
========================================================================
'''


def inverted_right_triangle_L(height):
  '''
  Prints inverted right triangle with L-like pattern
  '''
  print()
  for row in reversed(range(1, height+1)):
    print(put_char()*row)


# inverted_right_triangle_L(10)

r'''
========================================================================
Drill 1-11 Write a Python program that prints the following inverted right
hollow triangle pattern:
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height as function input parameter
========================================================================

e.g. height = 10

  AAAAAAAAAA
  V       V
  F      F
  Y     Y
  U    U
  D   D
  K  K
  A A
  MM
  V
========================================================================
'''

def hollow_inverted_right_triangle_L(height):
  '''
  Prints hollow inverted right triangle with L-like pattern
  '''
  print()
  for row in reversed(range(1, height+1)):
    if row < height and row > 2:
      print(put_char() + ' '*(row-2) + put_char())
    else:
      print(put_char()*row)

# hollow_inverted_right_triangle_L(10)


r'''
========================================================================
Drill 1-12 Write a Python program that prints the following right triangle
pattern (right-side oriented).
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height as function input parameter
========================================================================
e.g. at h = 10:
         I
        PP
       YYY
      RRRR
     SSSSS
    UUUUUU
   FFFFFFF
  BBBBBBBB
 RRRRRRRRR
FFFFFFFFFF
'''


def right_triangle_rotated_L(height):
  '''
  Prints right triangle with rotated L-like pattern
  '''
  print()
  for row in range(1, height+1):
    print(' '*(height-row) + put_char()*row)

# right_triangle_rotated_L(10)






r'''
========================================================================
Drill 1-13 Write a Python program that prints the following hollow right
triangle pattern (right-side oriented).
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height as function input parameter
========================================================================
e.g. at h = 10:
         F
        HH
       G G
      J  J
     K   K
    Q    Q
   S     S
  R      R
 X       X
ZZZZZZZZZZ
'''


def hollow_right_triangle_rotated_L(height):
  '''
  Prints hollow right triangle with rotated L-like pattern
  '''
  print()
  for row in range(1, height+1):
    if row > 2 and row < height:
      print(' '*(height-row) + put_char() + ' '*(row-2) + put_char())
    else:
      print(' '*(height-row) + put_char()*row)


# hollow_right_triangle_rotated_L(10)

r'''
========================================================================
Drill 1-14 Write a Python program that prints the following pyramid pattern
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height as function input parameter
========================================================================
e.g. at h = 10:
          E
         QQQ
        YYYYY
       IIIIIII
      KKKKKKKKK
     JJJJJJJJJJJ
    DDDDDDDDDDDDD
   KKKKKKKKKKKKKKK
  WWWWWWWWWWWWWWWWW
 HHHHHHHHHHHHHHHHHHH
'''



def pyramid(height):
  '''
  Prints pyramid pattern
  '''
  print()
  for row in range(height):
    print(' '*(height-row) + put_char()*(2*row+1))


# pyramid(10)



r'''
========================================================================
Drill 1-15 Write a Python program that prints the following hollow
pyramid pattern.
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use height as function input parameter
========================================================================
e.g. at h = 10:
          P
         G F
        L   G
       J     E
      L       L
     X         F
    L           Q
   K             J
  Q               U
 NNNNNNNNNNNNNNNNNNN
'''



def hollow_pyramid(height):
  '''
  Prints pyramid pattern
  '''
  print()
  for row in range(height):
    if row > 0 and row < height - 1:
      print(' '*(height-row) + put_char() + ' '*(2*row-1) + put_char())
    else:
      print(' '*(height-row) + put_char()*(2*row+1))


# hollow_pyramid(5)


r'''
========================================================================
Drill 1-16 Write a Python program that prints the following diamond
pattern. Use h variable to denote the height to center.
- Use random and string module to generate random uppercase characters
- Use Python sequence operations
- Use h as function input parameter
========================================================================
e.g. at h = 6:
      O
     HHH
    LLLLL
   HHHHHHH
  WWWWWWWWW
 FFFFFFFFFFF
  NNNNNNNNN
   OOOOOOO
    ZZZZZ
     TTT
      D
'''

def diamond(height):
  '''
  Prints diamond pattern
  '''
  print()
  for row in range(height):
    print(' '*(height-row) + put_char()*(2*row+1))
  for row in reversed(range(height-1)):
    print(' '*(height-row) + put_char()*(2*row+1))



# diamond(6)



r'''
========================================================================
Drill 1-17 Write a Python program that prints the following hollow diamond
pattern. Use h variable to denote the height to center.
(Use random & string module to generate random uppercase characters)
========================================================================
e.g. at h = 5:
      R
     T W
    Y   G
   T     W
  V       R
   E     J
    T   G
     V E
      Y
'''


def hollow_diamond(height):
  '''
  Prints hollow diamond pattern
  '''
  print()
  for row in range(1, height+1):
    print(' '*(height-row) + put_char() + ' '*(2*row-3) + put_char()*(1%row))
  for row in reversed(range(1, height)):
    print(' '*(height-row) + put_char() + ' '*(2*row-3) + put_char()*(1%row))


# hollow_diamond(6)


r'''
========================================================================
A palindrome is a word, number, phrase, or other sequence of characters
which reads the same backward as forward such as the number 108801.
Write a Python function that accepts either an integer or string
and returns a tuple consisting of two possible palindromes that
can be made from the input sequence.
========================================================================
e.g.
to_palindrome(567) == (567765, 765567)
to_palindrome("Hello") == ("HelloolleH", "olleHHello")
to_palindrome("12345") ==  ("1234554321", "5432112345")
'''

def to_palindrome(seq):
    """
    Generates two possible palindromic sequence from the input sequence
    """
    init_type = type(seq)
    if not (init_type is str or init_type is int):
        raise TypeError("Input a string or integer only")

    if init_type == int:
      seq = str(seq)
    forward   = seq + seq[::-1]
    reverse   = seq[::-1] + seq
    return (forward, reverse) if init_type == str \
     else (int(forward), int(reverse))


# print(to_palindrome("Hello")) # okay

# print(to_palindrome(567))

print(to_palindrome("12345"))
