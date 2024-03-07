from tkinter import *
from PIL import Image,ImageTk



win=Tk()
win.geometry('300x300')
win.config(bg='yellow')
on_pressed=False
def button():
    global on_pressed
    if on_pressed==False:
        
        btn1.config(image=off_photo_img)
        win.config(bg='black')
        label1.config(text='You are in night mode',bg='black',fg='white')
        label.config(image=moon_photo_img)
        on_pressed=True
        
    else:
        
        btn1.config(image=on_photo_img)
        win.config(bg='yellow')
        label1.config(text='You are in day mode',bg='yellow',fg='black')
        label.config(image=sun_photo_img)
        on_pressed = False

on_photo=Image.open('on.png')
on_photo_img=ImageTk.PhotoImage(on_photo, master=win)

off_photo=Image.open('off.png')
off_photo_img=ImageTk.PhotoImage(off_photo, master=win)

sun_photo=Image.open('sun_rise.jpg')
sun_photo_img=ImageTk.PhotoImage(sun_photo, master=win)

moon_photo=Image.open('moon.jpg')
moon_photo_img=ImageTk.PhotoImage(moon_photo, master=win)


btn1=Button(win,image=on_photo_img,command=button,bd=0,bg='yellow')
btn1.pack(padx=50,pady=50)

label=Label(win,image=sun_photo_img)
label.pack(padx=10,pady=10)

label1=Label(win,text="You are in day mode",fg='black',bg='yellow',font=("Arial",15,'bold'))
label1.pack(padx=20,pady=20)


win.mainloop()
