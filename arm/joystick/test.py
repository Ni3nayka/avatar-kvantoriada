import pygame
from time import sleep

pygame.init()
#pygame.display.set_caption("Joystick")
pygame.joystick.init()
    
    
def test():
    global pygame,joystick
    
    pygame.event.get()
    joystick_count = pygame.joystick.get_count()
    
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
            
        axes = joystick.get_numaxes()
        for i in range( axes ):
            axis = joystick.get_axis( i )
            if (axis!=0): print("joystick",["Left_X","Left_Y","Right_Y","Right_X"][i], axis)
            
        buttons = joystick.get_numbuttons()
        for i in range( buttons ):
            button = joystick.get_button( i )
            if (button!=0): print("button",i)
            
        hats = joystick.get_numhats()
        for i in range( hats ):
            hat = joystick.get_hat( i )
            if (hat!=(0,0)): print("arrows",i,hat)
    
while True:
 
    
    # For each joystick:
    
        
        
    test()
            
    sleep(0.1)
    
pygame.quit()
