from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from pathlib import Path

NORMAL_PASTE_CORNERS = (16,16) #placeholder coordinates
WILD_PASTE_CORNERS = (0,0)
NORMAL_SIZE = (0,0)
WILD_SIZE = (0,0)

window=tk.Tk()
window.resizable(0,0)
window.title("gbcam-border")

border_path = Path(r".\\borders\\")
border_list = list(border_path.iterdir())

image_default=Image.new(mode='RGB', size=(128,112))
global image_obj
image_obj=image_default
image_default=ImageTk.PhotoImage(image_default)
image=image_default
border_var=tk.StringVar(None,border_list[0].stem)
#scaling_list=[x for x in range(1,6)]
#scaling_var=tk.StringVar(None,scaling_list[0])

def select_image():
    global imagename
    global image_obj
    global image
    imagename = fd.askopenfilename(
        title='Select image file'
     )
    image_obj=Image.open(imagename)
    image = ImageTk.PhotoImage(image_obj)
    image_preview_widget.configure(image=image)
     
def process_image(self):
    global image_obj
    border = Image.open(border_var.get())
    if "wild" in border_var.get():
        corners=WILD_PASTE_CORNERS
    else:
        corners=NORMAL_PASTE_CORNERS
    border.paste(image_obj, corners)
    image = ImageTk.PhotoImage(border)
    image_preview_widget.configure(image=image)
    
def save_file():
    global image
    imageout=ImageTk.getimage(image)
    #apply scaling

    filename = fd.asksaveasfilename(defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*")))
    if filename is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    imageout.save(filename)
    #if single image selected
    #save current working preview image as filename+bordername

#if frames folder does not exist, display error frame "no borders detected! etc"
#on launch, search borders/frames folder for all available borders
#naming convention frame-1, frame-1-JP, wildframe-1, wildframe-1-JP
#maybe convert filenames for readability?
#create list of available borders
border_list_widget = ttk.Combobox(window,textvariable=border_var,values=border_list,state="readonly")
border_list_widget.bind('<<ComboboxSelected>>',process_image)
image_preview_widget = ttk.Label(
    image=image
)

image_open_widget = ttk.Button(
  window,
  text='Select image',
  command=select_image
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
