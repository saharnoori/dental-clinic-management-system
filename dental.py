from tkinter import *
from tkinter import ttk , messagebox
from PIL import Image , ImageTk
import sqlite3
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)   



class DentalClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("995x550+50+120")
        self.root.title("Dental Clinic")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        
        
        #============= varibles ====================
        self.var_search_comb = StringVar()
        self.var_search_en = StringVar()
        
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_age = StringVar()
        self.var_date = StringVar()
        self.var_state = StringVar()
        self.var_contact = StringVar()
        self.var_address = StringVar()
        
        #====================== search frame ===============
        search_frame = LabelFrame(self.root, text='بحث', font=('goudy old style',12,"bold" ),bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=370, y=20, width=600, height=70)
        
       #======================== combbox ====================
        cmb_search = ttk.Combobox(search_frame,textvariable=self.var_search_comb, values=("Select", "Name", "Contact","Gender","Age"), state='readonly', justify=CENTER, font=("tagwal",15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
         
        txt_search = Entry(search_frame,textvariable=self.var_search_en, font=("tajwal",15), bg='lightyellow',justify=CENTER).place(x=200,y=10,width=210)
        
        btn_search = Button(search_frame,command=self.search, text="بحث", font=("goudy old style", 15), bg="#005c78",fg='white',cursor='hand2').place(x=415,y=9,width=150,height=30) 
       
       #======================== label ======================
        title = Label(self.root, text="إدخال البيانات", font=('arial', 15),bg="#005c78", fg="white").place(x=340,y=100,width=645)  
        
        #====================== photo ======================
        self.logo = Image.open(resource_path("C:/Users/Ideapad 3/OneDrive/Desktop/CLINIC_APP/images/dental.jpg"))
        self.log = self.logo.resize((320,200))
        self.log = ImageTk.PhotoImage(self.log)
        
        lbl_image = Label(self.root, image=self.log)
        lbl_image.place(x=5,y=5,width=325,height=200)
        
        #===================== Label + Entrys ================
        lbl_name = Label(self.root, text="الأسم", font=("tajwal",15), bg='lightyellow').place(x=940,y=145)
        lbl_gender = Label(self.root, text="الجنس", font=("tajwal",15), bg='lightyellow').place(x=710,y=145)
        lbl_age = Label(self.root, text="العمر", font=("tajwal",15), bg='lightyellow').place(x=500,y=145)
        
        txt_name =Entry(self.root,textvariable=self.var_name, font=('tajwal',15), bg='lightyellow',justify=CENTER).place(x=780,y=150,width=150)
        
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender, value=("select","ذكر","أنثى"),state="readonly",justify=CENTER,font=("tajwal",15))
        cmb_gender.place(x=550,y=150,width=150)
        cmb_gender.current(0)
        
        txt_age =Entry(self.root,textvariable=self.var_age, font=('tajwal',15), bg='lightyellow',justify=CENTER).place(x=350,y=150,width=150)
        
        lbl_date = Label(self.root, text="التاريخ", font=("tajwal",15), bg='lightyellow').place(x=940,y=200)
        lbl_state = Label(self.root, text="الحالة", font=("tajwal",15), bg='lightyellow').place(x=710,y=200)
        lbl_contact = Label(self.root, text="الهاتف", font=("tajwal",15), bg='lightyellow').place(x=500,y=200)
        lbl_address = Label(self.root, text="العنوان", font=("tajwal",15), bg='lightyellow').place(x=940,y=250)
        
        txt_date =Entry(self.root,textvariable=self.var_date, font=('tajwal',15), bg='lightyellow',justify=CENTER).place(x=780,y=200,width=150)
        txt_state =Entry(self.root,textvariable=self.var_state, font=('tajwal',15), bg='lightyellow',justify=CENTER).place(x=550,y=200,width=150)
        txt_contact =Entry(self.root,textvariable=self.var_contact, font=('tajwal',15), bg='lightyellow',justify=CENTER).place(x=350,y=200,width=150)
        txt_address =Entry(self.root,textvariable=self.var_address, font=('tajwal',15), bg='lightyellow',justify=CENTER).place(x=780,y=250,width=150)
        
        #=============================== Buttons =========================
        btn_add = Button(self.root,command=self.add, text="إضافة",font=("tajwal",15),bg='#005c78', fg="white",cursor='hand2').place(x=175,y=215,width=155,height=28)
        btn_update = Button(self.root,command=self.update, text="تحديث",font=("tajwal",15),bg='#005c78', fg="white",cursor='hand2').place(x=5,y=215,width=155,height=28)
        btn_delete = Button(self.root,command=self.delete, text="حذف",font=("tajwal",15),bg='#005c78', fg="white",cursor='hand2').place(x=5,y=250,width=155,height=28)
        btn_clear = Button(self.root,command=self.clear, text="تفريغ",font=("tajwal",15),bg='#005c78', fg="white",cursor='hand2').place(x=175,y=250,width=155,height=28)
        
        #============================= tree view ==========================
        tree_frame = Frame(self.root, bd=3,relief=RIDGE)
        tree_frame.place(x=0,y=290,width=995,height=260)
        
        scrolly = Scrollbar(tree_frame, orient=VERTICAL)
        scrollx = Scrollbar(tree_frame, orient=HORIZONTAL)
        
        self.dental_table = ttk.Treeview(tree_frame,columns=("address","contact","state","date","age","gender","name","did"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.dental_table.xview)
        scrolly.config(command=self.dental_table.yview)
        
        self.dental_table.heading("address",text="العنوان")
        self.dental_table.heading("contact",text="هاتف")
        self.dental_table.heading("state",text="الحالة")
        self.dental_table.heading("date",text="التاريخ")
        self.dental_table.heading("age",text="العمر")
        self.dental_table.heading("gender",text="الجنس")
        self.dental_table.heading("name",text="الأسم")
        self.dental_table.heading("did",text="التسلسل")

        
        self.dental_table["show"]="headings"
        
        self.dental_table.column("did" ,width=40,anchor=NE)
        self.dental_table.column("name" ,width=100,anchor=NE)
        self.dental_table.column("gender" ,width=100,anchor=NE)
        self.dental_table.column("age" ,width=100,anchor=NE)
        self.dental_table.column("date" ,width=100,anchor=NE)
        self.dental_table.column("state" ,width=100,anchor=NE)
        self.dental_table.column("contact" ,width=100,anchor=NE)
        self.dental_table.column("address" ,width=100,anchor=NE)
        self.dental_table.pack(fill=BOTH,expand=1)
        self.dental_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
    def record_id(self):
        con = sqlite3.connect(resource_path('clinic.db'))
        cur = con.cursor()
        cur.execute("""
        WITH RECURSIVE cte As(
                     SELECT ROW_NUMBER() OVER (ORDER BY aid) As new_id, aid
                     FROM dental
                    ) 
        UPDATE dental
                    SET aid = (SELECT new_id FROM cte WHERE cte.aid = dental.aid)
        """ )
        con.commit()
            
        
    def add(self):
        con = sqlite3.connect(resource_path('clinic.db'))
        cur = con.cursor()
        if (self.var_address.get()=="" or self.var_contact.get()=="" or self.var_state.get()=="" or self.var_date.get()=="" or self.var_age.get()=="" or self.var_gender.get()=="select" or self.var_name.get()==""):
            messagebox.showerror("Error", "please enter all the data")
        else:
            cur.execute("Insert into dental(address,contact,state,date,age,gender,name) values(?,?,?,?,?,?,?)",(
                        self.var_address.get(),
                        self.var_contact.get(),
                        self.var_state.get(),
                        self.var_date.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_name.get(),
                      
                
            ))
            messagebox.showinfo("Success", "add Succcessfully")    
            con.commit()
            self.record_id()
            self.show()
            self.clear()
            
    def show(self):
        con = sqlite3.connect(resource_path('clinic.db'))
        cur = con.cursor()
        try:
            cur.execute("select * from dental ")
            rows = cur.fetchall()
            self.dental_table.delete(*self.dental_table.get_children()) 
            for row in rows:
                self.dental_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"error to :{str(ex)}")
            
    def clear(self):
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_age.set("")
        self.var_date.set("")
        self.var_state.set("")
        self.var_contact.set("")
        self.var_address.set("")
        self.var_id.set("")
        self.var_search_comb.set("Select")
        self.var_search_en.set("")
        
        self.show()
        
    def get_data(self,ev):
        f = self.dental_table.focus()
        contant =(self.dental_table.item(f))
        row = contant['values']
        
        self.var_address.set(row[0])
        self.var_contact.set(row[1])
        self.var_state.set(row[2])
        self.var_date.set(row[3])
        self.var_age.set(row[4])
        self.var_gender.set(row[5])
        self.var_name.set(row[6])
        self.var_id.set(row[7])    
                
    def update(self):
        con = sqlite3.connect(resource_path('clinic.db'))
        cur = con.cursor()
        cur.execute("""Update dental set address=?,contact=?,state=?,date=?,age=?,gender=?,name=? where aid=?""",(
                    
                    self.var_address.get(),
                    self.var_contact.get(),
                    self.var_state.get(),
                    self.var_date.get(),
                    self.var_age.get(),
                    self.var_gender.get(),
                    self.var_name.get(),
                    self.var_id.get(),
                    
         ))    
        messagebox.showinfo("Seccess", "update Successfully")
        con.commit()
        self.record_id()
        self.show()
        self.clear()
        
    def delete(self):
        con = sqlite3.connect(resource_path('clinic.db'))
        cur = con.cursor()
        op = messagebox.askyesno("Confirm", "Do you want to delete?")
        op == True
        cur.execute("delete from dental where aid=?", (self.var_id.get()))
        con.commit()
        self.record_id()
        messagebox.showinfo('delete', "delete from dental")
        self.show()
        self.clear()
       
    def search(self):
        con = sqlite3.connect(resource_path('clinic.db'))
        cur = con.cursor()
        try:
            if self.var_search_comb.get()=='Select':
                messagebox.showerror("Error","Select to search")
            elif self.var_search_en.get()=="":
                messagebox.showerror("Error","enter the value to search")
            else:
                column = self.var_search_comb.get().lower()
                query = f"SELECT * FROM dental WHERE {column} LIKE ?"
                cur.execute(query, ('%' + self.var_search_en.get() + '%',))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.dental_table.delete(*self.dental_table.get_children())
                    for row in rows:
                        self.dental_table.insert('',END,values=row)
                else:
                    messagebox.showerror("error","no resulte")
        except Exception as ex:
            messagebox.showerror("error",f"error to {str(ex)}")
                
            
        
        
        
        
        
if __name__=="__main__":
    root = Tk()
    obj = DentalClass(root)
    root.mainloop()


