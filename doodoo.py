from tkinter import *
from tkinter import filedialog
from pytube import *
import tkinter.font as font
from pytube import YouTube
import shutil

#functions

def select_path():
    #allows user to select path 
    path = filedialog.askdirectory()
    label2.config(text=path)
def download_video():
    get_link = entry.get()
    user_path = label2.cget("text")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    #move file to selected directory
    shutil.move(mp4_video, user_path)
   
# tkinter window   
doodoo_window = Tk()
doodoo_window.title('DooDoo')
doodoo_window.geometry('450x350')

# font
doodoo_font = font.Font(family='Verdana', size=15)
# frame
frame = Frame(doodoo_window, bg='#181616', height='1')
frame.place(relwidth=1, relheight=1)
# entry field
label1 = Label(frame,text='Enter video URL',bg='#181616', fg='#FFFFFF', width='25',height='1')
label1['font'] = doodoo_font
label1.pack(padx=10, pady=10,)
entry = Entry(frame, text="", width='25')
entry.place(relwidth=1, relheight=1)
entry['font'] = doodoo_font
entry.pack(padx=10, pady=10, anchor=N)

# label
label2 = Label(frame,text='Select path for download', bg='#181616', fg='#FFFFFF', width='25',height='1')
label2['font'] = doodoo_font
label2.pack(anchor=CENTER, padx=10, pady=10,)

# buttons
button_1 = Button(text='Download video',
                  fg='#181616',
                  width='15', height='1', 
                  padx=10, pady=10,
                  anchor=CENTER, command=download_video)
button_1['font'] = doodoo_font
button_1.pack(side=BOTTOM, anchor=S,padx=10, pady=10,)
# download_video_button
button_2 = Button(text='Select',
                  fg='#181616',
                  width='15', height='1', 
                  padx=10, pady=10,command=select_path)
button_2['font'] = doodoo_font
button_2.pack(side=BOTTOM, anchor=S,padx=10, pady=10,)

doodoo_window.mainloop()