from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webgendrill
from webgendrill import *
import webbrowser
import webtextDB
from webtextDB import *

class WebGen:

    def __init__(self, master): 
        master.title('Web Text Generator')
        
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Enter Text Here:').pack()
        self.text_enter = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))
        self.text_enter.pack(pady = 5)

        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).pack()
        ttk.Button(self.frame_content, text = 'View Website', command = self.viewSite).pack(pady = 20)
        
        self.list1 = Listbox(master, width = 75, height = 200)
        self.list1.pack(pady = 20)
        self.loadListbox()

        #scroll = Scrollbar(self.list1, orient=VERTICAL)
        #select = Listbox(self.list1, yscrollcommand=scroll.set, height=200)
        #scroll.config (command = select.yview)
        #scroll.pack(side=RIGHT, fill=Y)
        #select.pack(side=LEFT, fill=BOTH, expand=1)
        
        ttk.Button(self.frame_content, text = 'Insert Text', command = self.loadEntry).pack(pady = 20)

    def submit(self):
        bodyText = self.text_enter.get(1.0, 'end')
        webgendrill.write(bodyText)
        webtextDB.dataEntry(bodyText)
        print ('Text: {}'.format(bodyText))
        self.clear()
        messagebox.showinfo(title = "Web Text Generator", message = "Text Submitted!")
        self.loadListbox()

    def clear(self):
        self.text_enter.delete(1.0, 'end')
    
    def viewSite(self):
        webbrowser.open_new_tab('summersale.html')

    
        
    def loadListbox(self):
        list_load = webtextDB.fetchRecord()
        for item in list_load:
            self.list1.insert(END, item)
            print (item)
    

    def whichSelected(self):
        entry = self.list1.get(self.list1.curselection())
        return entry[1]
        

    def loadEntry(self):
        list_load = self.whichSelected()
        self.text_enter.insert(END, list_load)

        



def main ():
    root = Tk()
    webgen = WebGen(root)
    root.geometry('800x700')
    root.mainloop()

if __name__=="__main__": main()