﻿from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Registration:

    def __init__(self, master):

        master.title('Oregon Wine Experience Sponsor Registration')
        master.resizable(False, False)
        

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#FFFFFF')
        self.style.configure('TLabel', background = '#FFFFFF')
        self.style.configure("Header.TLabel", font = ("Arial", 18, "bold",))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        self.frame_header.configure(height = 200, width = 1000)

        self.logo=PhotoImage(file = 'OWELogo2016.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, padx = 23, sticky = 'nw')
        ttk.Label(self.frame_header, text = "Sponsor Registration", style = "Header.TLabel").grid(row=0, column=1, padx = 23)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        self.frame_content.configure(height = 500, width = 1000)

        ttk.Label(self.frame_content, text = 'Sponsor Company Name:').grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w')
        ttk.Label(self.frame_content, text = 'Select # of Tickets:').grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'w')
        ttk.Label(self.frame_content, text = 'Select Event:').grid(row = 0, column = 2, padx = 10, pady = 10, sticky = 'w')
        ttk.Label(self.frame_content, text = 'Attendee First & Last Name:').grid(row = 3, column = 0, padx = 10, pady = 5, sticky = 'w')
        ttk.Label(self.frame_content, text = 'E-mail Address:').grid(row = 3, column = 1, padx = 10, pady = 5, sticky = 'w')
        ttk.Label(self.frame_content, text = 'Mobile Number:').grid(row = 3, column = 2, padx = 10, pady = 5, sticky = 'w')

        self.entry_coname = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_tickets = ttk.Combobox(self.frame_content, width = 10, font = ('Arial', 10))
        self.entry_tickets['values'] = ('0', '2', '4', '8', '10')
        self.entry_tickets.bind('<<ComboboxSelected>>', self.entry)
  
    
        self.entry_event = ttk.Combobox(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_event['values'] = ('Barrel Auction','Medal Celebration','Salmon Bake', 'Vintner Dinner', 'Grand Tasting')
     
        self.tb_matrix = []
        self.entry_attendee1 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email1 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile1 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee1, self.entry_email1, self.entry_mobile1])
        self.entry_attendee2 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email2 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile2 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee2, self.entry_email2, self.entry_mobile2])
        self.entry_attendee3 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email3 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile3 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee3, self.entry_email3, self.entry_mobile3])
        self.entry_attendee4 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email4 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile4 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee4, self.entry_email4, self.entry_mobile4])
        self.entry_attendee5 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email5 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile5 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee5, self.entry_email5, self.entry_mobile5])
        self.entry_attendee6 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email6 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile6 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee6, self.entry_email6, self.entry_mobile6])
        self.entry_attendee7 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email7 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile7 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee7, self.entry_email7, self.entry_mobile7])
        self.entry_attendee8 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email8 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile8 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee8, self.entry_email8, self.entry_mobile8])
        self.entry_attendee9 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email9 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile9 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee9, self.entry_email9, self.entry_mobile9])
        self.entry_attendee10 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email10 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_mobile10 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.tb_matrix.append([self.entry_attendee10, self.entry_email10, self.entry_mobile10])
        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 14, column = 1, pady = 10, sticky = 's')
        self.disable()

        self.entry_coname.grid(row = 1, column = 0, padx = 5)
        self.entry_tickets.grid(row = 1, column = 1, padx = 5)
        self.entry_event.grid(row = 1, column = 2, padx = 5)
        for i, tb_list in enumerate(self.tb_matrix):
            for j, tb in enumerate(tb_list):
                tb.grid(row=4+i, column = j, padx = 5, pady = 5)
                
        '''
        self.entry_attendee1.grid(row = 4, column = 0, padx = 5)
        self.entry_email1.grid(row = 4, column = 1, padx = 5)
        self.entry_mobile1.grid(row = 4, column = 2, padx = 5)
        self.entry_attendee2.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.entry_email2.grid(row = 5, column = 1, padx = 5, pady = 5)
        self.entry_mobile2.grid(row = 5, column = 2, padx = 5, pady = 5)
        self.entry_attendee3.grid(row = 6, column = 0, padx = 5, pady = 5)
        self.entry_email3.grid(row = 6, column = 1, padx = 5, pady = 5)
        self.entry_mobile3.grid(row = 6, column = 2, padx = 5, pady = 5)
        self.entry_attendee4.grid(row = 7, column = 0, padx = 5, pady = 5)
        self.entry_email4.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.entry_mobile4.grid(row = 7, column = 2, padx = 5, pady = 5)
        self.entry_attendee5.grid(row = 8, column = 0, padx = 5, pady = 5)
        self.entry_email5.grid(row = 8, column = 1, padx = 5, pady = 5)
        self.entry_mobile5.grid(row = 8, column = 2, padx = 5, pady = 5)
        self.entry_attendee6.grid(row = 9, column = 0, padx = 5, pady = 5)
        self.entry_email6.grid(row = 9, column = 1, padx = 5, pady = 5)
        self.entry_mobile6.grid(row = 9, column = 2, padx = 5, pady = 5)
        self.entry_attendee7.grid(row = 10, column = 0, padx = 5, pady = 5)
        self.entry_email7.grid(row = 10, column = 1, padx = 5, pady = 5)
        self.entry_mobile7.grid(row = 10, column = 2, padx = 5, pady = 5)
        self.entry_attendee8.grid(row = 11, column = 0, padx = 5, pady = 5)
        self.entry_email8.grid(row = 11, column = 1, padx = 5, pady = 5)
        self.entry_mobile8.grid(row = 11, column = 2, padx = 5, pady = 5)
        self.entry_attendee9.grid(row = 12, column = 0, padx = 5, pady = 5)
        self.entry_email9.grid(row = 12, column = 1, padx = 5, pady = 5)
        self.entry_mobile9.grid(row = 12, column = 2, padx = 5, pady = 5)
        self.entry_attendee10.grid(row = 13, column = 0, padx = 5, pady = 5)
        self.entry_email10.grid(row = 13, column = 1, padx = 5, pady = 5)
        self.entry_mobile10.grid(row = 13, column = 2, padx = 5, pady = 5)
        '''

    def disable(self):
        for tb_list in self.tb_matrix:
            for tb in tb_list:
                tb.configure(state='disabled')
        '''
        self.entry_attendee1.configure(state='disabled')
        self.entry_email1.configure(state='disabled')
        self.entry_mobile1.configure(state='disabled')
        self.entry_attendee2.configure(state='disabled')
        self.entry_email2.configure(state='disabled')
        self.entry_mobile2.configure(state='disabled')
        self.entry_attendee3.configure(state='disabled')
        self.entry_email3.configure(state='disabled')
        self.entry_mobile3.configure(state='disabled')
        self.entry_attendee4.configure(state='disabled')
        self.entry_email4.configure(state='disabled')
        self.entry_mobile4.configure(state='disabled')
        self.entry_attendee5.configure(state='disabled')
        self.entry_email5.configure(state='disabled')
        self.entry_mobile5.configure(state='disabled')
        self.entry_attendee6.configure(state='disabled')
        self.entry_email6.configure(state='disabled')
        self.entry_mobile6.configure(state='disabled')
        self.entry_attendee7.configure(state='disabled')
        self.entry_email7.configure(state='disabled')
        self.entry_mobile7.configure(state='disabled')
        self.entry_attendee8.configure(state='disabled')
        self.entry_email8.configure(state='disabled')
        self.entry_mobile8.configure(state='disabled')
        self.entry_attendee9.configure(state='disabled')
        self.entry_email9.configure(state='disabled')
        self.entry_mobile9.configure(state='disabled')
        self.entry_attendee10.configure(state='disabled')
        self.entry_email10.configure(state='disabled')
        self.entry_mobile10.configure(state='disabled')
        '''
    
    def entry(self, event):
        print('Tickets: {}'.format(self.entry_tickets.get()))
        for i in range(int(self.entry_tickets.get())):
            for tb in self.tb_matrix[i]:
                tb.configure(state='normal')
        if int(self.entry_tickets.get()) == 0 : self.disable()
        '''
        if self.entry_tickets.get() == '2':
            self.entry_attendee1.configure(state='normal')
            self.entry_email1.configure(state='normal')
            self.entry_mobile1.configure(state='normal')
            self.entry_attendee2.configure(state='normal')
            self.entry_email2.configure(state='normal')
            self.entry_mobile2.configure(state='normal')
        elif self.entry_tickets.get() == '4':
            self.entry_attendee1.configure(state='normal')
            self.entry_email1.configure(state='normal')
            self.entry_mobile1.configure(state='normal')
            self.entry_attendee2.configure(state='normal')
            self.entry_email2.configure(state='normal')
            self.entry_mobile2.configure(state='normal')
            self.entry_attendee3.configure(state='normal')
            self.entry_email3.configure(state='normal')
            self.entry_mobile3.configure(state='normal')
            self.entry_attendee4.configure(state='normal')
            self.entry_email4.configure(state='normal')
            self.entry_mobile4.configure(state='normal')
        elif self.entry_tickets.get() == '8':
            self.entry_attendee1.configure(state='normal')
            self.entry_email1.configure(state='normal')
            self.entry_mobile1.configure(state='normal')
            self.entry_attendee2.configure(state='normal')
            self.entry_email2.configure(state='normal')
            self.entry_mobile2.configure(state='normal')
            self.entry_attendee3.configure(state='normal')
            self.entry_email3.configure(state='normal')
            self.entry_mobile3.configure(state='normal')
            self.entry_attendee4.configure(state='normal')
            self.entry_email4.configure(state='normal')
            self.entry_mobile4.configure(state='normal')
            self.entry_attendee5.configure(state='normal')
            self.entry_email5.configure(state='normal')
            self.entry_mobile5.configure(state='normal')
            self.entry_attendee6.configure(state='normal')
            self.entry_email6.configure(state='normal')
            self.entry_mobile6.configure(state='normal')
            self.entry_attendee7.configure(state='normal')
            self.entry_email7.configure(state='normal')
            self.entry_mobile7.configure(state='normal')
            self.entry_attendee8.configure(state='normal')
            self.entry_email8.configure(state='normal')
            self.entry_mobile8.configure(state='normal')
        elif self.entry_tickets.get() == '10':
            self.entry_attendee1.configure(state='normal')
            self.entry_email1.configure(state='normal')
            self.entry_mobile1.configure(state='normal')
            self.entry_attendee2.configure(state='normal')
            self.entry_email2.configure(state='normal')
            self.entry_mobile2.configure(state='normal')
            self.entry_attendee3.configure(state='normal')
            self.entry_email3.configure(state='normal')
            self.entry_mobile3.configure(state='normal')
            self.entry_attendee4.configure(state='normal')
            self.entry_email4.configure(state='normal')
            self.entry_mobile4.configure(state='normal')
            self.entry_attendee5.configure(state='normal')
            self.entry_email5.configure(state='normal')
            self.entry_mobile5.configure(state='normal')
            self.entry_attendee6.configure(state='normal')
            self.entry_email6.configure(state='normal')
            self.entry_mobile6.configure(state='normal')
            self.entry_attendee7.configure(state='normal')
            self.entry_email7.configure(state='normal')
            self.entry_mobile7.configure(state='normal')
            self.entry_attendee8.configure(state='normal')
            self.entry_email8.configure(state='normal')
            self.entry_mobile8.configure(state='normal')
            self.entry_attendee9.configure(state='normal')
            self.entry_email9.configure(state='normal')
            self.entry_mobile9.configure(state='normal')
            self.entry_attendee10.configure(state='normal')
            self.entry_email10.configure(state='normal')
            self.entry_mobile10.configure(state='normal')
        else:
            self.disable()
        '''

    def submit(self):
        print('CoName: {}'.format(self.entry_coname.get()))
        print('NumofTickets:{}'.format(self.entry_tickets.get()))
        print('Event:{}'.format(self.entry_event.get()))
        for i in range(int(self.entry_tickets.get())):
            print('Attendee{}:{}'.format(str(i+1),self.entry_attendee1.get()))
            print('Email{}:{}'.format(str(i+1),self.entry_email1.get()))
            print('Mobile{}:{}'.format(str(i+1),self.entry_mobile1.get()))
        '''    
        if self.entry_tickets.get() == '2':
            print('CoName: {}'.format(self.entry_coname.get()))
            print('NumofTickets:{}'.format(self.entry_tickets.get()))
            print('Event:{}'.format(self.entry_event.get()))
            print('Attendee1:{}'.format(self.entry_attendee1.get()))
            print('Email1:{}'.format(self.entry_email1.get()))
            print('Mobile1:{}'.format(self.entry_mobile1.get()))
            print('Attendee2:{}'.format(self.entry_attendee2.get()))
            print('Email2:{}'.format(self.entry_email2.get()))
            print('Mobile2:{}'.format(self.entry_mobile2.get()))
            messagebox.showinfo(title = "Registration Complete", message = "Thank you for Registering!")
        elif self.entry_tickets.get() == '4':
            print('CoName: {}'.format(self.entry_coname.get()))
            print('NumofTickets:{}'.format(self.entry_tickets.get()))
            print('Event:{}'.format(self.entry_event.get()))
            print('Attendee1:{}'.format(self.entry_attendee1.get()))
            print('Email1:{}'.format(self.entry_email1.get()))
            print('Mobile1:{}'.format(self.entry_mobile1.get()))
            print('Attendee2:{}'.format(self.entry_attendee2.get()))
            print('Email2:{}'.format(self.entry_email2.get()))
            print('Mobile2:{}'.format(self.entry_mobile2.get()))
            print('Attendee3:{}'.format(self.entry_attendee3.get()))
            print('Email3:{}'.format(self.entry_email3.get()))
            print('Mobile3:{}'.format(self.entry_mobile3.get()))
            print('Attendee4:{}'.format(self.entry_attendee4.get()))
            print('Email4:{}'.format(self.entry_email4.get()))
            print('Mobile4:{}'.format(self.entry_mobile4.get()))
            messagebox.showinfo(title = "Registration Complete", message = "Thank you for Registering!")
        elif self.entry_tickets.get() == '8':
            print('CoName: {}'.format(self.entry_coname.get()))
            print('NumofTickets:{}'.format(self.entry_tickets.get()))
            print('Event:{}'.format(self.entry_event.get()))
            print('Attendee1:{}'.format(self.entry_attendee1.get()))
            print('Email1:{}'.format(self.entry_email1.get()))
            print('Mobile1:{}'.format(self.entry_mobile1.get()))
            print('Attendee2:{}'.format(self.entry_attendee2.get()))
            print('Email2:{}'.format(self.entry_email2.get()))
            print('Mobile2:{}'.format(self.entry_mobile2.get()))
            print('Attendee3:{}'.format(self.entry_attendee3.get()))
            print('Email3:{}'.format(self.entry_email3.get()))
            print('Mobile3:{}'.format(self.entry_mobile3.get()))
            print('Attendee4:{}'.format(self.entry_attendee4.get()))
            print('Email4:{}'.format(self.entry_email4.get()))
            print('Mobile4:{}'.format(self.entry_mobile4.get()))
            print('Attendee5:{}'.format(self.entry_attendee5.get()))
            print('Email5:{}'.format(self.entry_email5.get()))
            print('Mobile5:{}'.format(self.entry_mobile5.get()))
            print('Attendee6:{}'.format(self.entry_attendee6.get()))
            print('Email6:{}'.format(self.entry_email6.get()))
            print('Mobile6:{}'.format(self.entry_mobile6.get()))
            print('Attendee7:{}'.format(self.entry_attendee7.get()))
            print('Email7:{}'.format(self.entry_email7.get()))
            print('Mobile7:{}'.format(self.entry_mobile7.get()))
            print('Attendee8:{}'.format(self.entry_attendee8.get()))
            print('Email8:{}'.format(self.entry_email8.get()))
            print('Mobile8:{}'.format(self.entry_mobile8.get()))
            messagebox.showinfo(title = "Registration Complete", message = "Thank you for Registering!")
        elif self.entry_tickets.get() == '10':
            print('CoName: {}'.format(self.entry_coname.get()))
            print('NumofTickets:{}'.format(self.entry_tickets.get()))
            print('Event:{}'.format(self.entry_event.get()))
            print('Attendee1:{}'.format(self.entry_attendee1.get()))
            print('Email1:{}'.format(self.entry_email1.get()))
            print('Mobile1:{}'.format(self.entry_mobile1.get()))
            print('Attendee2:{}'.format(self.entry_attendee2.get()))
            print('Email2:{}'.format(self.entry_email2.get()))
            print('Mobile2:{}'.format(self.entry_mobile2.get()))
            print('Attendee3:{}'.format(self.entry_attendee3.get()))
            print('Email3:{}'.format(self.entry_email3.get()))
            print('Mobile3:{}'.format(self.entry_mobile3.get()))
            print('Attendee4:{}'.format(self.entry_attendee4.get()))
            print('Email4:{}'.format(self.entry_email4.get()))
            print('Mobile4:{}'.format(self.entry_mobile4.get()))
            print('Attendee5:{}'.format(self.entry_attendee5.get()))
            print('Email5:{}'.format(self.entry_email5.get()))
            print('Mobile5:{}'.format(self.entry_mobile5.get()))
            print('Attendee6:{}'.format(self.entry_attendee6.get()))
            print('Email6:{}'.format(self.entry_email6.get()))
            print('Mobile6:{}'.format(self.entry_mobile6.get()))
            print('Attendee7:{}'.format(self.entry_attendee7.get()))
            print('Email7:{}'.format(self.entry_email7.get()))
            print('Mobile7:{}'.format(self.entry_mobile7.get()))
            print('Attendee8:{}'.format(self.entry_attendee8.get()))
            print('Email8:{}'.format(self.entry_email8.get()))
            print('Mobile8:{}'.format(self.entry_mobile8.get()))
            print('Attendee9:{}'.format(self.entry_attendee9.get()))
            print('Email9:{}'.format(self.entry_email9.get()))
            print('Mobile9:{}'.format(self.entry_mobile9.get()))
            print('Attendee10:{}'.format(self.entry_attendee10.get()))
            print('Email10:{}'.format(self.entry_email10.get()))
            print('Mobile10:{}'.format(self.entry_mobile10.get()))
            messagebox.showinfo(title = "Registration Complete", message = "Thank you for Registering!")
        else:
            pass'''
     


def main ():
    root = Tk()
    registration = Registration(root)
    root.geometry('735x750')
    root.mainloop()

if __name__=="__main__": main()

