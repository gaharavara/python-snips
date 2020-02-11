from tkinter import Tk, Label, Button, Entry, Text

class todo:
    def __init__(self):
        self.newTab = Tk()
        entryTxt = Entry(self.newTab)
        entryTxt.grid(row=0, column=0)
        Button(self.newTab, text="Save", command=lambda: self.saveItem(entryTxt.get())).grid(row=0, column=1)
        Button(self.newTab, text="Cancel", command=self.newTab.quit).grid(row=1, column=0)
        self.newTab.mainloop()

    def saveItem(self, task):
        file = open('myTodo.txt', 'a')
        file.write(task+"#*\n\n")
        file.close()

class main:
    def __init__(self):
        self.mainWindow = Tk()
        self.items = []
        Button(self.mainWindow, text="+", command=self.addItem).grid(row=0,column=0)
        self.readItems()
        self.mainWindow.mainloop()

    def deleteItem(self, n):
        print("n",n)
        del self.items[n]
        del self.fileItems[n]
        print("after deletion", self.items)
        for i in self.fileItems:
            text = i+"#*\n\n"
        file = open('myTodo.txt', 'w')
        file.write(text)
        file.close()
        self.readItems()    
    
    def refreshItems(self):
        print("refreshit")

    def readItems(self):
        file = open('myTodo.txt', 'r')
        self.fileItems = file.read()
        file.close()
        self.fileItems = self.fileItems.split("#*\n\n")
        print("after split",self.fileItems)
        p=0
        for i in self.fileItems:
            self.items.append([Label(self.mainWindow, text=i).grid(row=p+1, column=0), Button(self.mainWindow, text="X", command=lambda p=p: self.deleteItem(p))])
            self.items[p][1].grid(row=p+1, column=1)
            p+=1

    def addItem(self):
        test = todo()
        self.readItems()

    
m1 = main()