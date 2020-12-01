from filters import gray_color as gc, blur as gb, dilate_effect as de, zeteam as zt
import os

# DETECTION DES FICHIERS IMAGE ------------------
file_types = [".jpg",".png",]
files = [entry.name for entry in os.scandir('data/imgs/.') if entry.is_file() and os.path.splitext(entry.name)[1] in file_types]
print(f'Les fichiers transformables sont : {files}')
# ------------------------------------------------

def call_function():
    gc.grayscale(image)
    de.dilate(image)
    gb.gaussian_blur(image)
    zt.ze_team(image,'coucou')



for i in files:
    image = i
    call_function()


