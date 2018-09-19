from pynput import keyboard
import time

script_on = False

#Listener
def on_press(key):
    try: k = key.char
    except: k = key.name

    if key == keyboard.Key.esc: 
        return False

    if key == 'F10':
        print("Script toggled")
        script_on = not script_on
        
#Main body
def main():
    #Setting listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while True:
        time.sleep(10)