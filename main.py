import list_filters as lf
import os
import sys
import logger
from filters import grayscale
from filters import blur as gblur
from filters import dilate_effect
from filters import zeteam
from filters import message as gmsg
import cv2 as cv

print('')


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

# def call_function():
#     gc.grayscale(image)
#     de.dilate(image)
#     gb.gaussian_blur(image)
#     zt.ze_team(image)
#     msg.message(image, 'coucou')


input_folder = ""
output_folder = ""


args = sys.argv

if len(args) == 1:
    print('Please add arguments')
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
            print(f'{args[nxt_pos + 1]}')
            input_folder = args[nxt_pos + 1]
    except IndexError:
        print('Please enter an input as images folder')
    if '-o' in args:
        next_pos = args.index('-o')
        try:
            if not args[next_pos + 1]:
                print('Please enter an output folder to save images')
            else:
                print(f'{args[next_pos + 1 ]}')
                output_folder = args[next_pos + 1]
                file_types = [".jpg", ".png"]
                files = [entry.name for entry in os.scandir(f'{input_folder}/.') if entry.is_file() and os.path.splitext(entry.name)[1] in file_types]
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
                    img = cv.imread(f'{input_folder}{i}')
                    for item in filtre:
                        if item.startswith('grayscale'):
                            edited = grayscale.grayscale(img)
                        elif item.startswith('zeteam'):
                            edited = zeteam.ze_team(img)
                        elif item.startswith('blur'):
                            number = item.split(':')
                            try:
                                intensity = int(number[1])
                                edited = gblur.gaussian_blur(img, intensity)
                            except IndexError:
                                print('Please enter a value as filter intensity')
                            except ValueError:
                                print('Please enter an int as filter intensity')
                        elif item.startswith('dilate'):
                            number = item.split(':')
                            try:
                                intensity = int(number[1])
                                edited = dilate_effect.dilate(img, intensity)
                            except IndexError:
                                print('Please enter a value as filter intensity')
                            except ValueError:
                                print('Please enter an int as filter intensity')
                        elif item.startswith('message'):
                            number = item.split(':')
                            try:
                                msg = str(number[1])
                                edited = gmsg.message(img, msg)
                            except IndexError:
                                print('Please enter a message as filter value')
            try:
                cv.imwrite(f'{output_folder}__{i}', edited)
            except cv.error:
                print("")