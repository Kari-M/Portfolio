import wx
import shutil
import os
from time import time
import scripting_drill as sd
import file_trans_database as ftd
from datetime import datetime, time

app = wx.App()
source = 'C:\Users\Kari\Desktop\original_docs'
destination = 'C:\Users\Kari\Desktop\edited_docs'
files = os.listdir(source)
path = source + '\\'
time = datetime.now()



class file_trans (wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'File Transfer', size=(500, 400))
        panel=wx.Panel(self)
        button=wx.Button(panel, label="Browse Directory", pos=(150, 15), size=(175, 35))
        self.Bind(wx.EVT_BUTTON, self.searchDir, button)
        button=wx.Button(panel, label="Select Destination", pos=(150, 60), size=(175, 35))
        self.Bind(wx.EVT_BUTTON, self.searchDest, button)
        button=wx.Button(panel, label="Transfer Files", pos=(150, 100), size=(175, 35))
        self.Bind(wx.EVT_BUTTON, self.transferFiles, button)
        wx.StaticText(panel, wx.ID_ANY, label="Last File Transfer:", pos=(120, 200))
        self.lastTransTime = wx.StaticText(panel, wx.ID_ANY, label=str(ftd.readData()), pos=(240, 200))
 
    def searchDir(self,event):
        dialog = wx.DirDialog(None, 'Select a File:', style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON,)
        if dialog.ShowModal() == wx.ID_OK:
            source = dialog.GetPath()
            #print source
        dialog.Destroy()

    def searchDest(self,event):
        dialog = wx.DirDialog(None, 'Select the Destination:', style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON,)
        if dialog.ShowModal() == wx.ID_OK:
            destination = dialog.GetPath()
            #print destination
        dialog.Destroy()


    def transferFiles(self, event):
        files = os.listdir(source)
        #print files
        for f in files:
            path = source + '\\' + f
            if sd.mins_since_mod(path) < (24*60):
                shutil.move(path, destination)
                time = datetime.now()
        ftd.dataEntry()
        self.showDate()

    def showDate(self):
        mysql_data = ftd.readData()
        self.lastTransTime.SetLabel(mysql_data)
        print mysql_data
        

frame = file_trans(parent=None, id=-1)
frame.Show()                  
app.MainLoop()








