import time

from art import *

Art = text2art('LOG FILE')
print(Art)

def logs(log):
    ts = time.localtime()
    things = f'{time.strftime("%d-%m-%Y | %H:%M:%S", ts)} >> ' + log
    print(things)
    with open("image.log", "a") as file:
        file.write(f'{things}\n')
