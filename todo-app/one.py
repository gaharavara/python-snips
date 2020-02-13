from tkinter import Tk, Label, Button, Entry, Text

# Location of file to store the todo item list.
FILE_PATH = 'myTodoList.txt'

class todo:
    def __init__(self):
        self.newTab = Tk()
        entryTxt = Entry(self.newTab)
        entryTxt.grid(row=0, column=0)
        Button(self.newTab, text="Save", command=lambda: self.saveItem(entryTxt.get())).grid(row=0, column=1)
        Button(self.newTab, text="Cancel", command=self.newTab.quit).grid(row=1, column=0)
        self.newTab.mainloop()

    def saveItem(self, task):
        file = open(FILE_PATH, 'a')
        file.write(task+"#*#")
        file.close()
        self.newTab.destroy()

class main:
    def __init__(self):
        self.mainWindow = Tk()
        self.items = []
        Button(self.mainWindow, text="+", command=self.addItem).grid(row=0,column=0)
        
        file = open(FILE_PATH, 'a')
        file.close()

        self.readItems()
        self.mainWindow.mainloop()

    def deleteItem(self, n):
        print("n",n)
        self.items[n][0].grid_forget()
        self.items[n][1].grid_forget()
        self.items[n] = []
        del self.fileItems[n]
        print("after deletion", self.items)
        for i in self.fileItems:
            text = i+"#*#"
        file = open(FILE_PATH, 'w')
        file.write(text)
        file.close()
        self.readItems()    
    
    def readItems(self):
        file = open(FILE_PATH, 'r')
        self.fileItems = file.read()
        file.close()
        print(self.fileItems)
        self.fileItems = self.fileItems.split("#*#")
        print("after split",self.fileItems)
        p=0
        for i in self.fileItems:
            if i != '':
                self.items.append([Label(self.mainWindow, text=i), Button(self.mainWindow, text="X", command=lambda p=p: self.deleteItem(p))])
                self.items[p][0].grid(row=p+1, column=0)
                self.items[p][1].grid(row=p+1, column=1)
                p+=1

    def addItem(self):
        newItem = todo()
        print("destroy")
        newItem.newTab.destroy()
        print("destroyed newTab")
        self.readItems()

    
m1 = main()