"""
File: sierpinski.py
Name: Rebecca
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Draw a Sierpinski Triangle with designated order
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the recursion times of the Sierpinski triangle
	:param length: float, the side length of the largest Sierpinski triangle
	:param upper_left_x: float, the x-coordinate of the upper-left corner of the triangle
	:param upper_left_y: float, the y-coordinate of the upper-left corner of the triangle
	:return: None, this function draws the triangle on a canvas but does not return a value
	"""
	if order == 0:
		draw_triangle(length, upper_left_x, upper_left_y)
	else:
		# Calculate the height of each triangle
		height = length*0.866

		# Calculate the new length of rach triangle
		length_new = length/2

		# Calculate coordinates for top_left_triangle
		top_left_x = upper_left_x
		top_left_y = upper_left_y

		# Calculate coordinates for top_right_triangle
		top_right_x = upper_left_x + length/2
		top_right_y = upper_left_y

		# Calculate coordinates for bottom_triangle
		bottom_x = upper_left_x + length/4
		bottom_y = upper_left_y + height/2

		# Recursive calls
		sierpinski_triangle(order - 1, length_new, top_left_x, top_left_y)
		sierpinski_triangle(order - 1, length_new, top_right_x, top_right_y)
		sierpinski_triangle(order - 1, length_new, bottom_x, bottom_y)


def draw_triangle(length, upper_left_x, upper_left_y):
	"""
	Draws an equilateral triangle with the given information
	:param length: float, the side length of the triangle
	:param upper_left_x: float, the x-coordinate of the upper-left corner of the triangle
	:param upper_left_y: float, the y-coordinate of the upper-left corner of the triangle
	:return: None, this function draws the triangle on a canvas but does not return a value
	"""
	# Define the height of each triangle
	height = length*0.866

	# Create the vertexes of each triangle
	p1x = upper_left_x
	p1y = upper_left_y
	p2x = upper_left_x + length
	p2y = upper_left_y
	p3x = upper_left_x + length*0.5
	p3y = upper_left_y + height

	# Draw a triangle according to the vertex
	line_up = GLine(p1x, p1y, p2x, p2y)
	line_right = GLine(p2x, p2y, p3x, p3y)
	line_left = GLine(p1x, p1y, p3x, p3y)
	window.add(line_up)
	window.add(line_right)
	window.add(line_left)


if __name__ == '__main__':
	main()

