r'''
              ___________________________________________________
            /                                                    \
           |    _____________________________________________     |
           |   |                                             |    |
           |   |  >>> _                                      |    |
           |   |                                             |    |
           |   |             Python Refresher III            |    |
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


        • To introduce Karel the Robot introductory programming
          environment to teach students the fundamental concepts
          and skills of programming.

        • To practice conditionals and iteration (while-loop) as
          applied to solving Karel the Robot problems emphasizing
          logic and structure over calculation.

        • To install a Python package with pip package manager.

        • To introduce precondition and postcondition concepts.



              _      _  _                       __
   __      __| |__  (_)| |  ___  __   __ ___   / _|  ___   _ __
   \ \ /\ / /| '_ \ | || | / _ \ \ \ / // __| | |_  / _ \ | '__|
    \ V  V / | | | || || ||  __/  \ V / \__ \ |  _|| (_) || |
     \_/\_/  |_| |_||_||_| \___|   \_/  |___/ |_|   \___/ |_|




                               _
                        _ __  (_) _ __
                       | '_ \ | || '_ \
                       | |_) || || |_) |
                       | .__/ |_|| .__/
                       |_|       |_|

        a tool for installing and managing Python packages


          e.g.       pip install stanfordkarel


            Note: pip is run from the command line,
                     not the Python interpreter.


                    _  __                  _
                   | |/ / __ _  _ __  ___ | |
                   | ' / / _` || '__|/ _ \| |
                   | . \| (_| || |  |  __/| |
                   |_|\_\\__,_||_|   \___||_|

          Educational programming language for beginners
                       Rich Pattis (1970)

        e.g.
                   BEGINNING-OF-PROGRAM

                   DEFINE turnRight AS
                   BEGIN
                     turnLeft;
                     turnLeft;
                     turnLeft;
                   END

                   BEGINNING-OF-EXECUTION
                     ITERATE 3 TIMES
                     BEGIN
                       turnRight;
                         move
                       END
                       turnoff
                     END-OF-EXECUTION

                    END-OF-PROGRAM


      • Syntactic rules and patterns - conditionals and iteration
      • Defining new functions
      • Problem Decomposition
      • Logic and structure over calculation





========================================================================
Drill 1-0 a) Install stanfordkarel module by running the ff. in
             cmd or Anaconda prompt or Terminal.

                 pip install stanfordkarel

       (https://pypi.org/project/stanfordkarel/)

       b) Issue help() on stanfordkarel module for documentation
       and familiarize Karel commands.

       c) Run a simple Karel program where Karel moves forward 3 times.
========================================================================
'''

# YOUR CODE HERE



r'''
               _          _    _
              / \    ___ | |_ (_)  ___   _ __   ___
             / _ \  / __|| __|| | / _ \ | '_ \ / __|
            / ___ \| (__ | |_ | || (_) || | | |\__ \
           /_/   \_\\___| \__||_| \___/ |_| |_||___/

                      BASIC FUNCTIONS

                      move() -> None

                      turn_left() -> None

                      pick_beeper() -> None

                      put_beeper() -> None

                      paint_corner(color: str) -> None



                             _  _  _    _                       _
       ___  ___   _ __    __| |(_)| |_ (_)  ___   _ __    __ _ | |
      / __|/ _ \ | '_ \  / _` || || __|| | / _ \ | '_ \  / _` || |
     | (__| (_) || | | || (_| || || |_ | || (_) || | | || (_| || |
      \___|\___/ |_| |_| \__,_||_| \__||_| \___/ |_| |_| \__,_||_|


   TEST                 OPPOSITE                    CHECKING

front_is_clear()    front_is_blocked()     Is there a wall in front of Karel?

left_is_clear()     left_is_blocked()      Is there a wall to Karel’s left?

right_is_clear()    right_is_blocked()     Is there a wall to Karel’s right?

beepers_present()   no_beepers_present()   Are there beepers on this corner?

beepers_in_bag()    no_beepers_in_bag()    Any there beepers in Karel’s bag?

facing_north()      not_facing_north()     Is Karel facing north?

facing_east()       not_facing_east()      Is Karel facing east?

facing_south()      not_facing_south()     Is Karel facing south?

facing_west()       not_facing_west()      Is Karel facing west?

corner_color_is(color: str)         Is the color of corner (color: str)?



                        _ __  _   _  _ __
                       | '__|| | | || '_ \
                       | |   | |_| || | | |
                       |_|    \__,_||_| |_|

              run_karel_program(world_file: str = '') -> None



                                            __  __
              _ __ ___    ___ __   __ ___  / /  \ \
             | '_ ` _ \  / _ \\ \ / // _ \| |    | |
             | | | | | || (_) |\ V /|  __/| |    | |
             |_| |_| |_| \___/  \_/  \___|| |    | |
                                           \_\  /_/
                  move forward one square



  _                             _         __  _     __  __
 | |_  _   _  _ __  _ __       | |  ___  / _|| |_  / /  \ \
 | __|| | | || '__|| '_ \      | | / _ \| |_ | __|| |    | |
 | |_ | |_| || |   | | | |     | ||  __/|  _|| |_ | |    | |
  \__| \__,_||_|   |_| |_|_____|_| \___||_|   \__|| |    | |
                         |_____|                   \_\  /_/

               turn 90 degrees to the left




                _         _                                      __  __
  _ __   _   _ | |_      | |__    ___   ___  _ __    ___  _ __  / /  \ \
 | '_ \ | | | || __|     | '_ \  / _ \ / _ \| '_ \  / _ \| '__|| |    | |
 | |_) || |_| || |_      | |_) ||  __/|  __/| |_) ||  __/| |   | |    | |
 | .__/  \__,_| \__|_____|_.__/  \___| \___|| .__/  \___||_|   | |    | |
 |_|               |_____|                  |_|                 \_\  /_/

                  puts a beeper on the current square





         _        _                                                  __  __
  _ __  (_)  ___ | | __       _ __    ___   ___  _ __    ___  _ __  / /  \ \
 | '_ \ | | / __|| |/ /      | '_ \  / _ \ / _ \| '_ \  / _ \| '__|| |    | |
 | |_) || || (__ |   <       | |_) ||  __/|  __/| |_) ||  __/| |   | |    | |
 | .__/ |_| \___||_|\_\_____ | .__/  \___| \___|| .__/  \___||_|   | |    | |
 |_|                  |_____||_|                |_|                 \_\  /_/

                picks up a beeper from the current square




========================================================================
Drill 1-1 a) Write a Karel helper function to make Karel turn right.
          e.g. turn_right()

          b) Write a Karel helper function to make Karel turn around.
          e.g. turn_around()

          Note: This new functions extends the set of operation the
          robot can perform
========================================================================
'''


# YOUR CODE HERE

from stanfordkarel import *

def turn_around():
  turn_left()
  turn_left()

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def go_to_wall():
  while front_is_clear():
    move()




r'''                                       _  _  _    _
  _ __   _ __  ___   ___  ___   _ __    __| |(_)| |_ (_)  ___   _ __
 | '_ \ | '__|/ _ \ / __|/ _ \ | '_ \  / _` || || __|| | / _ \ | '_ \
 | |_) || |  |  __/| (__| (_) || | | || (_| || || |_ | || (_) || | | |
 | .__/ |_|   \___| \___|\___/ |_| |_| \__,_||_| \__||_| \___/ |_| |_|
 |_|
              what is true about the inputs to a function
                   to guarantee expected behavior

              or assumed true at the start of a method

        e.g.
                  • Karel starts at (1,1) facing East
                  • the world is rectangular and,
                  • there are no walls other than the outer border





                     _                          _  _  _    _
  _ __    ___   ___ | |_  ___  ___   _ __    __| |(_)| |_ (_)  ___   _ __
 | '_ \  / _ \ / __|| __|/ __|/ _ \ | '_ \  / _` || || __|| | / _ \ | '_ \
 | |_) || (_) |\__ \| |_| (__| (_) || | | || (_| || || |_ | || (_) || | | |
 | .__/  \___/ |___/ \__|\___|\___/ |_| |_| \__,_||_| \__||_| \___/ |_| |_|
 |_|
              what must always be true after the execution
                   of a function or block of code

              or promised to be true at the end of a method

        e.g.
                  • the world will be full of beepers
                  • Karel's final position will not important
                  • Karel may face in any direction




========================================================================
Drill 1-2 Write a Karel helper function to put beepers in the row.
          What are the preconditions and postconditions?
========================================================================
'''


# YOUR CODE HERE


r'''

      _                                                  _  _    _
   __| |  ___   ___  ___   _ __ ___   _ __    ___   ___ (_)| |_ (_)  ___   _ __
  / _` | / _ \ / __|/ _ \ | '_ ` _ \ | '_ \  / _ \ / __|| || __|| | / _ \ | '_ \
 | (_| ||  __/| (__| (_) || | | | | || |_) || (_) |\__ \| || |_ | || (_) || | | |
  \__,_| \___| \___|\___/ |_| |_| |_|| .__/  \___/ |___/|_| \__||_| \___/ |_| |_|
                                     |_|
                organizing a program as a number of parts

                  e.g. the main() should be clutter-free



========================================================================
Drill 1-3 Write a Karel helper function to solve the collect newspaper
          karel problem. Make Karel walk to the door of its house, pick
          up the newspaper (beeper), and then return to its initial
          position in the upper left corner of the house.
          What are the preconditions and postconditions?
========================================================================
'''


# YOUR CODE HERE








r'''
========================================================================
Drill 1-4 Write a Karel helper function to install beepers in the
          perimeter of the word. The solution should be able to solve
          any of at least 2x2 in size.
          Note: Do not repeat beeper installation.
          What are the preconditions and postconditions?
========================================================================
'''



# YOUR CODE HERE







r'''
========================================================================
Drill 1-5 Write a Karel helper function to paint the perimeter 'Green'.
          What are the preconditions and postconditions?
========================================================================

                _         _                                              __  __
  _ __    __ _ (_) _ __  | |_       ___  ___   _ __  _ __    ___  _ __  / /  \ \
 | '_ \  / _` || || '_ \ | __|     / __|/ _ \ | '__|| '_ \  / _ \| '__|| |    | |
 | |_) || (_| || || | | || |_     | (__| (_) || |   | | | ||  __/| |   | |    | |
 | .__/  \__,_||_||_| |_| \__|_____\___|\___/ |_|   |_| |_| \___||_|   | |    | |
 |_|                         |_____|                                    \_\  /_/
'''



# YOUR CODE HERE




r'''
========================================================================
Drill 1-6 Write a Karel helper function to create an ascending staircase
          pattern of beepers.
          What are the preconditions and postconditions?
========================================================================
'''



# YOUR CODE HERE







r'''
========================================================================
Drill 1-7 Write a Karel helper function to create an ascending staircase
          pattern of colors.
          What are the preconditions and postconditions?

Karel Colors:

colors = ["Red","Black","Cyan","Dark Gray", \
    "Gray", "Green", "Light Gray", "Magenta", \
    "Orange", "Pink", "White", "Blue","Yellow",
]
========================================================================
'''



# YOUR CODE HERE







r'''
========================================================================
Drill 1-8 Write a Karel helper function to create an descending staircase
          pattern of beepers.
          What are the preconditions and postconditions?
========================================================================
'''

# YOUR CODE HERE









r'''
========================================================================
Drill 1-8 Write a Karel helper function to create an descending staircase
          pattern of colors.
          What are the preconditions and postconditions?
========================================================================
'''

# YOUR CODE HERE










r'''
========================================================================
Drill 1-9 Write a Karel helper function to create a pyramid pattern
          of colors.
          What are the preconditions and postconditions?
========================================================================
'''

# YOUR CODE HERE










r'''
========================================================================
Drill 1-9 Write a Karel helper function to create a random color pattern
          for any world size.
          What are the preconditions and postconditions?
========================================================================
'''

# YOUR CODE HERE

def go_back(steps):
  turn_around()
  for _ in range(steps):
    move()

def move_to_position():
  turn_right()
  move()
  turn_right()

import random
def get_color():
  colors = ["Red","Black","Cyan","Dark Gray", \
      "Gray", "Green", "Light Gray", "Magenta", \
      "Orange", "Pink",  "Blue","Yellow",
  ] # "White"
  return random.choice(colors)


def color_corners(number):
  for _ in range(number):
    paint_corner(get_color())
    move()
  paint_corner(get_color())

def pyramid():
  # Base count
  base = 0
  while front_is_clear():
    paint_corner(get_color())
    move()
    base += 1
  paint_corner(get_color())

  # Go back
  go_back(base-1)

  base -= 2

  # Install in next layers
  while right_is_clear() and base > -1:
    move_to_position()
    color_corners(base)
    go_back(base-1)
    base -= 2

def main():
  pyramid()

if __name__=="__main__":
  run_karel_program()



r'''
========================================================================
Drill 1-10 Write a Karel program to create rectangular layers of color.
          Note: World should be at least 2x2.
          What are the preconditions and postconditions?
========================================================================
'''


# YOUR CODE HERE





r'''
                        _      _                _  _  _
 __      __ ___   _ __ | |  __| |      ___   __| |(_)| |_  ___   _ __
 \ \ /\ / // _ \ | '__|| | / _` |     / _ \ / _` || || __|/ _ \ | '__|
  \ V  V /| (_) || |   | || (_| |    |  __/| (_| || || |_| (_) || |
   \_/\_/  \___/ |_|   |_| \__,_|_____\___| \__,_||_| \__|\___/ |_|
                                |_____|

from stanfordkarel.world_editor import run_world_editor

if __name__ == "__main__":
    run_world_editor()
'''
