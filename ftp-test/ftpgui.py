from tkinter import *
from tkinter import messagebox
from ftplib import FTP, error_perm
import tkinter
import os, shutil
root = tkinter.Tk()

FONT = "Arial Narrow"
BUTTONCOLOR = "black"
BGCOLOR = "black"
ACTIVEBG = "grey"

class BuildFtp():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('NCBI FTP GUI')
        self.parent.geometry("940x600")
        self.parent.configure(background=BUTTONCOLOR)
        self.parent.grid()
        self.parent.resizable(0,0)
        self.CreateFrames()
        self.AddButtons()
        self.AddLabel()
        self.AddEntrys()
        self.AddListbox()
        self.PopulateLocal()

    def CreateFrames(self):
        """Create The Frames"""
        self.EntryFrm = Frame(self.parent, bg = BUTTONCOLOR)
        self.EntryFrm.grid(row = 0, column = 0)
        self.LstFrm = Frame(self.parent, bg = BUTTONCOLOR)
        self.LstFrm.grid(row = 1, column = 0)
        self.BtnFrm = Frame(self.parent, bg = BUTTONCOLOR)
        self.BtnFrm.grid(row = 2, column = 0)

    def AddButtons(self):
        """Add Button"""
        self.LoginBtn = Button(self.EntryFrm, text = "Login", height = 2, width = 10, fg = "white", activebackground = ACTIVEBG, bg = BGCOLOR, command = self.Login)
        self.LocalUpLvl = Button(self.BtnFrm, text = "Up Level", fg = "white", activebackground = ACTIVEBG, bg = BGCOLOR, command = self.UpLocal)
        self.RemoteUpLvl = Button(self.BtnFrm, text = "Up Level", fg = "white", activebackground = ACTIVEBG, bg = BGCOLOR, command = self.UpRemote)
        self.RemoteNewF = Button(self.BtnFrm, text = "New Folder", fg = "white", activebackground = ACTIVEBG, bg = BGCOLOR, command = self.NewRemoteFolder)
        self.LocalNewF = Button(self.BtnFrm, text = "New Folder", fg = "white", activebackground = ACTIVEBG, bg = BGCOLOR, command = self.NewLocalFolder)
        self.RemoteDwn = Button(self.BtnFrm, text = "Download", fg = "white", activebackground = ACTIVEBG, bg = BGCOLOR, command = self.RemoteDwn)
        self.LocalDel = Button(self.BtnFrm, text = "Delete", fg = "white", activebackground = ACTIVEBG, bg = BGCOLOR, command = self.LocalDel)
        self.LoginBtn.grid(row = 0, column = 8, padx = 1, pady = 10)
        self.LocalUpLvl.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.LocalNewF.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.LocalDel.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.RemoteUpLvl.grid(row = 1, column = 3, padx = 10, pady = 10)
        self.RemoteNewF.grid(row = 1, column = 4, padx = 10, pady = 10)
        self.RemoteDwn.grid(row = 1, column = 5, padx = 10, pady = 10)

    def LocalDel(self):
        self.Selection3 = self.LocalLst.curselection()
        self.Value3 = self.LocalLst.get(self.Selection3[0])
        self.Cdir3 = os.getcwd()
        self.NewDir3 = self.Cdir3 + chr(92) + self.Value3
        self.Question = messagebox.askyesno("Delete Query", "Are you sure?")
        if self.Question:
            if '.' not in self.NewDir3:
                shutil.rmtree(self.NewDir3)
            else:
                os.remove(self.NewDir3)
            self.PopulateLocal()


    def RemoteDwn(self):
        self.Selection4 = self.RemoteLst.curselection()
        self.Value4 = self.RemoteLst.get(self.Selection4[0])
        self.Question2 = messagebox.askyesno("Download File", "Are you sure?")
        if self.Question2:
            if '.' in self.Value4:
                with open(self.Value4, 'wb') as local_file:
                    self.SERVER.retrbinary('RETR %s' % self.Value4, local_file.write)
            else:
                self.SERVER.rmd(self.Value4)
            self.PopulateLocal()

    def AddListbox(self):
        self.LocalLst = Listbox(self.LstFrm, bd = 1, height = 20, width = 40, font = (FONT, 12), selectbackground = 'red', selectmode = EXTENDED)
        self.RemoteLst = Listbox(self.LstFrm, bd = 1, height = 20, width = 40, font = (FONT, 12), selectbackground = 'red', selectmode = EXTENDED)
        self.LocalLst.bind('<Double-Button-1>', self.Forwarddir)
        self.RemoteLst.bind('<Double-Button-1>', self.RemoteForwarddir)
        self.LocalLst.grid(row = 0, column = 0, padx = 30, pady = 10)
        self.RemoteLst.grid(row = 0, column = 1, padx = 30, pady = 10)

    def AddLabel(self):
        """Add Label"""
        self.HostLbl = Label(self.EntryFrm, text = "Hostname: ", bg = BUTTONCOLOR, fg = "white", font = (FONT, 12))
        self.UserLbl = Label(self.EntryFrm, text = "Username: ", bg = BUTTONCOLOR, fg = "white", font = (FONT, 12))
        self.PwdLbl = Label(self.EntryFrm, text = "Password: ", bg = BUTTONCOLOR, fg = "white", font = (FONT, 12))
        self.PortLbl = Label(self.EntryFrm, text = "Port: ", bg = BUTTONCOLOR, fg = "white", font = (FONT, 12))
        self.HostLbl.grid(column = 0, row = 0, padx = 10, pady = 10)
        self.UserLbl.grid(column = 2, row = 0, padx = 10, pady = 10)
        self.PwdLbl.grid(column = 4, row = 0, padx = 10, pady = 10)
        self.PortLbl.grid(column = 6, row = 0, padx = 10, pady = 10)

    def AddEntrys(self):
        """Add Entrys"""
        self.HostEnt = Entry(self.EntryFrm, bd = 1, width = 17, font = (FONT, 10))
        self.UserEnt = Entry(self.EntryFrm, bd = 1, width = 17, font = (FONT, 10))
        self.PwdEnt = Entry(self.EntryFrm, bd = 1, width = 17, font = (FONT, 10), show = '*')
        self.PortEnt = Entry(self.EntryFrm, bd = 1, width = 17, font = (FONT, 10))
        self.HostEnt.insert(END, "ftp.ncbi.nlm.nih.gov")
        self.UserEnt.insert(END, "anonymous")
        self.PortEnt.insert(END, "21")
        self.HostEnt.grid(column = 1, row = 0, padx = 5, pady = 10)
        self.UserEnt.grid(column = 3, row = 0, padx = 5, pady = 10)
        self.PwdEnt.grid(column = 5, row = 0, padx = 5, pady = 10)
        self.PortEnt.grid(column = 7, row = 0, padx = 5, pady = 10)

    def UpLocal(self):
        os.chdir("..")
        self.PopulateLocal()

    def UpRemote(self):
        self.SERVER.cwd("..")
        self.PopulateRemote()

    def NewLocalFolder(self):
        x = True
        NewFolder(x)

    def NewRemoteFolder(self):
        x = False
        NewFolder(x)

    def Forwarddir(self, event):
        self.Widget = event.widget
        self.Selection = self.Widget.curselection()
        self.Value = self.Widget.get(self.Selection[0])
        self.Cdir = os.getcwd()
        self.NewDir = self.Cdir + chr(92) + self.Value
        try:
            os.chdir(self.NewDir)
            self.PopulateLocal()
        except:pass

    def PopulateLocal(self):
        self.LocalLst.delete(0, END)
        self.LocalDirLst = os.listdir()
        for i in range(len(self.LocalDirLst)):
            self.LocalLst.insert(i, self.LocalDirLst[i - 1])

    def PopulateRemote(self):
        self.RemoteLst.delete(0, END)
        self.DirLst = self.SERVER.nlst()
        for i in range(len(self.DirLst)):
            self.RemoteLst.insert(i, (self.DirLst[i - 1]))

    def RemoteForwarddir(self, event):
        self.Widget2 = event.widget
        self.Selection2 = self.Widget2.curselection()
        self.Value2 = self.Widget2.get(self.Selection2[0])
        if '.' not in self.Value2:
            try:
                self.SERVER.cwd(self.Value2)
                self.PopulateRemote()
            except:pass
        else:pass

    def Login(self):
        self.HostHold = self.HostEnt.get()
        self.UserHold = self.UserEnt.get()
        self.PwdHold = self.PwdEnt.get()
        self.PortHold = self.PortEnt.get()
        try:
            self.SERVER = FTP(self.HostHold, timeout=None)
        except:
            messagebox.showerror("Server Connection", "Cannot Connect to server")
        try:
            self.SERVER.login(user=self.UserHold, passwd=self.PwdHold)
            messagebox.showinfo("Server Connection", "Succesfully logged in! Welcome " + self.UserHold + ".")
            self.PopulateRemote()
        except:
            messagebox.showerror("Server Login", "User Login details incorrect")

    def NewRm(self, new):
        try:
            self.SERVER.mkd(new)
        except:
            messagebox.showerror("Folder Creation", "Folder Creation Failed - Permission denied")


class NewFolder():
    def __init__(self, x):
        self.x = x
        self.parent = Tk()
        self.parent.title('Folder Name')
        self.parent.geometry("250x250")
        self.parent.configure(background=BUTTONCOLOR)
        self.parent.grid()
        self.parent.resizable(0,0)
        self.AddStuff()

    def AddStuff(self):
        self.Lbl = Label(self.parent, text = "Enter Folder Name", bg = BUTTONCOLOR, font = (FONT, 12))
        self.Ent = Entry(self.parent, bd = 1, width = 25, font = (FONT, 10))
        self.Btn = Button(self.parent, text = "Create", height = 2, width = 10, fg = "white", activebackground = ACTIVEBG, bg = BGCOLOR, command = self.Create)
        self.Lbl.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.Ent.grid(row = 1, column = 0, padx = 20, pady = 20)
        self.Btn.grid(row = 2, column = 0, padx = 20, pady = 20)

    def Create(self):
        self.Breaker = True
        for x in self.Ent.get():
            if x in[' /', '?', '<', '>', ':,', '*', '|'] or x == chr(92):
                messagebox.showerror("User Error", "Folder name cannot contain  / ? < > \ : * |")
                self.Breaker = False
                break

        if len(self.Ent.get()) < 1: ####validation needed, e.g. ;' cannot be used as file names
            messagebox.showerror("User Error", "Folders need names!!")

        elif self.Breaker:
            if self.x:
                os.makedirs(self.Ent.get())
                buildftp.PopulateLocal()
            else:
                z = self.Ent.get()
                buildftp.NewRm(z)
                buildftp.PopulateRemote()
            self.parent.destroy()


buildftp = BuildFtp(root)
root.mainloop()