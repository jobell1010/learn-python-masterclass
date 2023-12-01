import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('260x300+100+200')
mainWindow['padx'] = 10
mainWindow.minsize(240, 240)

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4)

cButton = tkinter.Button(mainWindow, text="C")
ceButton = tkinter.Button(mainWindow, text="CE")
cButton.grid(row=1, column=0, sticky='nsew')
ceButton.grid(row=1, column=1, sticky='nsew')

row1 = ['7', '8', '9', '+']
row2 = ['4', '5', '6', '-']
row3 = ['1', '2', '3', '*']
buttonNames = [row1, row2, row3]

for i, r in enumerate(buttonNames):
    for j, butt in enumerate(r):
        button = tkinter.Button(mainWindow, text=butt)
        button.grid(row=i+3, column=j, sticky='nsew')

zeroButton = tkinter.Button(mainWindow, text="0")
zeroButton.grid(row=6, column=0, sticky='nsew')
equalButton = tkinter.Button(mainWindow, text="=")
equalButton.grid(row=6, column=1, columnspan=2,sticky='nsew')
divideButton = tkinter.Button(mainWindow, text="/")
divideButton.grid(row=6, column=3, sticky='nsew')

mainWindow.mainloop()
