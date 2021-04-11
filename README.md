

|Command|	Description|
|---|---|
|move()|	Asks Karel to move forward one block. Karel cannot respond to a move() command if there is a wall blocking its way.|
|turn_left()|	Asks Karel to rotate 90 degrees to the left (counterclockwise).|
|pick_beeper()|	Asks Karel to pick up one beeper from a corner and stores the beeper in its beeper bag, which can hold an infinite number of beepers. Karel cannot respond to a pick_beeper() command unless there is a beeper on the current corner.|
|put_beeper()|	Asks Karel to take a beeper from its beeper bag and put it down on the current corner. Karel cannot respond to a put_beeper() command unless there are beepers in its beeper bag.|



|Test|Opposite|What it checks|
|---|---|---|
|front_is_clear()	|front_is_blocked()	|Is there a wall in front of Karel?|
|beepers_present()	|no_beepers_present()	|Are there beepers on this corner?|
|left_is_clear()|	left_is_blocked()	|Is there a wall to Karel’s left?|
|right_is_clear()|	right_is_blocked()|	Is there a wall to Karel’s right?|
|beepers_in_bag()	|no_beepers_in_bag()|	Does Karel have any beepers in its bag?|
|facing_north()|	not_facing_north()|	Is Karel facing north?|
|facing_south()|	not_facing_south()	|Is Karel facing south?|
|facing_east()	|not_facing_east()|	Is Karel facing east?|
|facing_west()	|not_facing_west()|	Is Karel facing west?|

Karel also has the ability to paint corners in its world with the following colors:
```
BLANK, which removes any color on the square
BLACK
BLUE
CYAN
DARK_GRAY
GRAY
GREEN
LIGHT_GRAY
MAGENTA
ORANGE
PINK
RED
WHITE
YELLOW
```

|Command|	What it does|
|---|---|
|paint_corner(COLOR_NAME)|	Karel colors the corner he's standing on COLOR_NAME. For example, to color the corner blue, you would write paint_corner(BLUE).|
|corner_color_is(COLOR_NAME)|	A condition checking this question: Is the color of the corner Karel is standing on COLOR NAME?|

