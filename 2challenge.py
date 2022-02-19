from tkinter import *
import glob
from PIL import Image
import time

root_obj = Tk()

root_obj.geometry("1280x720")
root_obj.title("Imges opener app")
path= glob.glob(r"C:\Users\Acer\Pictures\clicks\*.jpg")
l=0
for file_name in path:
    im = Image.open(file_name)
    im.show()
    time.sleep(1)
    text_label = Label(text="Image"+l)
    

