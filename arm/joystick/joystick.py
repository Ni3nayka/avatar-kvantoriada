import pygame

pygame.init()

pygame.display.set_caption("Joystick")

clock = pygame.time.Clock()
 
# Initialize the joysticks
pygame.joystick.init()
    
while True:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
 
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            if (axis!=0): print("joystick",["Left_X","Left_Y","Right_Y","Right_X"][i], axis)
            
        buttons = joystick.get_numbuttons()
 
        for i in range( buttons ):
            button = joystick.get_button( i )
            if (button!=0): print("button",i)
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
 
        for i in range( hats ):
            hat = joystick.get_hat( i )
            if (hat!=(0,0)): print("arrows",i,hat)
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()