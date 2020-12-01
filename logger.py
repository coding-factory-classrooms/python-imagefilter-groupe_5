import time

from art import *

Art = text2art('LOGS')
print(Art)

def logs(log):
    '''
    Write each perfomed actions into a log file (named : image.log)
    :param log: The sentence to be entered after the timestamp into the logs
    :return:
    '''
    ts = time.localtime()
    things = f'{time.strftime("%d-%m-%Y | %H:%M:%S", ts)} >> ' + log
    print(things)
    with open("image.log", "a") as file:
        file.write(f'{things}\n')

def open_logs():
    '''
    Open the log file and print his content
    '''
    with open('image.log','r') as logfile:
        content = logfile.read()
        print(content)