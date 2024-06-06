from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")


def restart_time():
    os.system("shutdown /r /t 20")


def logout():
    os.system("shutdown -1")


def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Black")

r_button = Button(st, text="Restart", font=("Time New Roman", 26, "bold"), relief=RAISED, cursor="plus",
                  command=restart)
r_button.place(x=280, y=70, height=70, width=190)

rt_button = Button(st, text="Restart Time", font=("Time New Roman", 21, "bold"), relief=RAISED, cursor="plus",
                   command=restart_time)
rt_button.place(x=280, y=210, height=70, width=190)

lg_button = Button(st, text="Log-Out", font=("Time New Roman", 26, "bold"), relief=RAISED, cursor="plus",
                   command=logout)
lg_button.place(x=280, y=350, height=70, width=190)

st_button = Button(st, text="Shut-Down", font=("Time New Roman", 24, "bold"), relief=RAISED, cursor="plus",
                   command=shutdown)
st_button.place(x=280, y=490, height=70, width=190)


st.mainloop()