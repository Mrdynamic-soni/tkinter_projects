#reading images using os module in python 
from PIL import Image
import time
import glob
image_list = []
path = glob.glob(r"C:\Users\Acer\Pictures\clicks\*.jpg")
for file_name in path:
 im = Image.open(file_name)
 im.show()
 time.sleep(1)
#  image_list.append(im)

#to open a single image 
im = Image.open(r"C:\Users\Acer\Pictures\clicks\rail.jpg")
im.show()