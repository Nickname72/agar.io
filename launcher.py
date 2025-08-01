from customtkinter import *

class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()
        self.name = None
        self.host = None
        self.port = None

        self.title("Agario LAuncher")
        self.geometry('400x300')

        CTkLable(self, text="Connect to server", font=('Comic Sance MS',20,'bold')).pack(pady=15,padx=20,anchor='w')



        self.name_entry = CTkEntry(self,placeholder_text='Enter your name:', placeholder_text_color='Gray',
                                   height = 50)
        self.name_entry.pack(padx=20, anchor = 'w', fill = 'x')


        self.host_entry = CTkEntry(self,placeholder_text='Enter :', placeholder_text_color='Gray',
                                   height = 50)
        self.host_entry.pack(padx=20, anchor = 'w', fill = 'x')


        self.port_entry = CTkEntry(self,placeholder_text='Enter port:', placeholder_text_color='Gray',
                                   height = 50)
        self.port_entry.pack(padx=20, anchor = 'w', fill = 'x')

        CTkButton(self,text = 'Join', command = self.open_game, height = 50).pack(pady=15,padx=20,fill='x')

    def open_game():
        self.name = self.name_entry.get()
        self.host = self.host_entry.get()
        self.port = int(self.port_entry.get())
        self.destroy(

            
        )
        
















































