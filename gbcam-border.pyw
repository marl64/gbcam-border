from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from pathlib import Path

NORMAL_PASTE_CORNERS = (16,16) #placeholder coordinates
WILD_PASTE_CORNERS = (16,40)
#add support for overwriting exisitng borders on a source image?
NORMAL_SIZE = (0,0)
WILD_SIZE = (0,0)

window=tk.Tk()
window.attributes('-toolwindow', True)
window.resizable(0,0)
window.title("gbcam-border")
windowframe = tk.Frame(window)
path = Path.cwd()
border_path = path / 'borders'
border_list = [x.stem for x in border_path.iterdir() if x.is_file()]

global image_obj
image_obj=Image.new(mode='RGB', size=(128,112))
image=ImageTk.PhotoImage(image_obj)
border_var=tk.StringVar(None,border_list[0]) #set initial value to first border
#scaling_list=[x for x in range(1,6)]
#scaling_var=tk.StringVar(None,scaling_list[0])

def select_image():
    global imagename
    global image_obj
    global image
    imagename = fd.askopenfilename(
        title='Select image file'
     )
    if imagename:
        image_obj=Image.open(imagename)
    else:
        return
    image = ImageTk.PhotoImage(image_obj)
    image_preview_widget.configure(image=image)
     
def process_image(self):
    global image_obj
    global image
    border_filename = border_var.get() + '.png'
    border = Image.open(border_path / border_filename).convert('LA')
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

    filename = fd.asksaveasfilename(defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*")), initialfile= Path(imagename).stem + '-' + border_var.get())
    
    if filename:  # asksaveasfile return `None` if dialog closed with "cancel"
        imageout.save(filename)
    else:
        return
    #if single image selected
    #save current working preview image as filename+bordername

#if frames folder does not exist, display error frame "no borders detected! etc"
#on launch, search borders/frames folder for all available borders
#naming convention frame-1, frame-1-JP, wildframe-1, wildframe-1-JP
#maybe convert filenames for readability?
windowframe.pack(padx=10,pady=10)

image_preview_widget = ttk.Label(
    windowframe,
    image=image
)
image_preview_widget.pack()
#create list of available borders
border_list_widget = ttk.Combobox(windowframe,textvariable=border_var,values=border_list,state="readonly")
border_list_widget.bind('<<ComboboxSelected>>',process_image)
border_list_widget.pack()

image_open_widget = ttk.Button(
  windowframe,
  text='Select image',
  command=select_image
)
image_open_widget.pack()
image_save_widget = ttk.Button(
  windowframe,
  text='Save image',
  command=save_file
 )

image_save_widget.pack()
#palette_select_widget = 

window.mainloop()
