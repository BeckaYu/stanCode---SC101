"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    dx = graphics.get_dx()
    dy = graphics.get_dy()
    remain_lives = NUM_LIVES

    # Add the animation loop here!
    # Update
    while True:
        # start dropping the ball only after user make the mouse-click
        if graphics.start:  # if True
            # Stop the game
            if graphics.finished_bricks or remain_lives == 0:
                break

            # Make the ball move in line with the predefined direction
            graphics.ball.move(dx, dy)

            # Check if the ball is collided with bricks and paddles
            graphics.check_collisions()

            # Check if the user has finished all the bricks
            graphics.count_bricks()

            # Check
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window_width:
                dx = -dx
            elif graphics.ball.y <= 0:
                dy = -dy

            # Reset ball position to the staring location
            elif graphics.ball.y + graphics.ball.height >= graphics.window_height:
                graphics.reset_position()   # Reset the ball position when hitting the bottom of the window
                remain_lives -= 1
                graphics.start = False

            # Collide with paddle or bricks
            elif graphics.is_collisions:
                dy = -dy
                graphics.is_collisions = False

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
