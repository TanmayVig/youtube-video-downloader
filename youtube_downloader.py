from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
from threading import *
from pytube import YouTube
from tkinter.messagebox import askyesno

filewt=0

def downThread():
    thread=Thread(target=downloader)
    thread.start()

def prog_bar(chunk,file_handle, left):
    global download_status
    file_downloaded=filewt-left
    per=(file_downloaded/filewt)*100
    download_status.config(text='{:00.0f}% downloaded'.format(per))

def downloader():
    global filewt, download_status
    download_button.config(state=DISABLED)
    download_status.place(x=230,y=250)
    try:
        url1=url.get()
        path=askdirectory()
        yt=YouTube(url1,on_progress_callback=prog_bar)
        video=yt.streams.filter(progressive=True,file_extension='mp4').first()
        filewt=video.filesize
        video.download(path)
        download_status.config(text='Download Compelete')
        yn=askyesno('Youtube Video Downloader','Do you want to download another video?')
        if yn==1:
            url.delete(0,END)
            download_button.config(state=NORMAL)
            download_status.config(text=' ')
        else:
            root.destroy()
            root.mainloop()
    except Exception as e:
        download_status.config(text='Failed! The video is not found')
root = Tk()
root.geometry('750x400')
root.iconbitmap('logo.ico')

root.resizable(False,False)
root.title("Youtube Video Downloader")
root['bg']='white'
img=Image.open('ytd.png')
img=img.resize((80,80), Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
head=Label(root, image=img)
head.config(anchor=CENTER)
head.pack()
url_=Label(root, text="Enter URL:", bg='white')
url_.config(font=('Helvetica',15))
url_.place(x=50,y=120)
url=Entry(root,width=40, border=2, relief=SUNKEN, font=('Helvetica',15))
url.place(x=170, y=123)
download_button=Button(root,width=160,height=45,bg='white',
                        activebackground='red', command=downThread)
download_button.config(text="Download", width=10, height=3)
download_button.place(x=300,y=170)
download_status=Label(root, text="please wait...",font=('Hevetica',15),bg='white')
name=Label(root,text="Made by- Tanmay Vig", bg='white')
name.place(x=0,y=0)
root.mainloop()
