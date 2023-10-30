"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10       # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.total_bricks = BRICK_COLS * BRICK_ROWS
        self.counted_bricks = 0
        self.obj = None
        self.ball_radius = ball_radius
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle = GRect(width=self.paddle_width, height=self.paddle_height,
                            x=(self.window_width-self.paddle_width)/2, y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(self.ball_radius*2, self.ball_radius*2,
                          x=(self.window_width-self.ball_radius)/2, y=(self.window_height-self.ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Draw bricks
        # red
        for i in range(brick_cols):
            for j in range(brick_rows//5):
                self.brick_red = GRect(brick_width, brick_height)
                self.brick_red.filled = True
                self.brick_red.fill_color = 'red'
                self.window.add(self.brick_red,
                                x=(brick_spacing + brick_width) * i,
                                y=(brick_offset+(brick_height+brick_spacing)*j))

        # orange
        for i in range(brick_cols):
            for j in range(brick_rows//5):
                self.brick_org = GRect(brick_width, brick_height)
                self.brick_org.filled = True
                self.brick_org.fill_color = 'orange'
                self.window.add(self.brick_org,
                                x=(brick_spacing + brick_width) * i,
                                y=((self.brick_red.y+brick_height+brick_spacing)+(brick_height+brick_spacing)*j))

        # yellow
        for i in range(brick_cols):
            for j in range(brick_rows//5):
                self.brick_yellow = GRect(brick_width, brick_height)
                self.brick_yellow.filled = True
                self.brick_yellow.fill_color = 'yellow'
                self.window.add(self.brick_yellow,
                                x=(brick_spacing + brick_width) * i,
                                y=((self.brick_org.y+brick_height+brick_spacing)+(brick_height+brick_spacing)*j))

        # green
        for i in range(brick_cols):
            for j in range(brick_rows//5):
                self.brick_green = GRect(brick_width, brick_height)
                self.brick_green.filled = True
                self.brick_green.fill_color = 'green'
                self.window.add(self.brick_green,
                                x=(brick_spacing + brick_width) * i,
                                y=((self.brick_yellow.y+brick_height+brick_spacing)+(brick_height+brick_spacing)*j))

        # blue
        for i in range(brick_cols):
            for j in range(brick_rows//5):
                self.brick_blue = GRect(brick_width, brick_height)
                self.brick_blue.filled = True
                self.brick_blue.fill_color = 'blue'
                self.window.add(self.brick_blue,
                                x=(brick_spacing + brick_width) * i,
                                y=((self.brick_green.y+brick_height+brick_spacing)+(brick_height+brick_spacing)*j))

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Define the self.start as False
        self.start = False

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.handle_click)

        # Check for collisions
        self.check_collisions()
        self.is_collisions = False
        self.react_collisions()

        # Reset ball position when ball hit the bottom of the window
        self.reset_position()

        # Finished all the bricks
        self.count_bricks()
        self.finished_bricks = False

    # Reset ball to the starting position
    def reset_position(self):
        self.ball.x = (self.window_width-self.ball_radius)/2
        self.ball.y = (self.window_height-self.ball_radius)/2

    # Check for collisions and react correspondingly
    def check_collisions(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is None:
            if self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y) is None:
                if self.window.get_object_at(self.ball.x, self.ball.y+self.ball_radius*2) is None:
                    if self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2) is None:
                        pass
                    else:
                        self.obj = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2)
                        self.react_collisions()
                else:
                    self.obj = self.window.get_object_at(self.ball.x, self.ball.y+self.ball_radius*2)
                    self.react_collisions()
            else:
                self.obj = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
                self.react_collisions()
        else:
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
            self.react_collisions()

    # React differently with the collision
    def react_collisions(self):
        if self.obj is not None and self.obj != self.paddle:
            self.window.remove(self.obj)
            self.counted_bricks += 1
        self.is_collisions = True

    def count_bricks(self):
        if self.counted_bricks == self.total_bricks:
            self.finished_bricks = True

    # change self.start to True after user click the mouse
    def handle_click(self, event):
        if not self.start:
            self.start = True

    def get_dx(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def get_dy(self):
        self.__dy = INITIAL_Y_SPEED
        return self.__dy

    # Set the position of brick in align with that of the mouse
    def move_paddle(self, mouse):
        if self.paddle_width/2 <= mouse.x <= self.window_width - self.paddle_width/2:
            self.paddle.x = mouse.x - self.paddle_width/2
        elif mouse.x <= self.paddle_width/2:
            self.paddle.x = 0
        elif mouse.x >= self.window_width - self.paddle_width/2:
            self.paddle.x = self.window_width - self.paddle_width

