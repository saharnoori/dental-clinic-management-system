from tkinter import *
from tkinter import ttk , messagebox
from PIL import Image, ImageTk
import sqlite3
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)   



class XraysClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("995x550+50+120")
        self.root.title("X-rays")
        self.root.resizable(False,False)
        self.root.config(bg='white')
        
        
       #================================ varibales ==================================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_age = StringVar()
        self.var_date = StringVar()
        self.var_state = StringVar()
        self.var_price = StringVar()
        self.var_contact = StringVar()
        self.var_address = StringVar()
       
        #================================ search fram =========================
        search_frame = LabelFrame(self.root, text='البحث', font=('goudy old style', 12, 'bold'), bd=2, relief=RIDGE, bg='white')
        search_frame.place(x=370, y=20, width=600, height=70)
        #================================ options ==========================
        cmb_search = ttk.Combobox(search_frame,textvariable=self.var_searchby, values=("Select","name","contact"), justify=CENTER, state='readonly', font=('goudy old style',15)) 
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        
        self.txt_search = Entry(search_frame, textvariable=self.var_searchtxt, font=("tajwal", 15), bg='lightyellow', justify=(CENTER)).place(x=200, y=10, width=210)
        
        self.btn_search = Button(search_frame, text='بحث', font=('goudy old style',15), bg='#005c78', fg='white', cursor='hand2',command=self.search).place(x=420, y=9, width=150, height=30)
        
        
        #================================== title ==============================
        self.title = Label(self.root, text='التفاصيل', font=('goudy old style', 15),bg='#005c78', fg='white').place(x=340, y=100, width=645)
        
      #===================================== image ===================================
        self.logo = Image.open(resource_path("C:/Users/Ideapad 3/OneDrive/Desktop/CLINIC_APP/images/xray.jpeg"))
        self.logo = self.logo.resize((325,200))
        self.logo = ImageTk.PhotoImage(self.logo) 
        
        lbl_img = Label(self.root, image=self.logo)
        lbl_img.place(x=5, y=5, width=325, height=200)
        
        
        #========================================== labal + entrys =========================
        lbl_name = Label(self.root, text='الأسم', font=('tajwal', 15),bg='white').place(x=940, y=145)
        lbl_gender = Label(self.root, text='الجنس', font=('tajwal', 15),bg='white').place(x=710, y=150)
        lbl_age = Label(self.root, text='العمر', font=('tajwal', 15),bg='white').place(x=500, y=150)
        
        en_name = Entry(self.root,textvariable=self.var_name, font=('tajwal',15), bg='lightyellow', justify=CENTER).place(x=780, y=150, width=150)
        
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender, values=("Select","ذكر","انثى"), state='readonly', justify=CENTER, font=('tajwal', 15))
        cmb_gender.place(x=550, y=150, width=150)
        cmb_gender.current(0)
        
        en_age = Entry(self.root,textvariable=self.var_age, font=('tajwal',15), bg='lightyellow', justify=CENTER).place(x=350, y=150, width=150) 
        
        lbl_date = Label(self.root, text='التأريخ', font=('tajwal', 15),bg='white').place(x=940, y=200)
        lbl_state = Label(self.root, text='الحالة', font=('tajwal', 15),bg='white').place(x=710, y=200)
        lbl_price = Label(self.root, text='المبلغ', font=('tajwal', 15),bg='white').place(x=500, y=200)
        
        en_date = Entry(self.root,textvariable=self.var_date, font=('tajwal',15), bg='lightyellow', justify=CENTER).place(x=780, y=200, width=150) 
        en_state = Entry(self.root,textvariable=self.var_state, font=('tajwal',15), bg='lightyellow', justify=CENTER).place(x=550, y=200, width=150) 
        en_price = Entry(self.root,textvariable=self.var_price, font=('tajwal',15), bg='lightyellow', justify=CENTER).place(x=350, y=200, width=150) 
        
        lbl_contact = Label(self.root, text='الهاتف', font=('tajwal', 15),bg='white').place(x=940, y=250)
        lbl_address = Label(self.root, text='العنوان', font=('tajwal', 15),bg='white').place(x=701, y=250)
        
        en_contact = Entry(self.root,textvariable=self.var_contact, font=('tajwal',15), bg='lightyellow', justify=CENTER).place(x=780, y=250, width=150) 
        en_address = Entry(self.root, textvariable=self.var_address, font=('tajwal',15), bg='lightyellow', justify=CENTER).place(x=350, y=250, width=350) 
        
        #========================================== buttons =================================
        btn_add =Button(self.root, text='اضافة', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2',command=self.add).place(x=175, y=215, width=155, height=28)
        btn_update =Button(self.root, text='تعديل', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2',command=self.update ).place(x=5, y=215, width=155, height=28)
        btn_delete =Button(self.root, text='حذف', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2', command= self.delete).place(x=5, y=250, width=155, height=28)
        btn_clear =Button(self.root, text='تفريغ', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2',command=self.clear ).place(x=175, y=250, width=155, height=28)
        
        
        #============================================= treeview frame ========================
        xray_frame = Frame(self.root, bd=3, relief=RIDGE)
        xray_frame.place(x=0, y=290, width=995, height=260)
        
        scrolly = Scrollbar(xray_frame, orient=VERTICAL)
        scrollx = Scrollbar(xray_frame, orient=HORIZONTAL)
        
        self.Xray_Table =ttk.Treeview(xray_frame, columns=("address","contact", "price", "state","date", "age","gender", "name", "xid"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        
        scrollx.config(command=self.Xray_Table.xview)
        scrolly.config(command=self.Xray_Table.yview)
        
        self.Xray_Table.heading("address", text='العنوان')
        self.Xray_Table.heading("contact", text='الهاتف')
        self.Xray_Table.heading("price", text='المبلغ')
        self.Xray_Table.heading("state", text='الحالة')
        self.Xray_Table.heading("date", text='التاريخ')
        self.Xray_Table.heading("age", text='العمر')
        self.Xray_Table.heading("gender", text='الجنس')
        self.Xray_Table.heading("name", text='الأسم')
        self.Xray_Table.heading("xid", text='التسلسل')
        
        self.Xray_Table["show"]="headings"
        
        self.Xray_Table.column("xid", width=20, anchor=NE)
        self.Xray_Table.column("name", width=100, anchor=NE)
        self.Xray_Table.column("gender", width=40, anchor=NE)
        self.Xray_Table.column("age", width=30, anchor=NE)
        self.Xray_Table.column("date", width=100, anchor=NE)
        self.Xray_Table.column("state", width=100, anchor=NE)
        self.Xray_Table.column("price", width=50, anchor=NE)
        self.Xray_Table.column("contact", width=100, anchor=NE)
        self.Xray_Table.column("address", width=100, anchor=NE)
        self.Xray_Table.pack(fill=BOTH, expand=1)
        self.Xray_Table.bind("<ButtonRelease-1>",self.get_data )
        self.show()
        
        
    def reco_id(self):
        con = sqlite3.connect(resource_path('clinic.db'))
        cur = con.cursor()
        cur.execute("""
        WITH RECURSIVE cte AS (
         SELECT ROW_NUMBER() OVER (ORDER BY xid) AS new_id, xid
         FROM xrays
        )
        UPDATE xrays
        SET xid = (SELECT new_id FROM cte WHERE cte.xid = xrays.xid) 
                 
        """)    
        con.commit()
        
        
    def add(self):
        con =sqlite3.connect(resource_path('clinic.db'))
        cur = con.cursor()
        if (self.var_address.get()=="" or self.var_contact.get()=="" or self.var_price.get()=="" or self.var_state.get()=="" or self.var_date.get()=="" or self.var_age.get()=="" or self.var_gender.get()=="" or self.var_name.get()==""):
            messagebox.showerror("Error", "please inter all the data")
        else:
          cur.execute("Insert into xrays (address , contact, price, state, date, age, gender, name) values(?,?,?,?,?,?,?,?)",(
              self.var_address.get(),
              self.var_contact.get(),
              self.var_price.get(),
              self.var_state.get(),
              self.var_date.get(),
              self.var_age.get(),
              self.var_gender.get(),
              self.var_name.get(),
          ))    
          messagebox.showinfo("Success", "add successfully")
          con.commit()
          self.reco_id()
          self.show()
          self.clear()
       
       
    # def show(self):
    #     con = sqlite3.connect(resource_path('clinic.db'))
    #     cur = con.cursor()
    #     try:
    #         cur.execute("select * from xrays")
    #         rows = cur.fetchall()
    #         self.Xray_Table.delete(*self.Xray_Table.get_children())
    #         for row in rows:
    #             self.Xray_Table.insert('', END, values=row)
    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error xrays to : {str(ex)}")   
        
    def show(self):
            con = sqlite3.connect(resource_path('clinic.db'))
            cur = con.cursor()
            try:
                cur.execute("""
                SELECT address, contact, price, state, date, age, gender, name, xid
                FROM xrays
                """)
                rows = cur.fetchall()
                self.Xray_Table.delete(*self.Xray_Table.get_children())
                for row in rows:
                    self.Xray_Table.insert('', END, values=row)
            except Exception as ex:
              messagebox.showerror("Error", str(ex))
   
        
        
    def clear(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_age.set("")
        self.var_date.set("")
        self.var_state.set("")
        self.var_price.set("")
        self.var_contact.set("")
        self.var_address.set("")
        
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        
        
        self.show()   
        
    def get_data(self, ev):
        f = self.Xray_Table.focus()
        contant = (self.Xray_Table.item(f)) 
        row = contant['values'] 
        
        self.var_address.set(row[0])
        self.var_contact.set(row[1])
        self.var_price.set(row[2])
        self.var_state.set(row[3])
        self.var_date.set(row[4])
        self.var_age.set(row[5])
        self.var_gender.set(row[6])
        self.var_name.set(row[7])
        self.var_id.set(row[8])
          
        
    def update(self):
        con = sqlite3.connect(resource_path('clinic.db'))
        cur = con.cursor()
        cur.execute("Update xrays SET address=?, contact=?, price=?, state=?, date=?, age=?, gender=?, name=? WHERE xid=? ",(
                        self.var_address.get(),
                        self.var_contact.get(),
                        self.var_price.get(),
                        self.var_state.get(),
                        self.var_date.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_name.get(),
                        self.var_id.get(),
                        
                     ))
        con.commit()
        self.reco_id()
        self.show()
        self.clear()
        
    def delete(self):
        con = sqlite3.connect(resource_path('clinic.db')) 
        cur = con.cursor()
        op = messagebox.askyesno("confirm", "Do you really want to delete=?") 
        #op = True
        if op:
            cur.execute("delete from xrays where xid=?", (self.var_id.get(),))
            con.commit()
        #self.reco_id()
        messagebox.showinfo("Delete, xrays delet Successfully")
        self.show()
        self.clear() 
    
    def search(self):
        con = sqlite3.connect(resource_path('clinic.db')) 
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "select to search")
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "to search inter value")
            else:
                query = f"SELECT * FROM xrays WHERE {self.var_searchby.get()} LIKE ?"
                cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.Xray_Table.delete(*self.Xray_Table.get_children())
                    for row in rows:
                        self.Xray_Table.insert('', END,values=row)
                else:
                    messagebox.showerror("Error", "No resulte")
        except Exception as ex:
            messagebox.showerror("Error", f"error to : {str(ex)}")                    
                        
                            
           
       
       
       
if __name__=="__main__":
    root = Tk()
    obj = XraysClass(root)
    root.mainloop()
          