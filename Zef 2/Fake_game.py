import pygame, pygame.transform, pygame.image
from operator import *
from pygame.surfarray import *
from pygame.locals import *
from Numeric import *

# ------------------------------------------------------------------------------------
# Glob decs

# Screen resolution...
RES 	= array((640,480))

# ------------------------------------------------------------------------------------
def main():
    "Inisalises display, precalculates the cosine values, and controls the update loop"
    
    # Initialise pygame, and grab an 8bit display.
    pygame.init()
    screen_surface = pygame.display.set_mode(RES, 0, 8)

    # Load a source image, and convert it to a surfarray...
    image = pygame.image.load("monty.gif")
    image_buff = pygame.surfarray.array2d(image)

    # Numeric array (working) for the display. Do all our fun stuff here...
    rot_buffer  = zeros(RES/8)
    
    # Pygame Surface object which will take the surfarray data and be translated into a screen blit... 
    rot_surface = pygame.Surface((RES[0]/8, RES[1]/8), 0, 8)
        
    # apply the same palette to plasma_surface
    rot_surface.set_palette(image.get_palette())

    # Setup our parameters for calling the roto_zoom function...
    angle = 0.1
    scale = 2
    surface_x = RES[0]/8
    surface_y = RES[1]/8
    image_x = image.get_width()
    image_y = image.get_height()

    # Angle incrementor
    inc = 0.1

    # Zoom up or down...
    dir = 0

    # Fruity loops...
    while 1:
    
        # Have we received an event to close the window?
        for e in pygame.event.get():
            if e.type in (QUIT,KEYDOWN,MOUSEBUTTONDOWN):
                return

	# Call the roto_zoom function, blit a scaled surfarray to the screen and display it..            
	# We mod the angle to keep it in bounds...
	rot_buffer = roto_zoom(rot_buffer, image_buff, mod(angle,360), scale, surface_x, surface_y, image_x, image_y) 
	blit_scaled_surface(screen_surface, rot_buffer, rot_surface)
	pygame.display.update()

        # Increment the angle for the next iteration
    	angle += inc

        # Check the scale is in bounds, and increment or decrement accordingly...
	if(dir):
	    scale -= 0.1
	    if(scale <= 0):
		dir = 0
        else:
	    scale += 0.1
            if(scale >= 4):
            	dir = 1
            
# ------------------------------------------------------------------------------------
def roto_zoom(dest, src, angle, scale, x_size, y_size, x_mask, y_mask):
    """ Function to rotate and scale a supplied surfarray, filling the screen with the results..."""
 
    # Our initial positions in the source surfarray
    src_x = 0.0
    src_y = 0.0

    # Our initial positions in the destination surfarray
    dest_x = 0
    dest_y = 0

    # The "delta" values for incrementing the position of src_x & src_y
    dx = 0.0
    dy = 0.0

    # Src_x & src_y will be initialised to start_x and start_y at the beginning of each newline
    start_x = 0.0
    start_y = 0.0

    # Calculate the increments we need for the source bitmap everytime we move right a pixel in the destination
    dx = cos(angle) * scale
    dy = sin(angle) * scale

    # For each row in the destination
    for dest_y in range(0,y_size):
       
        # Set the position in the source to the start of this line
	src_x = start_x
	src_y = start_y
	
	# For each pixel in the row...
	for dest_x in range(0,x_size):
		
		# copy a pixel from the source to the desitination
		# We mod the src_x/y vars to keep them in bounds of the source image...
		dest[dest_x][dest_y] = src[mod(int(src_x),x_mask)][mod(int(src_y),y_mask)]

		# Increment the source positions by our calculated increments...
		src_x += dx
		src_y += dy

	# Change the starting positions for the next line (this is a dot product I think...)
    	start_x -= dy
   	start_y += dx

    # Return the surfarray for blitting...
    return dest


# ------------------------------------------------------------------------------------
def blit_scaled_surface(screen, flame, miniflame):
    "double the size of the data, and blit to screen -- Nicked from Shread's Fast Flame"
    blit_array(miniflame, flame)
    s2 = pygame.transform.scale(miniflame, screen.get_size())
    screen.blit(s2, (0,0))

# Shit captain! In the void of space we're all alone...
# Don't worry ensign. I have a plan: Fire our trippy laser!
if __name__ == '__main__': main()
