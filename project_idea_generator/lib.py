from time import sleep
import webbrowser

def try_me():
    input('Hello! What topic would you like your project to be about?\n')
    print('Interesting!\nYour project idea is being generated.')
    for _ in range(3):
        sleep(0.5)
        print('.')
    print('Your project idea is ready to be accessed:')
    webbrowser.open(url="https://youtu.be/dQw4w9WgXcQ?t=42")

try_me()
