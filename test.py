# Import and initialize Pygame
import pygame
import math
import random
# Initialize game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
SKY      = ( 135, 206, 235)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)
GREY     = ( 169, 169, 169)    

# Define pi
PI = 3.141592653

# Open a new window and set window size
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Anna's magische molen")

# Loop until the user clicks the close button.
done = False

angle = 0
angle2 = 3

x1 = 0
x2 = 70

# wolkje start
wolk_x = 0
wolk_y = 20

#speed and direction
wolk_ch_x = 2

# Regen
rain_list = []
for i in range(50):
    x = random.randrange(wolk_x+20, 50)
    y = random.randrange(wolk_y, 400)
    rain_list.append([x, y])

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --------- Main program loop ------------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicks close
            done = True # Flag that we are done so loop is exited

    # --- Game logic here

    # First, clear screen to white. no drawing commands above this
    # that will be erased
    screen.fill(WHITE)

    

    # --- Drawing code here

    # Draw molen

    pygame.draw.rect(screen, GREEN, [0, 400, 700, 500])
    pygame.draw.rect(screen, SKY, [0, 0, 700, 400])
    pygame.draw.polygon(screen, RED, [(250, 400), (300, 230), (400, 230), (450, 400)])
    pygame.draw.polygon(screen, BLUE, [(290, 230), (350, 170), (410, 230)])

    '''
    # Dimensions of the wieken sweep
    #Top left is 250, 100
    # Width/height of 200, 200
    box_dimensions = [250, 100, 200, 200]

    # Outline of circle to 'sweep' the line around
    pygame.draw.ellipse(screen, GREEN, box_dimensions, 2)
    # Black box around circle
    pygame.draw.rect(screen, BLACK, box_dimensions, 2)

    '''
    # --- Wieken

    #Calculate x,y, for the end point of our sweep based on current angle
    x = 125 * math.sin(angle) + 350
    y = 125 * math.cos(angle) + 200

    x2 = 125 * math.sin(angle2) + 350
    y2 = 125 * math.cos(angle2) + 200
    #Draw line from center at 350, 200 to the calculated end spot
    pygame.draw.line(screen, YELLOW, [350, 200], [x,y], 5)
    pygame.draw.line(screen, YELLOW, [350, 200], [x2,y2], 5)
    points = [(350, 170), (x, y), (x+30, y), (x+30, y+70), (350, 170)]
    #pygame.draw.lines(screen, BLUE, False, points, 2)

    #increase the angle by 0.03 radians
    angle = angle + .03
    angle2 = angle2 + .03

    #If done a full sweep, reset the angle to 0
    if angle > 2 * PI:
        angle = angle - 2 * PI
    
    if angle2 > 3 * PI:
        angle2 = angle - 3 * PI

    # --- Wolkje
    pygame.draw.ellipse(screen, GREY, [wolk_x, 50, 70, 50])
    pygame.draw.ellipse(screen, GREY, [wolk_x+30, wolk_y, 60, 50])
    pygame.draw.ellipse(screen, GREY, [wolk_x+50, wolk_y+30, 90, 50])

    wolk_x += wolk_ch_x
    if wolk_x > 570 or wolk_x < 0:
        wolk_ch_x = wolk_ch_x * -1
    '''
    # -- Regen
    for i in range(len(rain_list)):
        pygame.draw.circle(screen, WHITE, rain_list[i], 2)
        rain_list[i][1] += 1
        rain_list[i][0] += wolk_ch_x
    #start vanaf de top wanneer sneew beneden is
        if rain_list[i][1] > 400:
            # reset to just above the top
            y = random.randrange(-wolk_x, -10)
            rain_list[i][1] = y
            # give it a new x position
            x = random.randrange(wolk_x, 50)
            rain_list[i][0] = x
    '''
    # --- Update screen with what is drawn
    pygame.display.flip()

    # --- Limit to 60 fps
    clock.tick(60)
# -- Shutdown Pygame program
pygame.quit()