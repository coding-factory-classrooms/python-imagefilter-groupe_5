import os
import sys
import logger
from filters import grayscale, blur as gblur, dilate_effect, zeteam, message as gmsg
import list_filters as lf
import cv2
import configparser
from art import *

print('')
Art = text2art('LOGS')


# DETECTION DES FILTRES --------------------------
filters_types = [".py"]
filtres = [entry.name for entry in os.scandir('filters/') if entry.is_file() and os.path.splitext(entry.name)[1] in filters_types]
# --------------------------------------------------


def help():
    '''
    Display every arguments of the program
    '''
    print('usage : imagefilter\n -h >> Display informations about the function\n -i [folder] >> Enter a folder in pair with this argument to add it as image "image picker"\n -o [folder] >> Enter a folder in pair with this argument to add it as output folder (for saving images)\n --list-filters >> Display all available filters to apply\n --filters [filters] >> Enter filters in pair with this argument to select wanted effect to apply\n Example: --filter "blur:3|dilate:5|grayscale"')
    logger.logs('Display help page')


input_folder = ""
output_folder = ""
args = sys.argv


if len(args) == 1:
    print('Please add arguments')
else:
    if '--config-file' in args:
        conf_file = args.index('--config-file')
        try:
            if not args[conf_file + 1]:
                print('Please enter a config file (.ini)')
            else:
                config = configparser.ConfigParser()
                config.read(args[conf_file + 1])
                input_folder = config['general']['input_dir']
                output_folder = config['general']['output_dir']
                log_file = config['general']['log_file']
                conf_filter = config['filters']['content']
        except IndexError:
            print('Please enter a config file (.ini)')
    elif args[1] == '--list-filters':
        lf.disp_filters()
    elif args[1] == '--log-file':
        try:
            if args[2].endswith('.log'):
                logger.open_logs(args[2])
            else:
                print('Please add .log file as argument')
        except IndexError:
            print('Please enter logfile name as argument')
        except FileNotFoundError:
            print('Please add an existing log file as argument')
    elif args[1] == '-h':
        help()
    elif '-i' in args:
        nxt_pos = args.index('-i')
        try:
            if not args[nxt_pos + 1]:
                print('Please enter an input as images folder')
            else:
                # print(f'{args[nxt_pos + 1]}')
                input_folder = args[nxt_pos + 1]
        except IndexError:
            print('Please enter an input as images folder')
        if '-o' in args:
            next_pos = args.index('-o')
            try:
                if not args[next_pos + 1]:
                    print('Please enter an output folder to save images')
                else:
                    # print(f'{args[next_pos + 1]}')
                    output_folder = args[next_pos + 1]
                    file_types = [".jpg", ".png"]
                    files = [entry.name for entry in os.scandir(f'{input_folder}/.') if
                             entry.is_file() and os.path.splitext(entry.name)[1] in file_types]
            except IndexError:
                print('Please enter an output folder to save images')
            for i in files:
                if '--filters' in args:
                    pos = args.index('--filters')
                    if '--filters' == args[-1]:
                        print('Please add filter to apply')
                    else:
                        id = args[pos + 1]
                        filtre = id.split('|')
                        img = cv2.imread(f'{input_folder}{i}')
                        for item in filtre:
                            if item.startswith('grayscale'):
                                img = grayscale.grayscale(img)
                            elif item.startswith('zeteam'):
                                img = zeteam.ze_team(img)
                            elif item.startswith('blur'):
                                number = item.split(':')
                                try:
                                    intensity = int(number[1])
                                    img = gblur.gaussian_blur(img, intensity)
                                except IndexError:
                                    print('Please enter a value as filter intensity')
                                except ValueError:
                                    print('Please enter an int as filter intensity')
                            elif item.startswith('dilate'):
                                number = item.split(':')
                                try:
                                    intensity = int(number[1])
                                    img = dilate_effect.dilate(img, intensity)
                                except IndexError:
                                    print('Please enter a value as filter intensity')
                                except ValueError:
                                    print('Please enter an int as filter intensity')
                            elif item.startswith('message'):
                                number = item.split(':')
                                try:
                                    msg = str(number[1])
                                    img = gmsg.message(img, msg)
                                except IndexError:
                                    print('Please enter a message as filter value')
                            try:
                                cv2.imwrite(f'{output_folder}__{i}', img)
                            except cv2.error:
                                print("")
    print(f'Edited images saved in {output_folder}\n')
    Question = input('\33[1m' + "Do you want to see the default log file ? (type yes or no): " + '\33[0m')
    if Question == ("yes"):
        print('\33[35m' + f"{Art}" + '\33[0m')
        logger.open_logs('image.log')
    elif Question == ("no"):
        print('\033[91m' + "+1 pour l'input ? :)" + '\033[0m')