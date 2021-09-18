from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog as fd
from pathlib import Path

NORMAL_PASTE_CORNERS = (0,0) #placeholder coordinates
WILD_PASTE_CORNERS = (0,0)
NORMAL_SIZE = (0,0)
WILD_SIZE = (0,0)

border_path = Path('\borders\')    
border_list = list(border_path.iterdir)

border_var=tk.StringVar(None,border_list(0))
scaling_var=tk.StringVar(None,'1')

def select_image():
    global image
    image = fd.askopenfile(
        title='Select image file',
        initialdir='\'
     )
     
def process_image():
    border = Image.open(border_path+border_var)
    if "wild" in border_var:
        corners=WILD_PASTE_CORNERS
    else
        corners=NORMAL_PASTE_CORNERS

    border.paste(image, corners)
    image = border
    image = ImageTk.PhotoImage(image)
    #apply current settings to image object
def save_file():
    #apply scaling
    #if single image selected
        #save current working preview image as filename+bordername

#if frames folder does not exist, display error frame "no borders detected! etc"
#on launch, search borders/frames folder for all available borders
#naming convention frame-1, frame-1-JP, wildframe-1, wildframe-1-JP
#maybe convert filenames for readability?
#create list of available borders

window=tk.Tk()
window.resizable(0,0)
window.title("gbcam-border")
main_frame=ttk.Frame()

border_list_widget = ttk.Combobox(window,textvariable=border_var,values=border_list,state="readonly")
border_list_widget.bind('<<ComboboxSelected>>',process_image)
image_preview_widget = ttk.Label(
    image=image
)
image_open_widget = ttk.Button(
  window,
  text='Select an image',
  command=select_file
)

image_save_widget = ttk.Button(
  window,
  text='Save image',
  command=save_file
 )
#palette_select_widget = 
image_preview_widget.pack()
image_open_widget.pack()
border_list_widget.pack()
image_save_widget.pack()

window.mainloop()