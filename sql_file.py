from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import Voice_Assistant as voice_assistant
import time
import json
import mysql.connector as connection



data  = {}  
conn=connection.connect(user="root", password="yashwant@123", database="chatbot_db")
print(conn.is_connected())
query = "select * from chatbotquestionanswers;"
cursor=conn.cursor()
cursor.execute(query)
for row in cursor.fetchall():
        data[row[0]]=row[1]


print(len(data))
class ChatBot:

    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620")
        self.root.resizable(0,0)
        
        self.root.bind('<Return>',self.enter_func)

        main_frame = Frame(self.root, bd=4, bg="powder blue", width = 610)
        main_frame.pack()

        img_chat = Image.open("pic.png")
        img_chat = img_chat.resize((200, 70))
        self.photoImg = ImageTk.PhotoImage(img_chat)

        img  = PhotoImage(file="pic.png")
        self.root.iconphoto(True, img)

        Title_label = Label(main_frame, bd =3, relief=RAISED, anchor='nw', width=730,compound=LEFT, image = self.photoImg, text='Chat Me', font=('arial',30, 'bold'), fg='green', bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text=Text(main_frame, width=65, height= 20, bd=3, relief=RAISED, font=("arial", 14), yscrollcommand=self.scroll_y.set, wrap='word')
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root, bd=4, relief=RAISED,bg='white', width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame, text='Type Something', font=('arial', 16, 'bold'), fg='Green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry= StringVar()
        self.entry1= ttk.Entry(btn_frame, textvariable=self.entry, width=30, font=('arial', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send=Button(btn_frame, text='Send>>', command=self.send,font=('arial', 16, 'bold'), width= 8, bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear=Button(btn_frame, text='Clear Data', command= self.clear_func, font=('arial', 16, 'bold'), width= 8, bg='Red', fg='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg=''
        self.label_l1 = Label(btn_frame, text=self.msg, font=('arial', 16, 'bold'), fg='Red', bg='white')
        self.label_l1.grid(row=1, column=1, padx=5, sticky=W)


    # ================================= Function Declaration =================================
        
    def send(self):
        send = "\t\t\t"+'You: '+self.entry.get()
        # self.text.insert(END, '\n'+send)
        # self.text.yview(END)
        

        if(self.entry.get() == ""):
            self.msg = "Please enter some input"
            self.label_l1.config(text=self.msg, fg='red')
            #voice_assistant.speechtx(self.msg)
        else:
            self.msg = ""
            self.label_l1.config(text=self.msg)
            self.text.insert(END, '\n'+send)
            self.text.yview(END)

            msg = data.get(self.entry.get().lower(), "Sorry I didn't get you") #for dict


            #msg = data_in_file.get(self.entry.get().lower(), "Sorry I didn't get you") # for json
            self.text.insert(END, '\n\n'+"Bot: "+msg)
            voice_assistant.speechtx(msg)



    # ============================== Enter Function =============================
    
    def enter_func(self, event):
        self.send.invoke()
        self.entry.set('')
        

    # ============================== Clear Function =============================
    
    def clear_func(self):
        self.text.delete("1.0", END)
        self.entry.set("")

    

if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()