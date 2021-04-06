```
from karel.stanfordkarel import *

def main():
   move()
   # repeat put_beeper many times 
   for i in range(42):
  	  put_beeper()
   move()
```

```
# Places one beeper in each corner
from karel.stanfordkarel import *
def main():
   # repeat the body 4 times 
   for i in range(4):
	   put_beeper()
	   move()
	   move()
	   move()
	   turn_left()
```

```
# Places five beepers in each corner
from karel.stanfordkarel import *
def main():
   # Repeat once for each corner 
   for i in range(4):
      put_five_beepers()
      move_to_next_corner()

# reposition karel to the next corner 
def move_to_next_corner() :
   move()
   move()
   move()
   turn_left()

# places 5 beepers using a for loop 
def put_five_beepers() :
   for i in range(5):
   	put_beeper()
```

### While Loops

```
# Uses a "while" loop to move Karel until it hits
# a wall. Works on any sized world.
from karel.stanfordkarel import *

# the program starts with main
def main():
   # call the move to wall function
   move_to_wall()

# this is a very useful function 
def move_to_wall():
   # repeat the body while the condition holds
   while front_is_clear():
      move()
```

```
# Uses a while loop to place a line of beepers.
# This program works for a world of any size.
# However, because each world requires one fewer
# moves than put_beepers it always misses a beeper.
from karel.stanfordkarel import *

# program starts at main
def main():
   # repeats until karel faces a wall
   while front_is_clear():
      # place a beeper on current square
      put_beeper()
      # move to the next square
      move()
```

```
# Uses a while loop to place a line of beepers.
# This program works for a world of any size.
from karel.stanfordkarel import *

# program starts at main
def main():
   # repeats until karel faces a wall
   while front_is_clear():
      # place a beeper on current square
      put_beeper()
      # move to the next square
      move()
   # solves the fencepost bug
   put_beeper()
```
