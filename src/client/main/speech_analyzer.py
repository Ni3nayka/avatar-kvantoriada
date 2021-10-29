'''
https://habr.com/ru/post/529590/
'''
import speech_recognition
from copy import deepcopy

# инициализация инструментов распознавания и ввода речи
recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

current_position_of_manipulator = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]

positions = []

#объявление переменных
d = 0
flag_light = 0
flag_magnet = 0
flag_trajectory = 0
flag_moving = 0
flag_bolt = 0
flag_marker = 0
flag_sponge = 0

def take_bolt():
    flag_bolt = 1
    print("болт взят")

def put_bolt():
    flag_bolt = 0
    print("болт возвращен")

def take_marker():
    flag_marker = 1
    print("маркер взят")

def put_marker():
    flag_marker = 0
    print("маркер возвращен")

def take_sponge():
    flag_sponge = 1
    print("губка взята")
    
def put_sponge():
    flag_sponge = 0
    print("губка возвращенa")

def turn_on_light():
    flag_light = 1
    print("фонарь включен")

def turn_off_light():
    flag_light = 0
    print("фонарь выключен")

def turn_on_magnet():
    flag_magnet = 1
    print("магнит включен")

def turn_off_magnet():
    flag_magnet = 0
    print("магнит выключен")

def remember_position():
    positions.append(deepcopy(current_position_of_manipulator))
    print("позиция запомнена")

def forget_position_1():
    positions[0] = 0
    print("позиция 1 забыта")

def forget_position_2():
    positions.pop(1)
    print("позиция 2 забыта")

def forget_position_3():
    positions.pop(2)
    print("позиция 3 забыта")

def forget_position_4():
    positions.pop(3)
    print("позиция 4 забыта")

def forget_position_5():
    positions.pop(4)
    print("позиция 5 забыта")

def forget_position_6():
    positions.pop(5)
    print("позиция 6 забыта")

def forget_position_7():
    positions.pop(6)
    print("позиция 7 забыта")

def forget_position_8():
    positions.pop(7)
    print("позиция 8 забыта")

def forget_position_9():
    positions.pop(8)
    print("позиция 9 забыта")

def forget_position_10():
    positions.pop(9)
    print("позиция 10 забыта")

def clear_massive():
    positions.clear()
    
def move_to_1_position():
    d = 1
    print("перемещение в позицию 1")
    
def move_to_2_position():
    d = 2
    print("перемещение в позицию 2")
    
def move_to_3_position():
    d = 3
    print("перемещение в позицию 3")
    
def move_to_4_position():
    d = 4
    print("перемещение в позицию 4")
    
def move_to_5_position():
    d = 5
    print("перемещение в позицию 5")
    
def move_to_6_position():
    d = 6
    print("перемещение в позицию 6")
    
def move_to_7_position():
    d = 7
    print("перемещение в позицию 7")
    
def move_to_8_position():
    d = 8
    print("перемещение в позицию 8")
    
def move_to_9_position():
    d = 9
    print("перемещение в позицию 9")
    
def move_to_10_position():
    d = 10
    print("перемещение в позицию 10")

def move_between_points():
    print("перемещение между точками начато")

def start_remembering_trajectory():
    flag_trajectory = 1
    print("запоминание траектории начато")

def move_along_the_trajectory():
    flag_moving = 1
    print("движение по траектории начато")

def stop_moving_along_the_trajectory():
    flag_moving = 0
    
def end_rememberung_trajectory():
    flag_trajectory = 0
    print("запоминание траектории закончено")

#список команд 
comands = [["включить фонарь", turn_on_light],
           ["выключить фонарь", turn_off_light],
           ["включить магнит", turn_on_magnet],
           ["выключить магнит", turn_off_magnet],
           ["удалить запомненные точки", clear_massive],
           ["запомнить позицию", remember_position],
           ["забыть позицию 1", forget_position_1],
           ["забыть позицию 2", forget_position_2],
           ["забыть позицию 3", forget_position_3],
           ["забыть позицию 4", forget_position_4],
           ["забыть позицию 5", forget_position_5],
           ["забыть позицию 6", forget_position_6],
           ["забыть позицию 7", forget_position_7],
           ["забыть позицию 8", forget_position_8],
           ["забыть позицию 9", forget_position_9],
           ["забыть позицию 10", forget_position_10],
           ["перемещение в позицию 1", move_to_1_position],
           ["перемещение в позицию 2", move_to_2_position],
           ["перемещение в позицию 3", move_to_3_position],
           ["перемещение в позицию 4", move_to_4_position],
           ["перемещение в позицию 5", move_to_5_position],
           ["перемещение в позицию 6", move_to_6_position],
           ["перемещение в позицию 7", move_to_7_position],
           ["перемещение в позицию 8", move_to_8_position],
           ["перемещение в позицию 9", move_to_9_position],
           ["перемещение в позицию 10", move_to_10_position],
           ["начать запоминать траекторию", start_remembering_trajectory],
           ["закончить запоминать траекторию", end_rememberung_trajectory],
           ["начать движение по траетории", move_along_the_trajectory],
           ["акончить движение по траектории", stop_moving_along_the_trajectory],
           ["начать перемещение между точками", move_between_points]]

def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        #recognized_data = translate_audio_in_text(audio)
        # использование online-распознавания через Google 
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data

#def arduino_fun():
#    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def record_and_recognize_audio_main():

    while True:
        # старт записи речи с последующим выводом распознанной речи 
        voice_input = record_and_recognize_audio()
        
        #if (voice_input=="включить фонарь"): turn_on_light()
        print("=>",voice_input)

        for i in comands:
            if (voice_input == i[0]):
                try: i[1]()
                except IndexError: pass


if __name__ == "__main__":
    record_and_recognize_audio_main()
    
