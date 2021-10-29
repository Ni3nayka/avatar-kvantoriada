from speech_analyzer import record_and_recognize_audio_main, current_position_of_manipulator, positions, flag_light, flag_magnet, flag_trajectory, flag_moving, flag_bolt, flag_marker, flag_sponge 

from time import sleep
from threading import Thread

class my_audio(Thread):
    
    def __init__(self): 
        Thread.__init__(self)
        self.current_position_of_manipulator = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        self.positions = []
        self.flag_light = 0
        self.flag_magnet = 0
        self.flag_trajectory = 0
        self.flag_moving = 0
        self.flag_bolt = 0
        self.flag_marker = 0
        self.flag_sponge  = 0
    
    def run(self):
        while (1): 
            record_and_recognize_audio_main()

    def update(self):
        self.current_position_of_manipulator = current_position_of_manipulator
        self.positions = positions
        self.flag_light = flag_light
        self.flag_magnet = flag_magnet
        self.flag_trajectory = flag_trajectory
        self.flag_moving = flag_moving
        self.flag_bolt = flag_bolt
        self.flag_marker = flag_marker
        self.flag_sponge  = flag_sponge


if __name__ == "__main__":
    #main()
    print("main")

if __name__ == "__main__":
    audio = my_audio()
    audio.start()