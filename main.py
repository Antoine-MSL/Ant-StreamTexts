import tkinter as tk
import glob
import os

root = tk.Tk()

root.resizable(False, False)
# 52

canvasheight = 50
os.chdir(r'texts')
textFiles = glob.glob('*.txt')
for i in range(len(textFiles)):
    if (i % 2) == 0:
        canvasheight = canvasheight
    else:
        canvasheight += 51

root.title("StreamTexts")

canvas1 = tk.Canvas(root, width=280, height=canvasheight)
canvas1.pack()
canvas1.config(background="#262626")

buttonList = []

i = 0

width1 = 70
width2 = 210

height1 = 20
height2 = 40

for elements in textFiles:
    file = open('%s' % (elements))
    content = file.read()
    if (i % 2) == 0:
        label1 = tk.Label(root, text=elements.split('.')[0])
        label1.configure(background="#272727", foreground="white")
        canvas1.create_window(width1, height1, window=label1)
        entry1 = tk.Entry(root)
        entry1.insert(0, content)
        buttonList.append(entry1)
        canvas1.create_window(width1, height2, window=entry1)
    elif (i % 2) != 0:
        label2 = tk.Label(root, text=elements.split('.')[0])
        label2.configure(background="#272727", foreground="white")
        canvas1.create_window(width2, height1, window=label2)
        entry2 = tk.Entry(root)
        entry2.insert(0, content)
        buttonList.append(entry2)
        canvas1.create_window(width2, height2, window=entry2)
        height1 += 50
        height2 += 50
    file.close()
    i += 1

def confirm():
    contentList = []
    for i in range(len(buttonList)):
        contentList.append(buttonList[i].get())
    i = 0
    for elements in textFiles:
        file = open('%s' % (elements), 'w')
        file.write(contentList[i])
        file.close()
        i += 1


button1 = tk.Button(text='Save Data', command=confirm)
canvas1.create_window(width2+30, height2-10, window=button1)

root.mainloop()
# this is the part where I mine crypto on your computer