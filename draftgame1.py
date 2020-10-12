"""
----A TEXT BASED FIRST-PERSON GAME----
game proceeds according to user reply.
to be modified and updated.
first draft of code, console based ~
"""

import time

"""----console formatting [windows]---"""
from ctypes import windll, create_string_buffer

# stdin handle is -10
# stdout handle is -11
# stderr handle is -12

h = windll.kernel32.GetStdHandle(-12)
csbi = create_string_buffer(22)
res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

if res:
    import struct
    (bufx, bufy, curx, cury, wattr,
     left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    sizex = right - left + 1
    sizey = bottom - top + 1
else:
    sizex, sizey = 80, 25

"""---console formatting ends---"""

import winsound
def beep():
    winsound.Beep(200,1500)


def printer(string):
    print((string+'\n').center(sizex))      #defining print function for game
    time.sleep(.5)

#list of player responses
pos=['yes','y','ok','okay']
Pos=[p.upper() for p in pos]
pos+=Pos
neg=['no','n']
Neg=[n.upper() for n in neg]
neg+=Neg
a=['a','A']
b=['b','B']


"""
Scene 1
"""

printer('Monday, October 18 1977. It is a cold night. Somewhere in the world, the sun in shining, you think.')
printer('You stand outside your home. It is 8 pm and the blinds are drawn.')
printer('A pretty house, this. Flowers nod to you as you stand, ringing the doorbell.')
time.sleep(1)
printer('Welcome home, sunshine.')
printer('You\'re late tonight. The fridge is empty. You could go to bed, or go grab dinner.')
printer('---Will you go to bed?---')
choice1=input('... ')

#goes to bed
if choice1 in pos:
    printer('(You go to bed)')
    printer('1:03 am')
    beep()
    time.sleep(1)
    beep()
    printer('---What is that sound?---')
    printer('(You get out of bed. It comes from behind the curtains.)')
    printer('(Why won\'t the lights turn on?)')
    printer('---You: (a) go to draw the window curtains, OR (b) grab your phone and run downstairs.---')
    choice2=input('... ')

    #goes to window
    if choice2 in a:
        printer('(You draw the curtains.)')
        printer('Where\'d the window go?')
        printer('A soft wind blows, smelling of the sea. But the sea is a thousand miles away. You smile and lean forward, blissfully forgetful.')
        time.sleep(1)
        printer('---the smell of the sea is stronger than ever.---')
        printer('Your hair is wet! You\'re in the sea. You\'re so tired though...')
        printer('A rock in sight! But somebody\'s on it...')
        printer('Do you (a)risk social interaction, or (b)continue swimming to shore?')
        choice3=input('... ')
        if choice3 in a:
            print('That was the ghost of a pirate forsaken in love by a mermaid. Congratulations, you found yoursel

    elif choice2 in b:
        printer('You run.')


#grabs dinner
elif choice1 in neg:
    printer('You should run.')


