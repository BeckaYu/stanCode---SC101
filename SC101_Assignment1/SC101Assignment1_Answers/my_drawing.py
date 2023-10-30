"""
File: my_drawing.py
Name: Rebecca
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Moonlight Sea

    I currently live in Taitung.
    Moonlight sea is one of the must-see here.
    It is extremely stunning and I love it!
    """
    window = GWindow(width=800, height=500, title='moonlight_sea')

    # Ocean
    ocean = GRect(800, 200, x=0, y=300)
    ocean.filled = True
    ocean.fill_color = 'midnightblue'
    ocean.color = 'midnightblue'
    window.add(ocean)

    # Darksky
    darksky = GRect(800, 300, x=0, y=0)
    darksky.filled = True
    darksky.fill_color = 'black'
    darksky.color = 'black'
    window.add(darksky)

    # moon
    moon_r = GArc(800, 500, 0, 90)
    moon_r.filled = True
    moon_r.fill_color = 'navajowhite'
    moon_r.color = 'navajowhite'
    window.add(moon_r, x=200, y=170)

    moon_l = GArc(800, 500, 90, 90)
    moon_l.filled = True
    moon_l.fill_color = 'navajowhite'
    moon_l.color = 'navajowhite'
    window.add(moon_l, x=200, y=170)

    # moonlight
    moonlight_r1 = GArc(800, 500, 270, 90)
    moonlight_r1.filled = False
    moonlight_r1.color = 'navajowhite'
    window.add(moonlight_r1, x=200, y=170)

    moonlight_r2 = GArc(800, 300, 270, 90)
    moonlight_r2.filled = False
    moonlight_r2.color = 'navajowhite'
    window.add(moonlight_r2, x=200, y=230)

    moonlight_r3 = GArc(800, 200, 270, 90)
    moonlight_r3.filled = False
    moonlight_r3.color = 'navajowhite'
    window.add(moonlight_r3, x=200, y=250)

    moonlight_l1 = GArc(800, 500, 180, 90)
    moonlight_l1.filled = False
    moonlight_l1.color = 'navajowhite'
    window.add(moonlight_l1, x=200, y=170)

    moonlight_l2 = GArc(800, 300, 180, 90)
    moonlight_l2.filled = False
    moonlight_l2.color = 'navajowhite'
    window.add(moonlight_l2, x=200, y=230)

    moonlight_l3 = GArc(800, 200, 180, 90)
    moonlight_l3.filled = False
    moonlight_l3.color = 'navajowhite'
    window.add(moonlight_l3, x=200, y=250)

    # star
    star_1 = GLine(50, 50, 80, 80)
    star_1.color = 'whitesmoke'
    window.add(star_1)

    star_2 = GLine(50, 80, 80, 50)
    star_2.color = 'whitesmoke'
    window.add(star_2)

    star_3 = GLine(50, 65, 80, 65)
    star_3.color = 'whitesmoke'
    window.add(star_3)


if __name__ == '__main__':
    main()
