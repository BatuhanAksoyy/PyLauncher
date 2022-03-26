import ctypes
import json
import re
import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo
import time
import os
import keyboard

HideState = False
def start(): #Starts the game with saving all the information.
  global HideState
  name = UsernameEntry.get()
  version = VersionComboBox.get()
  path = PathEntry.get()
  width = WidthEntry.get()
  height = HeightEntry.get()
  ram = RamComboBox.get()
  hidestate = HideState
  #Exceptions
  if name == "":
    ctypes.windll.user32.MessageBoxW(0, "Please enter username ", "Error", 16)
    return
  elif len(name) < 4:
    ctypes.windll.user32.MessageBoxW(0, "Please enter a valid username ", "Error", 16)
    return
  elif len(name) > 16:
    ctypes.windll.user32.MessageBoxW(0, "Please enter a valid username ", "Error", 16)
    return
  elif path == "":
    ctypes.windll.user32.MessageBoxW(0, "Please enter a valid path ", "Error", 16)
    return
  elif version == "":
    ctypes.windll.user32.MessageBoxW(0, "Please enter a valid version ", "Error", 16)
    return
  elif height == "":
    ctypes.windll.user32.MessageBoxW(0, "Please enter a valid height ", "Error", 16)
    return
  elif width == "":
    ctypes.windll.user32.MessageBoxW(0, "Please enter a valid width ", "Error", 16)
    return
  JsonText = {
    "Name": name,
    "Version": version,
    "Path": path,
    "Width": width,
    "Height": height,
    "Ram": ram,
    "HideState": hidestate
  }
  dumpedtext = json.dumps(JsonText)
  jsonFile = open("LauncherInformation.json","w")
  jsonFile.write(dumpedtext)
  jsonFile.close()
  os.startfile("startmc.exe")
def SaveInformation():
    global HideState
    name = UsernameEntry.get()
    version = VersionComboBox.get()
    path = PathEntry.get()
    width = WidthEntry.get()
    height = HeightEntry.get()
    ram = RamComboBox.get()
    hidestate = HideState
    JsonText = {
        "Name": name,
        "Version": version,
        "Path": path,
        "Width": width,
        "Height": height,
        "Ram": ram,
        "HideState": hidestate
    }
    dumpedtext = json.dumps(JsonText)
    jsonFile = open("LauncherInformation.json", "w")
    jsonFile.write(dumpedtext)
    jsonFile.close()
def KillConsole():
    os.system("taskkill /im startmc.exe")
def OffConsole():
    global HideState
    HideState = True
    CheckBoxLabel.configure(fg="red")
    SaveInformation()
def OnConsole():
    global HideState
    HideState = False
    CheckBoxLabel.configure(fg="green")
    SaveInformation()
def select_file(): #browse directories
    curdir = filedialog.askdirectory(initialdir=str(os.getenv('APPDATA')))
    PathEntry.delete(0,tkinter.END)
    PathEntry.insert(0,str(curdir))
def restriction(input): #username special character restriction
    # You can't delete first element of the string. I couldn't figure out yet ill do that in the future.
    pattern = r'^[a-zA-Z0-9_]+$'
    if re.fullmatch(pattern, input) is None:
        return False
    else:
        return True

Window = Tk()
Window.geometry("800x600")
Window.configure(bg="#363333")
Window.title("PyLauncher")
dir = str(os.getcwd()) + "\\icon.ico"
Window.iconbitmap(dir)
buttonlogo = PhotoImage(file=f"Background.png")
Title = tkinter.Label(Window,text="PyLauncher",font=("Roboto",32),bg="#363333",fg="#E16428").place(relx=.5,rely=.1,anchor="center")
but2 = tkinter.Button(Window,image=buttonlogo,background="#363333",highlightcolor="#363333",highlightthickness=0,bd=0,borderwidth=0,activeforeground="#363333",activebackground="#363333",command=start)
but2.place(anchor="center",rely=0.37,relx=.69)
VersionList = open("VersionList.txt","r").read()
Username = tkinter.Label(Window,text="Username",font=("Roboto",20),bg="#363333",fg="white").place(relx=.5,rely=0.28,anchor="center")
SETTINGS = tkinter.Label(Window,text="Settings",font=("Roboto",20),bg="#363333",fg="white").place(relx=.5,rely=.55,anchor="center")
RAM = tkinter.Label(Window,text="Ram",font=("Roboto",17),bg="#363333",fg="white").place(relx=.3,rely=0.67,anchor="center")
PATH = tkinter.Label(Window,text="Path",font=("Roboto",17),bg="#363333",fg="white").place(relx=.648,rely=0.67,anchor="center")
VERSION = tkinter.Label(Window,text="Version",font=("Roboto",17),bg="#363333",fg="white").place(relx=.46,rely=0.67,anchor="center")
Width = tkinter.Label(Window,text="Width",font=("Roboto",17),bg="#363333",fg="white").place(relx=.3,rely=0.83,anchor="center")
Height = tkinter.Label(Window,text="Height",font=("Roboto",17),bg="#363333",fg="white").place(relx=.46,rely=0.83,anchor="center")
ATTENTION = tkinter.Label(Window,text="Please enter a specific value *(1600x900).",font=("Roboto",10),bg="#363333",fg="orange").place(relx=.7,rely=0.90,anchor="center")
CheckBoxLabel = tkinter.Label(Window,text="Console Toggle",font=("Roboto",10),bg="#363333",fg="green")
KillConsoleLabel = tkinter.Label(Window,text="Kill Console",font=("Roboto",12),bg="#363333",fg="white")
CheckBoxLabel.place(relx=.61,rely=0.829,anchor="center")
KillConsoleLabel.place(anchor="center",relx=.11,rely=0.96)
TextBox = PhotoImage(file=f"TextBox.png")
Image = tkinter.Label(Window, image = TextBox,bg="#363333").place(relx=.5,rely=0.37,anchor="center") #this is image for username
onlogo = PhotoImage(file=f"On.png")
offlogo = PhotoImage(file=f"Off.png")
killlogo = PhotoImage(file=f"kill.png")
KillButton = tkinter.Button(Window,image=killlogo,background="#363333",highlightcolor="#363333",highlightthickness=0,bd=0,borderwidth=0,activeforeground="#363333",activebackground="#363333",command=KillConsole)
OnButton = tkinter.Button(Window,image= onlogo,bg="#363333",highlightcolor="#363333",highlightbackground="#363333",highlightthickness=0,bd=0,activeforeground="#363333",activebackground="#363333",command=OnConsole)
OffButton = tkinter.Button(Window,image= offlogo,bg="#363333",highlightcolor="#363333",highlightbackground="#363333",highlightthickness=0,bd=0,activeforeground="#363333",activebackground="#363333",command=OffConsole)
Pathbutton = tkinter.Button(Window,image=buttonlogo,background="#363333",highlightcolor="#363333",highlightthickness=0,bd=0,borderwidth=0,activeforeground="#363333",activebackground="#363333",command=select_file)
OnButton.place(anchor="center",relx=.70,rely=0.829)
OffButton.place(anchor="center",relx=.74,rely=0.829)
Pathbutton.place(anchor="center",rely=0.749,relx=.79)
KillButton.place(anchor="center",relx=.03,rely=0.958)
validation = Window.register(restriction)
UsernameEntry = tkinter.Entry(Window,width=25,borderwidth=0,border=0,font=("Roboto",12),validate="key",validatecommand=(validation,'%P'))
PathEntry = tkinter.Entry(Window,width=25,font=("Roboto",10))
WidthEntry = tkinter.Entry(Window,width=15,font=("Roboto",10))
HeightEntry = tkinter.Entry(Window,width=15,font=("Roboto",10))
UsernameEntry.place(anchor="center",rely=0.37,relx=.5)
PathEntry.place(anchor="center",rely=0.75,relx=.654)
WidthEntry.place(anchor="center",rely=0.90,relx=.3)
HeightEntry.place(anchor="center",rely=0.90,relx=.46)
RamComboBox = ttk.Combobox(Window,width=15,state="readonly")
RamComboBox.place(relx=.3,rely=0.75,anchor="center")
VersionComboBox = ttk.Combobox(Window,width=15,state="readonly")
VersionComboBox.place(relx=.458,rely=0.75,anchor="center")
RamComboBox['values'] = ("1024","2048","4096","8192","12288")
VersionComboBox['values'] = open("VersionList.txt","r").read()

#Launch Condition Checker\Generator
if os.path.exists("LauncherInformation.json"):
    file = open("LauncherInformation.json","r")
    readedtext = json.loads(file.read())
    data = []
    for item in readedtext:
        data.append(readedtext[item])
    file.close()
    RamComboBox.set(data[5])
    VersionComboBox.set(data[1])
    PathEntry.insert(0,data[2])
    WidthEntry.insert(0,data[3])
    HeightEntry.insert(0,data[4])
    HideState = data[6]

else:
    PathEntry.insert(0,os.getenv("APPDATA"))
    RamComboBox.set("2048")
    VersionComboBox.set("1.18.2")
    WidthEntry.insert(0,"1600")
    HeightEntry.insert(0,"800")
    HideState = False
if HideState == False:
    CheckBoxLabel.configure(fg="green")
else:
    CheckBoxLabel.configure(fg="red")
Window.resizable("False","False")
Window.mainloop()



















