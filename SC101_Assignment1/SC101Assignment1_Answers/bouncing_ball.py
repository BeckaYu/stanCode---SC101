"""
File: bouncing_ball.py
Name: Rebecca
-------------------------
This program allows user to drop the ball by clicking the
mouse. The ball will drop and bounce back when hitting the bottom.
The user can click at maximum of three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 0   # Count the times the user click mouse


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global window
    global ball
    global count
    # Create a ball at the starting position
    ball.filled = True
    ball.fill_color = 'orchid'
    ball.color = 'orchid'
    window.add(ball)

    # Start bouncing the ball when user click their mouse
    onmouseclicked(bounce_ball)


def bounce_ball(mouse):
    global window
    global ball
    global count
    vy = 10    # Set the beginning moving speed of y
    pre_y = 500 - START_Y    # Distance between the ball and the ground

    over_three_times = False
    while True:
        if count == 3:
            break
        else:
            # Start dropping the ball
            ball.move(VX, vy)
            pause(DELAY)
            # The ball reach the bottom of the canvas
            if ball.y >= 500-SIZE:
                vy = -vy * REDUCE   # Moving upward. Speed will be reduced by predefined percentage
                pause(DELAY)

            # The ball reach the 1/3 height of its previous height
            elif vy < 0 and ball.y <= pre_y//3:
                vy = -vy    # Moving downward
                pause(DELAY)
                pre_y *= 1.3    # Adjust the actual distance to make the ball bounce higher

            elif ball.x >= 800-SIZE:    # Ball reach to the right-end of the canvas
                window.remove(ball)
                window.add(ball, START_X, START_Y)
                count += 1
                break


if __name__ == "__main__":
    main()
