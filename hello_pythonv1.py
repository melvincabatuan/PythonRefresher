r'''
              ___________________________________________________
            /                                                    \`
           |    _____________________________________________     |
           |   |                                             |    |
           |   |  >>> _                                      |    |
           |   |                                             |    |
           |   |             Python Refresher I              |    |
           |   |                                             |    |
           |   |                    for                      |    |
           |   |                                             |    |
           |   |                 Learners                    |    |
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



      • To introduce or review Python as a general programming language,
        and print the "Zen of Python" or its guiding principles.



      • To write and run a simple Python program with print() function
        with output formatting and distinguish between interactive
        Python shell and .py file programs.




      • To introduce or review python introspection with type() and id()
        functions, and ask guidance with help() function.




      • To enumerate Python data types - scalar: integers (int),
        floating-point numbers (float), Boolean (bool), complex numbers,
        and Nonetype; and non-scalar data structures: sequences
        (e.g. lists, tuples), sets, and mappings (e.g. dictionaries).




      • To recall fundamental programming ideas - objects, variables,
        literals, assignments, interpreter, operators, comments,
        indentation, expressions, keywords, errors, and naming
        conventions - in the context of Python programming.




      • To learn how to import Python modules and be aware of
        miscellaneous features, i.e. special characters, and assignments
        operators, etc.




      • To describe and implement basic program control flow - branching
        , i.e. conditional statements; and iteration, i.e. while and
        for loops.






           ____  ___   __  __  ____   _   _  _____  _____  ____
          / ___|/ _ \ |  \/  ||  _ \ | | | ||_   _|| ____||  _ \
         | |   | | | || |\/| || |_) || | | |  | |  |  _|  | |_) |
         | |___| |_| || |  | ||  __/ | |_| |  | |  | |___ |  _ <
          \____|\___/ |_|  |_||_|     \___/   |_|  |_____||_| \_\

                         • performs calculations

                         • remembers the results






                  ____ __   __ _____  _   _   ___   _   _
                 |  _ \\ \ / /|_   _|| | | | / _ \ | \ | |
                 | |_) |\ V /   | |  | |_| || | | ||  \| |
                 |  __/  | |    | |  |  _  || |_| || |\  |
                 |_|     |_|    |_|  |_| |_| \___/ |_| \_|

                  • a general-purpose programming language

                  • high-level, interpreted, & open-source

                  • many libraries or modules are available









              _ __   _ __  ___    __ _  _ __  __ _  _ __ ___
             | '_ \ | '__|/ _ \  / _` || '__|/ _` || '_ ` _ \
             | |_) || |  | (_) || (_| || |  | (_| || | | | | |
             | .__/ |_|   \___/  \__, ||_|   \__,_||_| |_| |_|
             |_|                 |___/

                  a sequence of definitions and commands


                                   ▐M

                                   ▓▓

                         ▐""""""""""""""""""""╙M

                         ╠                     Ω

                         ╠                     Ω

                         Ñwwwwwwwwwwæwwwwwwwwww

                                   ▐K

                                   ██

                         e∞∞∞∞∞∞∞∞∞æ∞∞∞∞∞∞∞∞∞∞∞

                         ╠                     Ω

                         ╠                     Ω

                         ▐,,,,,,,,,,,,,,,,,,,,,Ω

                                   ▐C

                                   ██

                         ,¿¿¿¿¿¿¿¿¿å▄¿¿¿¿¿¿¿¿¿u

                         ╠                     Ω

                         ╠                     Ω

                         ▐,,,,,,,,,,,,,,,,,,,,,Ω

                                   ▐Ö

                                   ▐M

                                   ▓▓





          _         _                                 _
         (_) _ __  | |_  ___  _ __  _ __   _ __  ___ | |_  ___  _ __
         | || '_ \ | __|/ _ \| '__|| '_ \ | '__|/ _ \| __|/ _ \| '__|
         | || | | || |_|  __/| |   | |_) || |  |  __/| |_|  __/| |
         |_||_| |_| \__|\___||_|   | .__/ |_|   \___| \__|\___||_|
                                   |_|

                a program that reads and executes commands







                                                           _
              _ __  _   _  _ __     __ _    ___  ___    __| |  ___
             | '__|| | | || '_ \   / _` |  / __|/ _ \  / _` | / _ \
             | |   | |_| || | | | | (_| | | (__| (_) || (_| ||  __/
             |_|    \__,_||_| |_|  \__,_|  \___|\___/  \__,_| \___|

                • using the Python interpreter interactively

                • using an IDE (Integrated Development Environment)

                • run a .py file using the python command

                • run a .py file as a shell script

                       #!/usr/bin/env python






                      ____   _____  ____   _
                     |  _ \ | ____||  _ \ | |
                     | |_) ||  _|  | |_) || |
                     |  _ < | |___ |  __/ | |___
                     |_| \_\|_____||_|    |_____|

                            Python Shell

                        Read-Evaluate-Print Loop





                               _         _     __ __
                  _ __   _ __ (_) _ __  | |_  / / \ \
                 | '_ \ | '__|| || '_ \ | __|| |   | |
                 | |_) || |   | || | | || |_ | |   | |
                 | .__/ |_|   |_||_| |_| \__|| |   | |
                 |_|                          \_\ /_/

========================================================================
Drill 1-1 Write a Python program or script that prints "Hello, World!".
========================================================================

           ____                                           _
          / ___| ___   _ __ ___   _ __ ___    ___  _ __  | |_  ___
         | |    / _ \ | '_ ` _ \ | '_ ` _ \  / _ \| '_ \ | __|/ __|
         | |___| (_) || | | | | || | | | | ||  __/| | | || |_ \__ \
          \____|\___/ |_| |_| |_||_| |_| |_| \___||_| |_| \__||___/

               lines of code that serve as documentation
'''


r'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Python vs. C

#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++







                  _            _          __  __
                 | |__    ___ | | _ __   / /  \ \
                 | '_ \  / _ \| || '_ \ | |    | |
                 | | | ||  __/| || |_) || |    | |
                 |_| |_| \___||_|| .__/ | |    | |
                                 |_|     \_\  /_/

                         asking for help



========================================================================
Drill 1-2. a) Experiment to find out what happens when print's argument
string contains special characters.

\n - Newline (go to start of next line)
\t - Horizontal tab
\r - Carriage return (go to start of current line)
\b - Backspace
\f - Form feed (go to start of next page)
\' - Single Quote
\" - double quote
\\ - Backslash

b) Print the ff. special characters in Python: Ä á @ ? & * \ / ' '
========================================================================
'''





r'''
  _____                      __   ____          _    _
 |__  / ___  _ __     ___   / _| |  _ \  _   _ | |_ | |__    ___   _ __
   / / / _ \| '_ \   / _ \ | |_  | |_) || | | || __|| '_ \  / _ \ | '_ \
  / /_|  __/| | | | | (_) ||  _| |  __/ | |_| || |_ | | | || (_) || | | |
 /____|\___||_| |_|  \___/ |_|   |_|     \__, | \__||_| |_| \___/ |_| |_|
                                         |___/

========================================================================
Drill 1-3 Print the "Zen of Python" by Tim Peters in interactive shell.
========================================================================
'''







r'''
                   ___   _      _              _
                  / _ \ | |__  (_)  ___   ___ | |_  ___
                 | | | || '_ \ | | / _ \ / __|| __|/ __|
                 | |_| || |_) || ||  __/| (__ | |_ \__ \
                  \___/ |_.__/_/ | \___| \___| \__||___/
                             |__/

                   Object = Identity + Type + Value

        • All data in a Python program is represented by objects
                 or by relations between them.

        • Object’s identity never changes once it has been created.

        • Objects whose value can change are said to be mutable.

        • Objects whose value is unchangeable once they are created
                 are called immutable

        • An object can be associated to one, more than one, or no name.

            docs.python.org/3/reference/datamodel.html




          ____          _           _____
         |  _ \   __ _ | |_  __ _  |_   _|_   _  _ __    ___
         | | | | / _` || __|/ _` |   | | | | | || '_ \  / _ \
         | |_| || (_| || |_| (_| |   | | | |_| || |_) ||  __/
         |____/  \__,_| \__|\__,_|   |_|  \__, || .__/  \___|
                                          |___/ |_|

  • Either scalar (indivisible) or non-scalar having internal structure.



  • Scalar types include integers (int), floating-point numbers
    (float), Boolean values (bool), complex numbers, and Nonetype (None).




    • Non-scalar types include:



      a) Immutable sequences, i.e. strings, tuples, bytes





      b) Mutable sequences, i.e lists, and byte arrays






      c) Set types, i.e. sets and frozen sets






      d) Mappings, i.e. dictionaries







Note: There is no limit on the maximum value for Python int.

                  ___  _   _  ___
                 / __|| | | |/ __|
                 \__ \| |_| |\__ \
                 |___/ \__, ||___/
                       |___/

                    sys.maxsize
                    sys.version




  ___         _                                        _    _
 |_ _| _ __  | |_  _ __  ___   ___  _ __    ___   ___ | |_ (_)  ___   _ __
  | | | '_ \ | __|| '__|/ _ \ / __|| '_ \  / _ \ / __|| __|| | / _ \ | '_ \
  | | | | | || |_ | |  | (_) |\__ \| |_) ||  __/| (__ | |_ | || (_) || | | |
 |___||_| |_| \__||_|   \___/ |___/| .__/  \___| \___| \__||_| \___/ |_| |_|
                                   |_|

            ability to get the type of an object at runtime


              _                         __ __
             | |_  _   _  _ __    ___  / / \ \
             | __|| | | || '_ \  / _ \| |   | |
             | |_ | |_| || |_) ||  __/| |   | |
              \__| \__, || .__/  \___|| |   | |
                   |___/ |_|           \_\ /_/

                      _  _         __  __
                   __| |(_) _ __  / /  \ \
                  / _` || || '__|| |    | |
                 | (_| || || |   | |    | |
                  \__,_||_||_|   | |    | |
                                  \_\  /_/

========================================================================
Drill 1-4 Print examples of each Python data types and use type() method.
========================================================================
'''




r'''


                _  _  _                     _
               | |(_)| |_  ___  _ __  __ _ | | ___
               | || || __|/ _ \| '__|/ _` || |/ __|
               | || || |_|  __/| |  | (_| || |\__ \
               |_||_| \__|\___||_|   \__,_||_||___/

               values recognized by language parser





         __     __            _         _      _
         \ \   / /__ _  _ __ (_)  __ _ | |__  | |  ___  ___
          \ \ / // _` || '__|| | / _` || '_ \ | | / _ \/ __|
           \ V /| (_| || |   | || (_| || |_) || ||  __/\__ \
            \_/  \__,_||_|   |_| \__,_||_.__/ |_| \___||___/

               a symbolic name that reference an object.
                          access + context





         _               _                                        _
        / \    ___  ___ (_)  __ _  _ __   _ __ ___    ___  _ __  | |_
       / _ \  / __|/ __|| | / _` || '_ \ | '_ ` _ \  / _ \| '_ \ | __|
      / ___ \ \__ \\__ \| || (_| || | | || | | | | ||  __/| | | || |_
     /_/   \_\|___/|___/|_| \__, ||_| |_||_| |_| |_| \___||_| |_| \__|
                            |___/

                         identifier = value

                  Python allows multiple assignment

              identifier1, identifier2 = value1, value2


========================================================================
Drill 1-5 Declare variables for each Python data types and print each.
========================================================================
'''





r'''
   ____                                 _    _
  / ___| ___   _ __ __   __ ___  _ __  | |_ (_)  ___   _ __   ___
 | |    / _ \ | '_ \\ \ / // _ \| '_ \ | __|| | / _ \ | '_ \ / __|
 | |___| (_) || | | |\ V /|  __/| | | || |_ | || (_) || | | |\__ \
  \____|\___/ |_| |_| \_/  \___||_| |_| \__||_| \___/ |_| |_||___/

                            lowercase

          more descriptive than short names i.e. a or b

        individual words separated by underscores (snake_case)

             e.g. user_name, is_correct, and so on

            a = 3.14159              pi = 3.14159
            b = 11.2         vs.     radius = 11.2
            c = a*(b**2)             area = pi*(radius **2)





          _  __                                      _
         | |/ / ___  _   _ __      __ ___   _ __  __| | ___
         | ' / / _ \| | | |\ \ /\ / // _ \ | '__|/ _` |/ __|
         | . \|  __/| |_| | \ V  V /| (_) || |  | (_| |\__ \
         |_|\_\\___| \__, |  \_/\_/  \___/ |_|   \__,_||___/
                     |___/

                          Python keywords











       ___                            _
      / _ \  _ __    ___  _ __  __ _ | |_  ___   _ __  ___
     | | | || '_ \  / _ \| '__|/ _` || __|/ _ \ | '__|/ __|
     | |_| || |_) ||  __/| |  | (_| || |_| (_) || |   \__ \
      \___/ | .__/  \___||_|   \__,_| \__|\___/ |_|   |___/
            |_|

         special symbols for computation or comparison

         • Arithmetic - addition (+), subtraction (-), multiplication
          (*), division (/), floor/integer division (//),
          exponentiation (**)








         • Comparison - greater than (>), less than (<), equal to (==),
           not equal to (!=), greater than or equal to (>=), and less
           than or equal to (<=).







        • Logical - conjunction (and), disjunction (or), and
          negation (not)








        • Bitwise - AND (&), OR (|), NOT (~), XOR (^), right shift (>>)
          , and left shift (<<)









Note: Python Enhancement Proposal (PEP) 8 recommends separating both
      operands from an operator with a space.

      e.g.  a*b  vs  a * b












            _   _                     _____
           | \ | |  ___   _ __    ___|_   _|_   _  _ __    ___
           |  \| | / _ \ | '_ \  / _ \ | | | | | || '_ \  / _ \
           | |\  || (_) || | | ||  __/ | | | |_| || |_) ||  __/
           |_| \_| \___/ |_| |_| \___| |_|  \__, || .__/  \___|
                                            |___/ |_|

                                None

                             nothingness









                            _      __   ___
                           / |    / /  / _ \
                           | |   / /  | | | |
                           | |  / /   | |_| |
                           |_| /_/     \___/

                   ZeroDivisionError: division by zero
                            _   _  __   ___
                           / | (_)/ /  / _ \
                           | |   / /  | | | |
                           | |  / /_  | |_| |
                           |_| /_/(_)  \___/








                   ___     _            ___     ____
                  / _ \   / |    _     / _ \   |___ \
                 | | | |  | |  _| |_  | | | |    __) |
                 | |_| |_ | | |_   _| | |_| |_  / __/
                  \___/(_)|_|   |_|    \___/(_)|_____|

                   floating-point representation error


========================================================================
Drill 1-6 Give examples for each operators.
========================================================================
'''




r'''
              _                                 _
             (_) _ __ ___   _ __    ___   _ __ | |_
             | || '_ ` _ \ | '_ \  / _ \ | '__|| __|
             | || | | | | || |_) || (_) || |   | |_
             |_||_| |_| |_|| .__/  \___/ |_|    \__|
                           |_|
          access the script from another file or module









                                    _    _
                  _ __ ___    __ _ | |_ | |__
                 | '_ ` _ \  / _` || __|| '_ \
                 | | | | | || (_| || |_ | | | |
                 |_| |_| |_| \__,_| \__||_| |_|

               module for mathematical functions

               docs.python.org/3/library/math.html









                                              _
        __ __  __ _ __   _ __  ___  ___  ___ (_) ___   _ __
      / _ \\ \/ /| '_ \ | '__|/ _ \/ __|/ __|| | / _ \ | '_ \
     |  __/ >  < | |_) || |  |  __/\__ \\__ \| || (_) || | | |
      \___|/_/\_\| .__/ |_|   \___||___/|___/|_| \___/ |_| |_|
                 |_|
         combination of numbers, operators, and parentheses









========================================================================
Drill 1-7 Import the math module and solve basic mathematical operations.

a) Evaluate the area of a circle in Python.
b) Compute the sine or cosine of an angle.
========================================================================
'''






r'''          _                       _     __  __
             (_) _ __   _ __   _   _ | |_  / /  \ \
             | || '_ \ | '_ \ | | | || __|| |    | |
             | || | | || |_) || |_| || |_ | |    | |
             |_||_| |_|| .__/  \__,_| \__|| |    | |
                       |_|                 \_\  /_/

                          user input

                        ___     __ ___
                       |_ _|   / // _ \
                        | |   / /| | | |
                        | |  / / | |_| |
                       |___|/_/   \___/






   _____                       ____             _    _
  |_   _|_   _  _ __    ___   / ___| __ _  ___ | |_ (_) _ __    __ _
    | | | | | || '_ \  / _ \ | |    / _` |/ __|| __|| || '_ \  / _` |
    | | | |_| || |_) ||  __/ | |___| (_| |\__ \| |_ | || | | || (_| |
    |_|  \__, || .__/  \___|  \____|\__,_||___/ \__||_||_| |_| \__, |
         |___/ |_|                                             |___/

            conversion of object from one data type to another













                    @@@@@@@@@@@@@@@@@@@@@@@@@@(.
                  ,@@@@@@@@@@@@@@@@@@@@@@@@@@@#.
                 .@#*     @@@,     @@@@#
                 .(       @@#.     @@@@(
                         @@@(      @@@@/
                         @@@(     #@@@@*
                        @@@@*     @@@@#.
                       @@@@#.     @@@@#
                     @@@@@@(      @@@@@*     @#
                   @@@@@@@@*      @@@@@@@@@@@&/
                   (@@@@@@/        &@@@@@@@@(.
                      ,,.              ,,,

========================================================================
Drill 1-8 Repeat the previous module but ask for user input of variables.

a) Evaluate the area of a circle in Python. Ask for radius from user.
b) Compute the sine or cosine of an angle. Ask for angle.
========================================================================
'''




r'''

               __              _          _
              / _|        ___ | |_  _ __ (_) _ __    __ _
             | |_  _____ / __|| __|| '__|| || '_ \  / _` |
             |  _||_____|\__ \| |_ | |   | || | | || (_| |
             |_|         |___/ \__||_|   |_||_| |_| \__, |
                                                    |___/

                        formatted string

    e.g. {variable:.2f}, {variable:,}, Php{cash:,.2f}, {ratio:.2%}




            3,141592653589793238462643383279502884197169399375
        105820974944592307816406286208998628034825342117067982
      14808651328230664709384460955058223172535940812848111745
    0284102701938521105559644622948954930381964428810975665933
    4461284756482337867831652712019091456485669234603486104543
  26648213          393607              26024914
  1273              724587            0066063155
8817                488152            0920962829
25                  409171            53643678
                    925903            60011330
                    530548            82046652
                  138414              69519415
                  116094              33057270
                  365759              59195309
                  218611              73819326
                  117931              05118548
                07446237              99627495
                67351885            7527248912
              2793818301            1949129833
              6733624406            5664308602
            139494639522            4737190702
            1798609437              0277053921              71
          762931767523              8467481846              76
          694051320005              681271452635          6082
        77857713427577              89609173637178      7214
      6844090122495343              014654958537105079227968
      92589235420199                  56112129021960864034
      41815981362977                  47713099605187072113
      499999983729                      7804995105973173
          281609                            63185950




                                                  _    _
              _ __ ___   _ __   _ __ ___    __ _ | |_ | |__
             | '_ ` _ \ | '_ \ | '_ ` _ \  / _` || __|| '_ \
             | | | | | || |_) || | | | | || (_| || |_ | | | |
             |_| |_| |_|| .__/ |_| |_| |_| \__,_| \__||_| |_|
                        |_|

                    for high-precision constants











  _                   _          _              _        __ __     __
 | |__    __ _   ___ | | __ ___ | |  __ _  ___ | |__    / / \ \    \ \
 | '_ \  / _` | / __|| |/ // __|| | / _` |/ __|| '_ \  | |   \ \    | |
 | |_) || (_| || (__ |   < \__ \| || (_| |\__ \| | | | | |    \ \   | |
 |_.__/  \__,_| \___||_|\_\|___/|_| \__,_||___/|_| |_| | |     \_\  | |
                                                        \_\        /_/

         breaks a long line of code into multiple lines










  _____                      _          _    _
 | ____|       _ __    ___  | |_  __ _ | |_ (_)  ___   _ __
 |  _|  _____ | '_ \  / _ \ | __|/ _` || __|| | / _ \ | '_ \
 | |___|_____|| | | || (_) || |_| (_| || |_ | || (_) || | | |
 |_____|      |_| |_| \___/  \__|\__,_| \__||_| \___/ |_| |_|

                   exponential notation









          _          __  _         _  _
         (_) _ __   / _|(_) _ __  (_)| |_  _   _
         | || '_ \ | |_ | || '_ \ | || __|| | | |
         | || | | ||  _|| || | | || || |_ | |_| |
         |_||_| |_||_|  |_||_| |_||_| \__| \__, |
                                           |___/
                         inf

                       math.inf








                                        _   __  __
          _ __  ___   _   _  _ __    __| | / /  \ \
         | '__|/ _ \ | | | || '_ \  / _` || |    | |
         | |  | (_) || |_| || | | || (_| || |    | |
         |_|   \___/  \__,_||_| |_| \__,_|| |    | |
                                           \_\  /_/
                     rounding numbers











                       _            __  __
                 __ _ | |__   ___  / /  \ \
                / _` || '_ \ / __|| |    | |
               | (_| || |_) |\__ \| |    | |
                \__,_||_.__/ |___/| |    | |
                                   \_\  /_/

                 absolute value of a number











     _            _         _                             __  __
    (_) ___      (_) _ __  | |_  ___   __ _   ___  _ __  / /  \ \
    | |/ __|     | || '_ \ | __|/ _ \ / _` | / _ \| '__|| |    | |
  _ | |\__ \     | || | | || |_|  __/| (_| ||  __/| |   | |    | |
 (_)|_||___/_____|_||_| |_| \__|\___| \__, | \___||_|   | |    | |
           |_____|                    |___/              \_\  /_/

             True if no fractional part, otherwise False.










                             _          __  __
                  _ __ ___  (_) _ __   / /  \ \
                 | '_ ` _ \ | || '_ \ | |    | |
                 | | | | | || || | | || |    | |
                 |_| |_| |_||_||_| |_|| |    | |
                                       \_\  /_/

                           minimum










                                           __  __
                  _ __ ___    __ _ __  __ / /  \ \
                 | '_ ` _ \  / _` |\ \/ /| |    | |
                 | | | | | || (_| | >  < | |    | |
                 |_| |_| |_| \__,_|/_/\_\| |    | |
                                          \_\  /_/
                           maximum











                    _                __ __
                   | |  ___  _ __   / / \ \
                   | | / _ \| '_ \ | |   | |
                   | ||  __/| | | || |   | |
                   |_| \___||_| |_|| |   | |
                                    \_\ /_/

                           length








                        Special Assignment Operations


                                _     _____
                              _| |_  |_____|
                             |_   _| |_____|
                               |_|

                                      _____
                              _____  |_____|
                             |_____| |_____|


                             __/\__  _____
                             \    / |_____|
                             /_  _\ |_____|
                               \/

                                 __
                                / /  _____
                               / /  |_____|
                              / /   |_____|
                             /_/

                               __ __
                              / // /  _____
                             / // /  |_____|
                            / // /   |_____|
                           /_//_/


                              _  __
                             (_)/ /  _____
                               / /  |_____|
                              / /_  |_____|
                             /_/(_)



                           __/\____/\__  _____
                           \    /\    / |_____|
                           /_  _\/_  _\ |_____|
                             \/    \/

'''



r'''
Additional Exercises:


Big Number:

• Write a script that creates the two variables, num1 and num2. Both
  num1 and num2 should be assigned the integer literal 12,000,000,000
  one written with underscored and one without. Print num1 and num2
  on two separate lines.
'''






r'''
Exponentiation:

• Write a script that assigns the floating-point literal 234000.0 to the
  variable num using exponential notation, and then prints num.

• Write a script that receives two numbers from the user and displays the
  first number raised to the power of the second number.

'''



'''

Infinity:

 • Find the smallest exponent n so that 2e n, returns inf.


Rounding-off:

 • Write a script that asks the user to input a number and then displays
   that number rounded to two decimal places.
'''




'''
Absolute value:

 • Write a script that asks the user to input a number and
  then displays the absolute value of that number.
'''


'''
Is integer:

 • Write a script that asks the user to input two numbers by using the
   input() function twice, then display whether or not the difference
   between those two number is an integer.
'''




'''
F-string:

 • Print the result of the calculation 7 ** .321 as a fixed-point
   number with three decimal places.

 • Print the number 340000 as currency, with the thousands grouped
   with commas. Currency should be displayed with two decimal places.

 • Print the result of 3 / 12 as a percentage with no decimal places.
'''






r'''
          ____                            _      _
         | __ )  _ __  __ _  _ __    ___ | |__  (_) _ __    __ _
         |  _ \ | '__|/ _` || '_ \  / __|| '_ \ | || '_ \  / _` |
         | |_) || |  | (_| || | | || (__ | | | || || | | || (_| |
         |____/ |_|   \__,_||_| |_| \___||_| |_||_||_| |_| \__, |
                                                           |___/


                                     ,▌

                                     ²▓

                                   ,e╜`*µ

                                ,m╜      `*w

                             ,*`             ⁿw

                 ▌MMMMMMMMM▀▄     CONDITION    ,ÅMMMMMMMMM▀M

                 ▌           `*µ            ,x╜           ]▌

                 ▌               *w      ,m╜              ]▌

                 ▌                  ╙w¿*╙                 ]▌

                ██    True                                ██   False

      ┌∞∞∞∞∞∞∞∞∞∞æ∞∞∞∞∞∞∞∞∞∞~                   æ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞w

      ▐                     &                   &                    ]

      ▐    statements1      &                   &     statements2    ]

      ▐                     &                   &                    ]

      ▐,,,,,,,,,,,,,,,,,,,,,&                   ▌,,,,,,,,,,,,,,,,,,,,▐

                 ▌                                        ▐M

                 ▌                                        ▐M

                 ▌                ,¿∞**═w,                ▐M

                 ▌               ƒ        *               ▐M

                 ▌▄▄▄▄▄▄▄▄▄▄▄▄█▄▐          ╠▄█▄▄▄▄▄▄▄▄▄▄▄▄█M

                                 t        ç`

                                  ²*w~¿~*`

                                     ]▌

                                     ]▌



                            if CONDITION:

                                statements1

                            else:

                                statements2


========================================================================
Drill 2-1 Write a Python program that determines whether the number is
          odd or even.
========================================================================
'''









r'''
  ___             _               _          _    _
 |_ _| _ __    __| |  ___  _ __  | |_  __ _ | |_ (_)  ___   _ __
  | | | '_ \  / _` | / _ \| '_ \ | __|/ _` || __|| | / _ \ | '_ \
  | | | | | || (_| ||  __/| | | || |_| (_| || |_ | || (_) || | | |
 |___||_| |_| \__,_| \___||_| |_| \__|\__,_| \__||_| \___/ |_| |_|

                 indicates nesting in Python











   ____                                                   _
  / ___| ___   _ __ ___   _ __    ___   _   _  _ __    __| |
 | |    / _ \ | '_ ` _ \ | '_ \  / _ \ | | | || '_ \  / _` |
 | |___| (_) || | | | | || |_) || (_) || |_| || | | || (_| |
  \____|\___/ |_| |_| |_|| .__/  \___/  \__,_||_| |_| \__,_|
                         |_|

                  two or more conditions

========================================================================
Drill 2-2 Write a Python program that determines whether the age is
          equal to or over 18, and whether cash is equal to or over
          Php 100.
========================================================================
'''




r'''
========================================================================
Drill 2-3 Write a program that examines three variables — x, y, and z —
          and prints the least among them.
========================================================================
'''







r'''
========================================================================
Drill 2-4 Write a program that examines three variables — x, y, and z —
          and prints the largest odd number among them. If none of them
          are odd, it should print the smallest value of the three.
========================================================================
'''





r'''
                      _____       _
                     |  ___|__ _ | | ___   ___
                     | |_  / _` || |/ __| / _ \
                     |  _|| (_| || |\__ \|  __/
                     |_|   \__,_||_||___/ \___|

                    0, '', and None equate to False




                      _____
                     |_   _|_ __  _   _   ___
                       | | | '__|| | | | / _ \
                       | | | |   | |_| ||  __/
                       |_| |_|    \__,_| \___|

            Non-zero, non-empty strings, any object equate to True

'''






r'''
  _   _             _             _   _   __                 _  _   __
 | \ | |  ___  ___ | |_  ___   __| | (_) / _|           ___ | |(_) / _|
 |  \| | / _ \/ __|| __|/ _ \ / _` | | || |_   _____   / _ \| || || |_
 | |\  ||  __/\__ \| |_|  __/| (_| | | ||  _| |_____| |  __/| || ||  _|
 |_| \_| \___||___/ \__|\___| \__,_| |_||_|            \___||_||_||_|

========================================================================
Drill 2-5 Write a program that converts the raw score input into
          equivalent grade using the ff. transmutation:

                    EQUIV  RAW SCORE
                    GRADE
                    4.0     96-100
                    3.5     92-95
                    3.0     88-91
                    2.5     83-87
                    2.0     78-82
                    1.5     74-77
                    1.0     70-73
                    0.0     Below 70
========================================================================
'''





r'''
              ___  _                     _    _
             |_ _|| |_  ___  _ __  __ _ | |_ (_)  ___   _ __
              | | | __|/ _ \| '__|/ _` || __|| | / _ \ | '_ \
              | | | |_|  __/| |  | (_| || |_ | || (_) || | | |
             |___| \__|\___||_|   \__,_| \__||_| \___/ |_| |_|

                             loops or repetition


                                     M▓

                                     █▓▄

                                     K▓

                                   ,▄▀▀▀µ

                                ,▄▀`     ²▀q

                             çæ╨            ²▀g,

                          ç#╜                  `▀▄,

                      ,╓▀╜                         ╨¼µ       False

         ▐█▀▀▀▀▀▀▓▓▓╜╨▒,         CONDITION           ç▓▀▀▀▀▀▀▀▀▀▀█

         ▐&            `▀æµ                       ç#╜           ]▓

         ▐&                ╨æµ                ,q▀╜              ]▓

         ▐&                   ²▀ç          ,▄▀"                 ]▓

         ▐&                      ²▀q    ,▄▀`                    ]▓

         ▐&                         `▀█╨                        ]▓

         ▐&                          C▓     True                ]▓

         ▐&                          ▓▓▌                        ]▓

         ▐&           ,,,,,,,,,,,,,,,▐▒,,,,,,,,,,,,,,,,         ]▓

         ▐&          ▐Ω                               Ñ         ]▓

         ▐&          ▐           statements           ▐         ]▓

         ▐&          ▐                                ▐         ]▓

         ▐&          ²╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙█▌╙╙╙╙╙╙╙╙╙╙╙╙╙╙²         ]▓

         ▐&                           ▐▌                        ]▓

         ▐&                           ▐▌                        ]▓

         ▓█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▌                        ]▓

                                                                ]▓

                                                                ]▓

                        while CONDITION:
                            statements


                               or


                        for item in sequence:
                            statements




                                                   __  __
                  _ __  __ _  _ __    __ _   ___  / /  \ \
                 | '__|/ _` || '_ \  / _` | / _ \| |    | |
                 | |  | (_| || | | || (_| ||  __/| |    | |
                 |_|   \__,_||_| |_| \__, | \___|| |    | |
                                     |___/        \_\  /_/

                    generates a sequence of numbers



                                              __  __
                      ___  _   _  _ __ ___   / /  \ \
                     / __|| | | || '_ ` _ \ | |    | |
                     \__ \| |_| || | | | | || |    | |
                     |___/ \__,_||_| |_| |_|| |    | |
                                             \_\  /_/


========================================================================
Drill 2-6 a) Get the sum of a sequence of integers from 1 to 10.
             Repeat this for odd and even integers only.
          b) Calculate the factorial of a number using iteration.
========================================================================
'''





r'''
========================================================================
Drill 2-7 Write a program that asks the user to input 10 integers, and
          then prints the largest odd number that was entered. If
          no odd number was entered, it should print a message to that
          effect.
========================================================================
'''






r'''
  _   _             _             _   _
 | \ | |  ___  ___ | |_  ___   __| | | |  ___    ___   _ __   ___
 |  \| | / _ \/ __|| __|/ _ \ / _` | | | / _ \  / _ \ | '_ \ / __|
 | |\  ||  __/\__ \| |_|  __/| (_| | | || (_) || (_) || |_) |\__ \
 |_| \_| \___||___/ \__|\___| \__,_| |_| \___/  \___/ | .__/ |___/
                                                      |_|
                    a loop within another loop

========================================================================
Drill 2-8 a) Write a python program that prints the multiplication table.
          b) Print a 2d-array of '*' characters.
========================================================================
'''










r'''
                      _                        _
                     | |__   _ __  ___   __ _ | | __
                     | '_ \ | '__|/ _ \ / _` || |/ /
                     | |_) || |  |  __/| (_| ||   <
                     |_.__/ |_|   \___| \__,_||_|\_\

                            exits the loop





                                 _    _
               ___  ___   _ __  | |_ (_) _ __   _   _   ___
              / __|/ _ \ | '_ \ | __|| || '_ \ | | | | / _ \
             | (__| (_) || | | || |_ | || | | || |_| ||  __/
              \___|\___/ |_| |_| \__||_||_| |_| \__,_| \___|

                         skips to next iteration

'''






r'''
                                         _
                  _ __  __ _  _ __    __| |  ___   _ __ ___
                 | '__|/ _` || '_ \  / _` | / _ \ | '_ ` _ \
                 | |  | (_| || | | || (_| || (_) || | | | | |
                 |_|   \__,_||_| |_| \__,_| \___/ |_| |_| |_|

                             random.randint(a, b)

                returns a random integer k such that a <= k <= b



========================================================================
Drill 2.9 Create a dice rolling program that continue to roll a pair
    of dice until the user indicates that they do not want to roll again.
========================================================================
'''




r'''
========================================================================
Drill 2:10 Write a number guessing game in which the user will guess a
           random number, 1 <= k <= 100. Provide feedback to the user if
           the current guess is higher or lower than the random number.
========================================================================
'''
import sys
import random

num = random.randint(1,100)
# guess = sys.maxsize
guess = -1

while num != guess:
  guess = int(input("Input your guess (1 <= k <= 100): "))
  if guess > num:
    print("Your guess is greater than my number...")
  if guess < num:
    print("Your guess is smaller than my number...")

print("Congratulations! You guessed my number:", num)



############################  END OF PART I  #############################
