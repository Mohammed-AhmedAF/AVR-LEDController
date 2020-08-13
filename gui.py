#!/bin/env python3
import platform
from tkinter import *
from tkinter import ttk
from functools import partial
import serial

ser = serial.Serial()
baudrate = 0
serialPort = str()

root = Tk()
root.title("4 LEDs controller")
root.resizable(width=True,height=False)

connectionFrame = LabelFrame(root,text="Connection",padx=10,pady=5)
connectionFrame.grid(row=0,column=3,padx=10,pady=10,stick=N+S)
controlFrame = LabelFrame(root,text="Control",padx=10,pady=5)
statusLabel = Label(root,text="",relief=SUNKEN,anchor=W)


def updateStatusbar(message):
    statusLabel['text'] = message

#Connection elements
portLabel = Label(connectionFrame,text="Port: ")
baudrateLabel = Label(connectionFrame,text="Baudrate: ")
baudrateCmbox = ttk.Combobox(connectionFrame,width="20",state="readonly")
baudrateCmbox['values'] = [9600,19200,38400,57600,115200]
baudrateCmbox.current(0)

#Control elements

led1Timer = ttk.Combobox(controlFrame,width="10",state="readonly")
led1Timer['values'] = ['1','3','5','9','12']
led1Timer.grid(row=1,column=0)
led1Timer.current(0)

led2Timer = ttk.Combobox(controlFrame,width="10",state="readonly")
led2Timer['values'] = ['1','3','5','9','12']
led2Timer.grid(row=1,column=1)
led2Timer.current(0)

led3Timer = ttk.Combobox(controlFrame,width="10",state="readonly")
led3Timer['values'] = ['1','3','5','9','12']
led3Timer.grid(row=1,column=2)
led3Timer.current(0)


led4Timer = ttk.Combobox(controlFrame,width="10",state="readonly")
led4Timer['values'] = ['1','3','5','9','12']
led4Timer.grid(row=1,column=3)
led4Timer.current(0)

def sendToggleSignal(id):
    if (id == 'a'):
        time = int(led1Timer.get()).to_bytes(1,'little')
    elif (id == 'b'):
        time = int(led2Timer.get()).to_bytes(1,'little')
    elif (id == 'c'):
        time = int(led3Timer.get()).to_bytes(1,'little')
    elif (id == 'd'):
        time = int(led4Timer.get()).to_bytes(1,'little')


    try:
        ser.write(id.encode())
        ser.write(time)
        ser.write(b't')
        ser.write(b't')
        updateStatusbar("Sent " + id)
    except:
        updateStatusbar("Unable to send " + id)


toggleLED1Btn = Button(controlFrame,text="Toggle 1",width="10",command=partial(sendToggleSignal,'a'))
toggleLED2Btn = Button(controlFrame,text="Toggle 2",width="10",command=partial(sendToggleSignal,'b'))
toggleLED3Btn = Button(controlFrame,text="Toggle 3",width="10",command=partial(sendToggleSignal,'c'))
toggleLED4Btn = Button(controlFrame,text="Toggle 4",width="10",command=partial(sendToggleSignal,'d'))

#Port values defined based on OS
if not (platform.system().startswith("Win")):
    port = ["/dev/ttyUSB0","Other"]
else:
    port = ["COM3","COM4"]

portCmbox = ttk.Combobox(connectionFrame,values=port,state="readonly")
portCmbox.current(0)

def updateStatusbar(message):
    statusLabel['text'] = message

def connectByUART():
   #Establishing serial connection
    global ser
    global baudrate
    global serialPort

    #Checking if there is a connection already or establish connection
    if not ser.is_open:
        try:
            baudrate = baudrateCmbox.get()
            serialPort = portCmbox.get()
            ser = serial.Serial(serialPort,baudrate)
            updateStatusbar("Connection established!" + " Baudrate: "+str(baudrateCmbox.get()) + " on " + serialPort)
        except:
            updateStatusbar("Could not establish connection "  + "on " + serialPort + " with baudrate " + str(baudrateCmbox.get()))
    else:
        if baudrate!=baudrateCmbox.get() or serialPort!=portCmbox.get():
            try:
                baudrate = int(baudrateCmbox.get())
                ser.close()
                connectByUART()
            except:
                updateStatusbar("No connection handle")
        else:
                updateStatusbar("Already connected!")

def sendStopWatch():
    try:
        sendFrame(['s','s','s','s'])
        updateStatusbar("Stop signal sent")
    except:
        updateStatusbar("Error sending stop signal")


connectBtn = Button(connectionFrame,text="Connect",padx=10,pady=5,command=connectByUART)

statusLabel.grid(row=1,column=0,columnspan=3,sticky=E+W,padx=10)

#Connection elements placements
connectBtn.grid(row=2,column=0,sticky=W+E,pady=5)
portLabel.grid(row=0,column=0,stick=W)
baudrateLabel.grid(row=1,column=0,sticky=W)
baudrateCmbox.grid(row=1,column=1)
portCmbox.grid(row=0,column=1,sticky=W+E)

#Control elements placements
controlFrame.grid(row=0,column=0,padx=10,pady=10,sticky=N+S)
toggleLED1Btn.grid(row=0,column=0,padx=10,pady=10,sticky=N+S)
toggleLED2Btn.grid(row=0,column=1,padx=10,pady=10,sticky=N+S)
toggleLED3Btn.grid(row=0,column=2,padx=10,pady=10,sticky=N+S)
toggleLED4Btn.grid(row=0,column=3,padx=10,pady=10,sticky=N+S)

root.mainloop()
