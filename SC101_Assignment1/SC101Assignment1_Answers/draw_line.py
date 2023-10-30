"""
File: draw_line.py
Name: Rebecca
-------------------------
This program allows user to draw line by clicking the mouse.
The first click will generate a circle that marks the beginning position of the line.
The position of the second click will become the ending position of the line.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
# Radius of the circle
SIZE = 30

# Global variable
window = GWindow()  # Create canvas
count = 0   # Count the total times of the clicks

# Record the hollow circle
hollow_circle = None
hollow_x = 0
hollow_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click_count)


def click_count(mouse):
    global count
    if count % 2 == 0:
        create_hollow_circle(mouse)
    else:
        draw_line(mouse)
    count += 1


def create_hollow_circle(mouse):
    global hollow_circle
    global hollow_x
    global hollow_y
    # Create hallow circle when user clicks for odd times
    hollow_circle = GOval(SIZE, SIZE)
    hollow_circle.filled = False
    hollow_circle.color = 'black'
    window.add(hollow_circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
    hollow_x = mouse.x-SIZE/2
    hollow_y = mouse.y-SIZE/2


def draw_line(mouse):
    global hollow_circle
    global hollow_x
    global hollow_y
    # Create a line and remove the hollow circle when use clicks for even times
    line = GLine(hollow_x, hollow_y, mouse.x, mouse.y)
    window.add(line)
    if hollow_circle is not None:
        window.remove(hollow_circle)


if __name__ == "__main__":
    main()
