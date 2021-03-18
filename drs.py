# Required Modules and packages.
import tkinter
import cv2
import PIL.Image , PIL.ImageTk
'''In order to execute multiple gui windows same time,
concept of threading is used.'''
import threading
import imutils
import time
from functools import partial

# To capture the video_clip from our local machine.
stream = cv2.VideoCapture("sample-clip.mp4")
flag = True

# Play function to play the video according to variable speed.
def play(speed):
    global flag
    # This statement gives fps(frame speed ) by which player is moving in the clip.
    print(f"the speed is {speed}")
    # Play the video in different frame speeds depending on the speed.
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+speed)

    grabbed , frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(145,26,fill='red',font='Times 26 bold',text='Decision Pending...')
    flag = not flag

# Out function
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon=1
    thread.start()
    print("I made my decision Player is Out")

# Not Out function
def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("I made my decsion player is Not Out")

# Decision Pending function analyses the frames of the decision and gives decision accordingly.
def pending(decision):

    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("decision_pending.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0, image=frame, anchor = tkinter.NW)

    # 2. Wait for 1 second.
    time.sleep(1)

    # 3. Display Sponsor image
    frame = cv2.cvtColor(cv2.imread("sponsors.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 seconds
    time.sleep(1.5)

    # 5. Display out/notout image based on decision
    if decision=="out":
        decisionImg = "out.jpg"
    else:
        decisionImg = "not_out.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

# Width and height of our main screen (GUI Window)
SET_WIDTH = 650
SET_HEIGHT = 368

# Implementation of Tkinter GUI starts here (Main Template starts here.)
window = tkinter.Tk()
window.title("Third Umpire DRS Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text = "<< Previous (fast)",width=50, command=partial(play,-25))
btn.pack()

btn = tkinter.Button(window, text = "<< Previous (slow)",width=50, command=partial(play,-2))
btn.pack()

btn = tkinter.Button(window, text = "Next (slow) >>",width=50, command=partial(play,2))
btn.pack()

btn = tkinter.Button(window, text = "Next (fast) >>",width=50, command=partial(play,25))
btn.pack()

btn = tkinter.Button(window, text = "Give Out",width=50, command = out)
btn.pack()

btn = tkinter.Button(window, text = "Give Not Out",width=50, command=not_out)
btn.pack()

window.mainloop()
