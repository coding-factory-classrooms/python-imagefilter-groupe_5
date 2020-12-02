import list_filters as lf
import os
import sys
import logger
from filters import grayscale as gc, dilate_effect as de, blur as gb, zeteam as zt

# DETECTION DES FICHIERS IMAGE ------------------
file_types = [".jpg",".png",]
files = [entry.name for entry in os.scandir('data/imgs/.') if entry.is_file() and os.path.splitext(entry.name)[1] in file_types]
# ------------------------------------------------
# DETECTION DES FILTRES --------------------------
filters_types = [".py"]
filtres = [entry.name for entry in os.scandir('filters/') if entry.is_file() and os.path.splitext(entry.name)[1] in filters_types]
print(filtres)
# --------------------------------------------------
def help():
    print('usage : imagefilter\n -h >> Display informations about the function\n -i [folder] >> Enter a folder in pair with this argument to add it as image "image picker"\n -o [folder] >> Enter a folder in pair with this argument to add it as output folder (for saving images)\n --list-filters >> Display all available filters to apply\n --filters [filters] >> Enter filters in pair with this argument to select wanted effect to apply\n Example: --filter "blur:3|dilate:5|grayscale"')
    logger.logs('Display help page')

# def call_function():
#     gc.grayscale(image)
#     de.dilate(image)
#     gb.gaussian_blur(image)
#     zt.ze_team(image,'Leonard Allan Mael')

# for i in files:
#     image = i
    # print(i)



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
elif '--filters' in args:
    pos = args.index('--filters')
    if '--filters' == args[-1]:
        print('Please add filter to apply')
    else:
        id = args[pos+1]
        filtre = id.split('|')
        for check in filtre:
            print(check)
            for f in filtres:
                if check in f:
                    print('coucou')
                    break
                else:
                    print('test')
                    break

