r'''
              ___________________________________________________
            /                                                    \`
           |    _____________________________________________     |
           |   |                                             |    |
           |   |  >>> _                                      |    |
           |   |                                             |    |
           |   |             Python Refresher II             |    |
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


        • To practice conditionals and iteration as applied to
          creating basic patterns.
        • To declare simple functions without parameters. (code reuse)

     __                      _    _                      __  __
    / _| _   _  _ __    ___ | |_ (_)  ___   _ __   ___  / /  \ \
   | |_ | | | || '_ \  / __|| __|| | / _ \ | '_ \ / __|| |    | |
   |  _|| |_| || | | || (__ | |_ | || (_) || | | |\__ \| |    | |
   |_|   \__,_||_| |_| \___| \__||_| \___/ |_| |_||___/| |    | |
                                                        \_\  /_/
      a block of code which only runs when it is called



          _         __  _         _  _    _
       __| |  ___  / _|(_) _ __  (_)| |_ (_)  ___   _ __
      / _` | / _ \| |_ | || '_ \ | || __|| | / _ \ | '_ \
     | (_| ||  __/|  _|| || | | || || |_ | || (_) || | | |
      \__,_| \___||_|  |_||_| |_||_| \__||_| \___/ |_| |_|

                      def function_name():
                        block_of_code

                                  _  _
                       ___  __ _ | || |
                      / __|/ _` || || |
                     | (__| (_| || || |
                      \___|\__,_||_||_|

                        function_name()

========================================================================
Drill 1-0 Write a function that prints "Hello, World".
========================================================================
'''

def greet():
  print("Hello, World!")



import random
import string

def put_char():  # FOR REUSE
  '''
  Prints a random uppercase letter
  '''
  char = random.choice(string.ascii_uppercase)
  #print(char, end='')
  return char
  # This is not returning the char
  # NONE



def put_blank():  # FOR REUSE
  '''
  Prints a blank character
  '''
  print(" ", end='')


r'''
========================================================================
Drill 1-1 Write a Python program that prints the following box pattern:
(Use random and string module to generate random uppercase characters)
========================================================================
e.g.

      KBNRRXHJTKRROAZKIFIGWXQOIWMAYNXQWNKKXRXEBLXBQTXGZS
      ZRGUQSOTOUHHIQHKDHABJOIKGNSVCPTPKBDZAHKGQMZHJUGGKE
      TBKHSGNMOHEJQABOSAIYRFPNUBPMIJGVFJXLPXZTAKIUUYPYST
      HCLBYXTHETFWTRTRITCKNIFDODLIEZKQGADLNZPEVEMGLMPWAG
      JMVBRZYQYDIVQFRUHJZQDESOWDTWRTZMJUBHSJOGFVEQCEAQOK
      YGROYHBOTMRVSYBAITAQPEMGXRDDYOVMIDFPYRLEMVTUETTAVJ
      ICGIEOAATRJHJSIPLATDBOHNXEBHJDXHHGLEUWBPPPSYNIVRCG
      MCPDDFJHHJKOLTDWTCTLANKKFMERBHJTWPGMILKZWESITPDWXX
      VMJLKJVSOECXQYBHLLSWOJONFQHJTXAPGFNFFGVNBPHAPXZFSG
      PHQBCYXDGOBUBVMIEUFXNAWIMGTDYAOBJFNXRBETNHDFQYQUFI

========================================================================
'''

def box():
  height = 5
  width = 50

  print()
  for i in range(height):
    for j in range(width):
      put_char()
    print()



r'''
========================================================================
Drill 1-2 Write a Python program that prints the following hollow box
pattern: (Use random & string module to generate random uppercase characters)
========================================================================
e.g.

          XIOAFFUTMCHEYQKODLEAVLWREBFXTRTHCTRLLISJ
          T                                      R
          U                                      E
          A                                      V
          B                                      L
          F                                      I
          Y                                      L
          W                                      T
          E                                      V
          IEFEJRRCWLZQRKUBJMXIOWHPKKOPVTPMTIMSRJGP

========================================================================
'''

def hollow_box():
  height = 10
  width = 40

  print()
  for row in range(height):
    for col in range(width):
      if row > 0 and row < height - 1:
        if col == 0 or col == width - 1:
          put_char()
        else:
          put_blank()
      else:
        put_char()
    print()




r'''
========================================================================
Drill 1-3 Write a Python program that prints the following right triangle
pattern: (Use random & string module to generate random uppercase characters)
========================================================================
e.g.

  J
  IK
  FXY
  VLFR
  IWNNU
  YMUAXP
  IHGLFOH
  AKLDHXKZ
  BNMPEYXSK
  QPPHJJKNSU
========================================================================
'''


def right_t():
  height = 10

  for row in range(height):
    for col in range(row):
      put_char()
    print()








r'''
========================================================================
Drill 1-4 Write a Python program that prints the following hollow right
triangle pattern: (Use random & string module to generate random uppercase
characters)
========================================================================
e.g.

  R
  YU
  E N
  Q  R
  W   B
  C    N
  Z     P
  W      U
  Q       G
  CJIJLNGRYT
========================================================================
'''


def hollow_right_t():
  height = 10

  for row in range(height):
    for col in range(row):
      if row > 1 and row < height - 1:
        if col == 0 or col == row - 1:
          put_char()
        else:
          put_blank()
      else:
        put_char()
    print()







r'''
========================================================================
Drill 1-5 Write a Python program that prints the following inverted right
triangle pattern:
(Use random & string module to generate random uppercase characters)
========================================================================
e.g.

  RRJABDRNIO
  UZKMYLPNF
  YLPSPBSG
  WPLEBML
  FQYZYM
  IVERP
  BPIR
  FEL
  KQ
  Y
========================================================================
'''

def inverted_right_t():
  height = 5

  print()
  for row in range(height):
    for col in range(height-row):
      put_char()
    print()






r'''
========================================================================
Drill 1-5 Write a Python program that prints the following inverted right
hollow triangle pattern:
(Use random & string module to generate random uppercase characters)
========================================================================
e.g.

  NUHAIFYPCU
  V       A
  Q      E
  W     G
  M    F
  Y   D
  C  U
  B I
  KF
  P
========================================================================
'''

def hollow_inverted_right_t():
  height = 10

  print()
  for row in range(height):
    for col in range(height-row):
      if row > 0 and row < height - 2:
        if col == 0 or col == height - row - 1:
          put_char()
        else:
          put_blank()
      else:
        put_char()
    print()







r'''
========================================================================
Drill 1-6 Write a Python program that prints the following right triangle
pattern (right-side oriented). Use h variable to denote the height.
(Use random & string module to generate random uppercase characters)
========================================================================
e.g. at h = 10:
         J
        BC
       IBO
      NLXW
     QZVJQ
    HACRSK
   QOBLCNF
  GWGLXPBL
 BJDUIITFB
RLLTTENZEB
'''

def right_tr():
  '''
  Right oriented Right Triangle
  '''
  height = 10

  print()
  for row in range(height):
    for col in range(height):
      if col >= height - (row + 1):
        put_char()
      else:
        put_blank()
    print()







r'''
========================================================================
Drill 1-7 Write a Python program that prints the following hollow right
triangle pattern (right-side oriented). Use h variable to denote the height.
(Use random & string module to generate random uppercase characters)
========================================================================
e.g. at h = 10:
         F
        PD
       F P
      G  W
     M   N
    T    J
   N     W
  V      F
 R       L
NKKEFGDMAU
'''

def hollow_right_tr():
  '''
  Hollow right oriented Right Triangle
  '''
  height = 10

  print()
  for row in range(height):
    for col in range(height):
      if col == height - (row + 1) or col == height - 1 or row == height - 1:
        put_char()
      else:
        put_blank()
    print()






r'''
========================================================================
Drill 1-8 Write a Python program that prints the following pyramid pattern
Use h variable to denote the height.
(Use random & string module to generate random uppercase characters)
========================================================================
e.g. at h = 10:
         N
        CUO
       HTNUY
      AMNQHGE
     SOPIKVVBN
    OXXOHQSVMGH
   TIAYEKBMCUUFT
  VTHBWFJQRLSPVXR
 VZWXDSAQGMPWJZWDL
YGUNHILFRGVPCSJUUDE
'''

def pyramid():
  '''
  Prints a pyramid pattern
  '''
  height = 5

  print()
  for row in range(height):
    for col in range(2*height):
      if col >= height - (row + 1) and col < height + row:
        put_char()
      else:
        put_blank()
    print()





r'''
========================================================================
Drill 1-9 Write a Python program that prints the following hollow pyramid
pattern. Use h variable to denote the height.
(Use random & string module to generate random uppercase characters)
========================================================================
e.g. at h = 10:
          U
         D K
        I   W
       Y     Y
      T       Z
     G         B
    B           A
   C             E
  I               O
 Z                 B
USQLKVWCMGCOCUDAVJOMU
'''

def hollow_pyramid():
  '''
  Prints a hollow pyramid pattern
  '''
  height = 10

  print()
  for row in range(height):
    for col in range(2*height-1):
      if col == height - (row + 1) or col == height + row - 1 \
      or row == height -1:
        put_char()
      else:
        put_blank()
    print()







r'''
========================================================================
Drill 1-10 Write a Python program that prints the following diamond
pattern. Use h variable to denote the height to center.
(Use random & string module to generate random uppercase characters)
========================================================================
e.g. at h = 5:
     E
    KHZ
   BQFJM
  MGXERZT
 IFQKNKRJQ
KLSMFFJNFNU
 MOGJJJGUB
  HOZACFQ
   VBHCG
    XSX
     A
'''


def diamond():
  '''
  Prints a diamond pattern
  '''
  height = 10

  print()

  # Upper triangle
  for row in range(height):
    for col in range(2*height):
      if col >= height - (row + 1) and col < height + row:
        put_char()
      else:
        put_blank()
    print()

  # Lower triangle
  for row in range(1, height):
    for col in range(2*height-1):
      if col >= row and col < 2*height - 1 - row:
        put_char()
      else:
        put_blank()

    print()




r'''
========================================================================
Drill 1-11 Write a Python program that prints the following hollow diamond
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


def hollow_diamond():
  '''
  Prints a diamond pattern
  '''
  height = 5

  print()

  # Upper triangle
  for row in range(height):
    for col in range(2*height):
      if col == height - (row + 1) or col == height + row - 1:
        put_char()
      else:
        put_blank()
    print()


  # Lower triangle
  for row in range(1, height):
    for col in range(2*height-1):
      if col == row or col == 2*height - row - 2 :
        put_char()
      else:
        put_blank()

    print()


# EXTRA - Box using string multiplication

# height = 10
# width = 50

# print()
# for row in range(height):
#   if row == 0 or row == height - 1:
#     print(put_char()*width)
#   else:
#     print(put_char() + " "*(width-2) + put_char())


