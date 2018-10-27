"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sneeuw")
 
# Loop until the user clicks the close button.
done = False

#snow
snow_list = []
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

#snowman
circ_x = 50
circ_y = 50

#speed and direction
circ_change_x = 5
circ_change_y = 5

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1
    #start vanaf de top wanneer sneew beneden is
        if snow_list[i][1] > 400:
            # reset to just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x

    pygame.draw.circle(screen, WHITE, [circ_x, circ_y], 20)
    pygame.draw.circle(screen, WHITE, [circ_x, circ_y + 60], 50)
    pygame.draw.circle(screen, WHITE, [circ_x, circ_y + 140], 70)

    #animate snowman
    circ_x += circ_change_x
    circ_y += circ_change_y
    if circ_y > 450 or circ_y < 0:
        circ_change_y = circ_change_y * -1
    if circ_x > 650 or circ_x < 0:
        circ_change_x = circ_change_x * -1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(20)
 
# Close the window and quit.
pygame.quit()