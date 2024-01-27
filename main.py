from pynput import keyboard as kb
import pygame
#pip install pyinstaller
#pyinstaller --onefile name.py

pygame.init()
pygame.mixer.init()
song = pygame.mixer.Sound('song.mp3')
print('HI, WELCOME TO CHECK BUTTONS SCRIPT!')
print('PRESS ANY BUTTON :)')
print('PRESS "q" TO FINISH THE SCRIPT')

class Button:
    def push(button):
        if button == kb.Key.f11:
            print('EUREKA!!!')
        else:
            pygame.mixer.Sound.play(song)


    def release(button): 
        print(button)
        if button == kb.KeyCode.from_char('q'):
            return False
        if button == kb.Key.f11:
            print('EUREKA!!!')

    list = kb.Listener(push,release)
    list.start()

    while list.is_alive():
        pass
            

if __name__ == '__main__':
    Button()
