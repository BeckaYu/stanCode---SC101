"""
File: babygraphics.py
Name: Rebecca
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # calculate space size
    x_interval = (width-GRAPH_MARGIN_SIZE*2)//len(YEARS)
    # find out the x coordinate according to its year index
    x_coordinates = GRAPH_MARGIN_SIZE + year_index*x_interval
    return x_coordinates


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw 2 horizontal lines that mark the upper and lower boundaries
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # Draw vertical lines that each represent a year
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0,
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, width=LINE_WIDTH)

    # Indicate different years on each intercept of vertical and horizontal line
    for i in range(len(YEARS)):
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    y_interval = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2-1)/1000     # the unit measurement of y coordinate
    y_coordinate_d = {}     # create a dictionary to store data about y coordinate
    # identify the order of the name to assign correspond color
    color_count = 0
    color_index = 0

    for lookup_name in lookup_names:
        if lookup_name in name_data:
            y_coordinate_d[lookup_name] = {}
            for i in range(len(YEARS)):
                if str(YEARS[i]) in name_data[lookup_name]:
                    y_coordinate = int(GRAPH_MARGIN_SIZE)+y_interval*(int(name_data[lookup_name][str(YEARS[i])]))
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, y_coordinate,
                                       text=lookup_name+' '+str(name_data[lookup_name][str(YEARS[i])]),
                                       anchor=tkinter.SW, fill=COLORS[color_index])
                else:
                    y_coordinate = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, y_coordinate,
                                       text=str(lookup_name) + ' ' + str('*'), anchor=tkinter.SW,
                                       fill=COLORS[color_index])
                y_coordinate_d[lookup_name][str(YEARS[i])] = y_coordinate

            for i in range(len(YEARS)-1):
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), y_coordinate_d[lookup_name][str(YEARS[i])],
                                   get_x_coordinate(CANVAS_WIDTH, i+1), y_coordinate_d[lookup_name][str(YEARS[i+1])],
                                   width=LINE_WIDTH, fill=COLORS[color_index])
            color_count += 1
            if color_count % 4 == 0:
                color_index = 0
            if color_count % 4 == 1:
                color_index = 1
            if color_count % 4 == 2:
                color_index = 2
            if color_count % 4 == 3:
                color_index = 3


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
