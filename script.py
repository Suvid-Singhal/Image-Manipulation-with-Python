from PIL import Image
import os

folder = input('Enter the name of folder: ')
os.makedirs(folder+"_processed")
os.chdir(os.getcwd()+"/"+folder)
images = os.listdir()

for Images in images:
    with Image.open(Images) as img:
        width, height = img.size
        if (width > 400 and height > 400) and width > height:
            junk = width - 400
            if junk >= height:
            	print("Oops... Image cannot be resized while maintaining Aspect Ratio...")
            	print("Image name: "+Images)
            	new_width = width
            	new_height = height
            else:
	            new_width = width - junk
	            new_height = height - junk
        elif (width > 400 and height > 400) and height > width:
        	junk = height - 400
        	if junk >= width:
        		print("Oops... Image cannot be resized while maintaining Aspect Ratio...")
        		print("Image name: "+Images)
        		new_width = width
        		new_height = height
        	else:
        		new_width = width - junk
        		new_height = height - junk
        else:
        	print("Oops... Image cannot be resized while maintaining Aspect Ratio...")
        	print("Image name: "+Images)
        	new_height = height
        	new_width = width
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        os.chdir(os.getcwd()+"/../"+folder+"_processed")
        img.save(os.getcwd()+"/"+Images+".jpeg", quality=12, optimize=True)
        os.chdir(os.getcwd()+"/../"+folder)
