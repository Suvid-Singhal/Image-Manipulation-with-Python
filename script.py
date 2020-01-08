from PIL import Image
import os

folder = input('Enter the name of folder: ')
os.makedirs(folder+"_processed")
os.chdir(os.getcwd()+"/"+folder)
images = os.listdir()

for Images in images:
    path = os.getcwd()+"/"+Images
    filename, file_extension = os.path.splitext(path)
    with Image.open(Images) as img:
        width, height = img.size
        if width > height:
            new_width  = 400
            new_height = round(new_width * height / width)
        else:
            new_height = 400
            new_width = round(new_height * width / height)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        os.chdir(os.getcwd()+"/../"+folder+"_processed")
        img.save(os.getcwd()+"/"+Images, quality=12, optimize=True)
        os.chdir(os.getcwd()+"/../"+folder)
