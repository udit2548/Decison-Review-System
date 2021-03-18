# Decison-Review-System

In this Cricketing Era, We all know how much important role does DRS(Decision Review System) Technology plays in
Modern Day game.
Following the same idea, I try to imitate the drs technology in python with the help of 
basic GUI techniques(Tkinter Module) and bit of Basics of Image-processing(OpenCv Module), so 
I can experience the role of Third Umpire in order to give correct decisions.

### Task Performed by this software:

1. Basically this software takes a short clip as an input named as 'clip.mp4' as specified in code
and with the help of buttons created with tkinter module the fps(the frame speed per second) is 
varied, so that video can be played in reverse and forward modes in order to give accurate decisions.

2. Then Third Umpire take look at clip by playing at differnet frame rates with the help of buttons 
   created with the help of tkinter.
   
3. Then based on the decison out or not-out button is pressed ,after then Decison pending Image is loaded called as 'decision_pending.jpg' in the software.

4. Then after sponsors of the game i.e 'sponsors.jpg' is loaded in the software.

5. After that finally the decision is shown that whether player is out or not out
  and as a result 'out.jpg' or 'not_out.jpg' depending on the decision made.
   
### You have to install following Python Modules to run the code in your Local Machine:

1. Tkinter is the first module you need in order to implement GUI Interface for the mainwindow.
  It is the inbuilt module so need to install it.
  
2. You need to have PIL(Python Imaging Library) to make tkinter compatible objects to be fit in canvas
  So install by this command - 
  pip install pillow
  
3. For recognising image and analysing the different images and in order to capture the 'clip.mp4'
  you need python module called OpenCv to play with images.
  So install by this command -
  pip install open-cv python
  
4. Python Time module to get information about time.
  Again, Inbulit Module no need to install it.
  
5. Imutils Python Module to resize the images of different dimensions, so that 
  it can become compatible with our created GUI window and can fit into the samescreen.
  So install by this command - 
  pip install imutils
   
    
