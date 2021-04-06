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
