from tkinter import *
root = Tk()                           
  
# frame inside root window
frame = Frame(root)                  
  
# geometry method
frame.pack()                          
  
# button inside frame which is 
# inside root
button = Button(frame, text ='SHATHISH')  
button.pack()                         
  
# Tkinter event loop
root.mainloop()        
