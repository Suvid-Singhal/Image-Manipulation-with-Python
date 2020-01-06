from PIL import Image
import os

folder = input('Enter the name of folder: ')
os.makedirs(folder+"_processed")
os.chdir(os.getcwd()+"/"+folder)
images = os.listdir()

for Images in images:
    with Image.open(Images) as img:
        width, height = img.size
        if width > 400 and width > height:
            junk = width - 400
            new_width = width - junk
            new_height = height - junk
        else:
            junk = height - 400
            new_height = height - junk
            new_width = width - junk
        img.thumbnail((width, height), Image.ANTIALIAS)
        os.chdir(os.getcwd()+"/../"+folder+"_processed")
        img.save(os.getcwd()+"/"+Images+".jpeg", quality=12, optimize=True)
        os.chdir(os.getcwd()+"/../"+folder)
