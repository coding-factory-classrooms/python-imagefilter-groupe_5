import time

from art import *

# Art = text2art('LOGS')
# print(Art)

# colors = ["\33[1m", '\33[31m', '\33[34m', '\33[35m', '\33[90m', '\33[91m', '\33[92m', '\33[94m', '\33[95m', '\33[36m']

def logs(log):
    '''
    Write each perfomed actions into a log file (named : image.log)
    :param log: The sentence to be entered after the timestamp into the logs
    :return:
    '''
    ts = time.localtime()
    things = "\033[31m" + f"{time.strftime('%d-%m-%Y | %H:%M:%S', ts)}\033[0m" + " >> " + log
    # print(things)
    with open("image.log", "a") as file:
        file.write(f'{things}\n')

def open_logs(log_file):
    '''
    Open the log file entered as parameter and print his content
    :param log_file: log's file to open
    '''
    logs(f'Display all logs in {log_file}')
    with open(f'{log_file}','r') as logfile:
        content = logfile.read()
        print(content)
