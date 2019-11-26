import tkinter as tk
from tkinter import filedialog,Text
import os

root = tk.Tk()
apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
        
    filename = filedialog.askopenfilename(initialdir="/",title="Select file name"
                                          ,filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg="gray")
        label.pack()
def runApp():
    for app in apps:
        os.startfile(app)
canvas = tk.Canvas(root,height=500,width=500,bg="#000")
canvas.pack()
frame = tk.Frame(root,bg="#fff")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
openFile = tk.Button(root,text="Open File", padx=10,pady=5,fg="white",bg="#000",command=addApp)
openFile.pack()
openApps = tk.Button(root,text="Run Apps", padx=10,pady=5,fg="white",bg="#000",command=runApp)
openApps.pack()

for app in apps:
    label = tk.Label(frame,text=app)
    label.pack()

root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')