from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from time import strftime
import time
import os
import sys

from xrays import XraysClass 
from dental import DentalClass
from implant import ImplantClass
from press import PressClass


# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
        
#     return os.path.join(base_path, relative_path)        


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
       
        return os.path.join(os.path.dirname(sys.executable), relative_path)
    else:
        return os.path.join(os.path.abspath("."), relative_path)


class clinic:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x650+50+20")
        self.root.resizable(False,False)
        self.root.title("Dental clinic")
        self.root.config(bg="white")


        #=======================label date=====================
        self.lbl_date = Label(self.root, text=' ادارة عيادة أسنان\t\t\t\t Date: DD-MM-YYYY\t\t\t\t Time: HH:MM:SS',font=('time new roman', 15, 'bold'), bg='#005c78', fg='white')
        self.lbl_date.place(x=0, y=0, width=1200, height=70)        
        self.timed()
        
        #====================fram buttons============
        btn_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white') 
        btn_frame.place(x=998, y=70, width=200, height=579) 
        
        #=======================image=======================
        self.menu_img = Image.open(resource_path("C:/Users/Ideapad 3/OneDrive/Desktop/CLINIC_APP/images/dash.jpeg"))
        self.menu_img =self.menu_img.resize((200,270))
        self.menu_img =ImageTk.PhotoImage(self.menu_img)
        
        lbl_img =Label(btn_frame, image=self.menu_img)
        lbl_img.pack(side=TOP, fill=X)
        
        #===================== label====================
        lbl_menu = Label(btn_frame, text="Menu", font=('times new roman', 20), bg='white', fg='#005c78',relief=RIDGE)
        lbl_menu.pack(fill=X)
        
        #================================ buttons========================
        btn1 = Button(btn_frame, text='الأشعة', font=('times new roman', 20), bg='#005c78', fg='white', bd=3, cursor='hand2', command=self.xrays)
        btn1.pack(side=TOP, fill=X)
        
        btn2 = Button(btn_frame, text='الحجوزات', font=('times new roman', 20), bg='#005c78', fg='white', bd=3, cursor='hand2', command=self.dental)
        btn2.pack(side=TOP, fill=X)
        
        btn3 = Button(btn_frame, text=' قسم الحشوات ', font=('times new roman', 20), bg='#005c78', fg='white', bd=3, cursor='hand2', command=self.press)
        btn3.pack(side=TOP, fill=X)
        
        btn4 = Button(btn_frame, text='قسم الزراعة', font=('times new roman', 20), bg='#005c78', fg='white', bd=3, cursor='hand2', command=self.implant)
        btn4.pack(side=TOP, fill=X)
        
        btn5 = Button(btn_frame, text='Exit', font=('times new roman', 20), bg='#005c78', fg='white', bd=3, cursor='hand2', command=root.quit)
        btn5.pack(side=TOP, fill=X)
        
        
        #=============================== frame image ==================================
        frame_img = Frame(self.root, bd=2, relief=RIDGE, bg='gray')
        frame_img.place(x=1, y=72, width=995, height=577)
        
        self.logo = Image.open(resource_path("C:/Users/Ideapad 3/OneDrive/Desktop/CLINIC_APP/images/board.jpg"))
        self.logo = self.logo.resize((995,577))
        self.logo = ImageTk.PhotoImage(self.logo)
        
        lbl_logo_img = Label(frame_img, image=self.logo)
        lbl_logo_img.place(x=0, y=0, width=995, height= 577)
        
        
        
        #============================= time =========================
    def timed(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%D:%M:%Y")
        self.lbl_date.config(text=f" إدارة عيادة أسنان \t\t\t\t Date: {str(date_)}\t\t\t\t Time: {str(time_)}")
        self.lbl_date.after(1000, self.timed)                     
        
    def xrays(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = XraysClass(self.new_win)
        
    def dental(self):
        self.new_win =  Toplevel(self.root)
        self.new_obj = DentalClass(self.new_win)   
            
        
        
    def implant(self):
        self.new_win =  Toplevel(self.root)
        self.new_obj = ImplantClass(self.new_win)   
        
        
        
        
        
    def press(self):
        self.new_win =  Toplevel(self.root)
        self.new_obj = PressClass(self.new_win)    
            
        
        
if __name__=="__main__":
    root=Tk()
    obj=clinic(root)
    root.mainloop()