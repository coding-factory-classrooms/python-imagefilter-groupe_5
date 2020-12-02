import os
import logger

file_types = [".py"]
files = [entry.name for entry in os.scandir('filters/') if entry.is_file() and os.path.splitext(entry.name)[1] in file_types]

description = ""

def disp_filters():
    '''
    Search in an array of each filters, remove the .py then display it.
    '''
    logger.logs('Display filters list')
    print('----------')
    for i in files:
        image = i
        if image == 'blur.py':
            description = 'Apply an blur effect on pictures (works with int to configure the intensity of the filter)'
            print(f'{image.replace(".py", "")}' + ' >> ' + f'{description}')
        elif image == 'dilate_effect.py':
            description = "Apply an dilatation effect on pictures (works with int to configure the intensity of the filter)"
            print(f'{image.replace(".py", "")}' + ' >> ' + f'{description}')
        elif image == 'grayscale.py':
            description = 'Apply a black and white effect on pictures'
            print(f'{image.replace(".py", "")}' + ' >> ' + f'{description}')
        elif image == 'message.py':
            description = 'Enter a message to display on pictures (works with a string to configure the message)'
            print(f'{image.replace(".py", "")}' + ' >> ' + f'{description}')
        elif image == 'zeteam.py':
            description = 'Apply our team effect on pictures (Display our names on the pictures)'
            print(f'{image.replace(".py", "")}' + ' >> ' + f'{description}')
        print('----------')