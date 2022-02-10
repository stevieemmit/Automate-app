import tkinter as tk
from tkinter import filedialog,Text
import os
 
root = tk.Tk()
apps = []

if os.path.isfile('save.text'):
    with open ('save.text', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps= [x for x in tempApps if x.strip()]
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables","*.exe"),("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps :
        label= tk.Label(frame,text=app, bg="grey")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=600, width=750 , bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openfile= tk.Button(root, text="Open File", padx=10,pady=5, fg="grey", bg="#263D42", command= addApp )
openfile.pack()

runApps= tk.Button(root, text="Run Apps", padx=10,
 pady=10, fg="grey", bg="#263D42", command= runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()

with open('save.text', 'w') as f:
    for app in apps:
        f.write(app +',')