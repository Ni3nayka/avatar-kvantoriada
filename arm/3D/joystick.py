import pygame
from time import sleep

pygame.init()
pygame.joystick.init()

def get_information_from_joystick():
    global pygame,joystick
    
    pygame.event.get()
    joystick_count = pygame.joystick.get_count()
    
    mas = [[],[],[]]
    
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
            
        axes = joystick.get_numaxes()
        for i in range( axes ):
            axis = joystick.get_axis( i )
            mas[0].append(axis)
            #if (axis!=0): print("joystick",["Left_X","Left_Y","Right_Y","Right_X"][i], axis)
            
        buttons = joystick.get_numbuttons()
        for i in range( buttons ):
            button = joystick.get_button( i )
            mas[1].append(button)
            #if (button!=0): print("button",i)
            
        hats = joystick.get_numhats()
        for i in range( hats ):
            hat = joystick.get_hat( i )
            mas[2].append(hat)
            #if (hat!=(0,0)): print("arrows",i,hat)
            
    return mas[0],mas[1],mas[2]
            
def destroy_joystick(): pygame.quit()

class my_universal_joystick():
    
    def __init__(self):
        self.joystick = 0
        self.arrow = 0
        self.button = 0
        self.update()
        
    def update(self):
        self.joystick,self.button,self.arrow = get_information_from_joystick()
        return self.joystick,self.button,self.arrow
                
    def destroy(self):
        destroy_joystick()


if __name__ == "__main__":
    controller = my_universal_joystick()
    while True:
        #joystick,button,arrow = controller.update()
        controller.update()
        print("joystick:",controller.joystick,"button:",controller.button,"arrow:",controller.arrow)
        sleep(0.1)
    controller.destroy()