#importing libraries
from tkinter import Label, Tk
import time

#defining title and size of the application
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(0,0) #(1,1) can be used to minimize and maximize the clock

#defining font,color and width
text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
border_width = 25

#combining all the elements to define the label of clock allicn
label = Label(app_window, font = text_font, bg = background, bd = border_width)
label.grid(row = 0, column = 1)

#defineing main fun
#setting text of the label as realtime
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text = time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
