## Reeborg's World Game
## Link: "https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"

## Given Functions
# move()
# turn_left()
# front_is_clear()
# wall_in_front()
# right_is_clear()
# wall_on_right()
# at_goal()

## Hints - Use...
# while()
# if/elif/else()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
