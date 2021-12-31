# import sqlite3
# conn = sqlite3.connect('txl_db.db')
# print('成功')
from os import name
import sqlite3
import tkinter as tk
from tkinter.constants import CENTER, END, LEFT, RIGHT, TOP
from typing import overload
# 连接数据库（如果没有该数据库，则生成一个新的数据库）
conn = sqlite3.connect('ohh_db.db', check_same_thread= False)
print('打开数据库成功')
# import sqlite3
# conn = sqlite3('txl_db.db')
cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE "note1" (
#     "id"	INTEGER,
#     "name"	TEXT,
#     "phone"	TEXT,
#     PRIMARY KEY("id")
#   );
# ''')

def add():
  id = shu1.get()
  cursor.execute('''
  select * from note1 where id = '%s'
  '''%id)
  all=cursor.fetchall()
  if len(all) == 1:
      text.insert('insert','\n')
      text.insert('end','id is have')
  else:
      id = shu1.get()
      name = shu2.get()
      phone = shu3.get()
      address = shu4.get()
      cursor.execute('''
      INSERT INTO note1(id,name,phone,address) VALUES (?,?,?,?)
      ''',(id,name,phone,address))
      conn.commit()
      text.insert('end','susscue')
      text.insert('insert','\n')
def dele():
  id=shu1.get()
  cursor.execute('''
    DELETE FROM "main"."note1" WHERE  id = %s;
  '''%id)
  text.insert(END,'Deletion success ')
  text.insert(tk.INSERT,'\n')
  conn.commit()
def update():
  id=shu1.get()
  Name=shu2.get()
  phone=shu3.get()
  address=shu4.get()
  cursor.execute('''
    UPDATE "main"."note1" SET name=(?),phone=(?),address=(?) WHERE id = %s;
  '''%id,(Name,phone,address))
  text.insert('end','The update is successful')
  text.insert('insert','\n')
  conn.commit()
def select():
  cursor.execute('''
   select * from "main"."note1";
  ''')
  all= cursor.fetchall()
  text.insert("end",all)
  text.insert('insert','\n')
def selectname():
  Name=shu2.get()
  cursor.execute('''
    SELECT * FROM note1 where name='%s'
  '''%Name)
  all= cursor.fetchall()
  if len(all) == 0:
    text.insert(END,'no name in note1')
  else:
    text.insert("end",all)
  text.insert('insert','\n')


main = tk.Tk()
main.title('txl')
main.geometry('600x1000')

text=tk.Text(main,height=20,width=66)
text.place(relx=0.5,rely=0.6,anchor="center")

l1 = tk.Label(main, text="--id--")
l1.place(relx=0.3,rely=0.2,anchor="center")
shu1 =tk.Entry(main)
shu1.place(relx=0.5,rely=0.2,anchor="center")

l2 = tk.Label(main, text="--name--")
l2.place(relx=0.3,rely=0.23,anchor="center")
shu2 =tk.Entry(main)
shu2.place(relx=0.5,rely=0.23,anchor="center")

l3 = tk.Label(main, text="--phone--")
l3.place(relx=0.3,rely=0.26,anchor="center")
shu3 =tk.Entry(main)
shu3.place(relx=0.5,rely=0.26,anchor="center")

l3 = tk.Label(main, text="--address--")
l3.place(relx=0.3,rely=0.29,anchor="center")
shu4 =tk.Entry(main)
shu4.place(relx=0.5,rely=0.29,anchor="center")


l4 = tk.Label(main, text="----TONGXUNLU----")
l4.place(relx=0.5,rely=0.1,anchor="center")


shub1= tk.Button(main,command=add,text='add')
shub1.place(relx=0.3,rely=0.35,anchor="center")
shub2= tk.Button(main,command=dele,text='dele')
shub2.place(relx=0.41,rely=0.35,anchor="center")
shub3= tk.Button(main,command=update,text='update')
shub3.place(relx=0.54,rely=0.35,anchor="center")
Button = tk.Button(main,command = select,text='select all')
Button.place(relx=0.69,rely=0.35,anchor="center")
Button2 = tk.Button(main,command = selectname,text='select name')
Button2.place(relx=0.69,rely=0.4,anchor="center")
tk.mainloop()