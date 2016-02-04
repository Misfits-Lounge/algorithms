'''gaming basics, pygame
'''


import pygame
import math

# Initialize the game engine
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (800, 600)
#create the window, get the menus out the way and so on
screen = pygame.display.set_mode(size)
#set title caption
pygame.display.set_caption("Artifacts")
#manage how fast the screen updates
clock = pygame.time.Clock()


def draw():
    '''draw a simple rectangle
    '''
    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)
        y_offset = y_offset + 10
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("My text", True, BLACK)
     # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])


def main():
    '''The basic logic and order for each frame of the game:
    While running:
    For each event (keypress, mouse click, etc.):
    Use a chain of if statements to run code to handle each event.
    Run calculations to determine where objects move, what happens when objects collide, etc.
    Clear the screen
    Draw everything
    '''
    #i rather not do denials when using loops
    #e.g. (while not done), but rather positive
    #statements (while running)    
    running = True
    while running:
        for event in pygame.event.get():
            #enable closing of the window
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        #draw whatever i want
        draw2()
        #update the window with what we've drawn through
        #the iteration
        pygame.display.flip()
        #limit the framerate to 60 frames/seconds
        clock.tick(60)
        
    pygame.quit()


if __name__ == '__main__':
    main()
