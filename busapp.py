
import tkinter as tk
from tkinter import *
from  tkinter import ttk

# Main window
frame = tk.Tk()
frame.attributes('-fullscreen', True)
frame.title("TextBox Input")

# Window's background image
#bacgr=PhotoImage(file="C:\\Users\\MITHUN\\OneDrive\\Desktop\\i.png")
k=Label(frame)
k.place(x=0,y=0)

# Logo
m=Frame(frame)
m.pack()
m.place(x=330,y=50)
xo=Frame(m)
xo.pack()
xo.place()
#bk=PhotoImage(file="C:\\Users\\MITHUN\\OneDrive\\Desktop\\projectforoop.png")
n=Label(xo)
n.pack()
n.place()

# Start label
l = tk.Label(frame,text="START",bg="#E0EEEE",font=250)
l.pack()
l.place(x=710,y=330)
varstar=StringVar()

# Entering values for start
inputstr=Entry(frame,width=30,font=200,textvariable=varstar)
inputstr.pack()
inputstr.place(x=580,y=360)

# Destination label
d= tk.Label(frame,text="DESTINATION",bg="#E0EEEE",font=350)
d.pack()
d.place(x=679,y=390)
vardesti=StringVar()

# Entering value for destination
inputdes =Entry(frame,width=30,font=200,textvariable=vardesti)
inputdes.pack()
inputdes.place(x=580,y=421)

#Submit button
printButton = tk.Button(frame,text = "SUBMIT",font=300,bg='#00CDCD', command = frame.destroy)
printButton.pack()
printButton.place(x=700,y=460)
frame.mainloop()
st=varstar.get()
de=vardesti.get()

# Dataset of buses for Nitte-Karkala ,Nitte-Mangalore,Nitte-Udupi
nk=['Nitte','Karkala','Ananathashaya','Gomateshwara Beta','Anekere','Bypass ','Kuntalpady','Doopadakatte','Lamina Cross','Parapadi Cross']
nm=['Nitte','Padubidri','Belman','Mangalore','Manjarpalke','Santhoor kopla','Kanjarkatte','Adve','Nandikoor']
nu=['Nitte','Padubidri','Kaup','Katpady','Udyavara','Kinnimulky','Uchilla','Udupi']

# Code for second window -  Nitte-Karkala route 
if st in nk and de in nk:

    # Main window
    pypro=tk.Tk()
    pypro.title("second")
    pypro.geometry('400x200')
    pypro.attributes('-fullscreen', True)

    #Background image
    #bacgr=PhotoImage(file="C:\\Users\\MITHUN\\OneDrive\\Desktop\\i.png")
    #j=Label(pypro,image=bacgr)
    #j.place(x=0,y=0)

    # Table
    table=Frame(pypro)
    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=50,font=100, background='#EEE8CD')
    s.configure('Treeview.Heading', rowheight=50,font=300,background='#00CDCD')
    table.pack()
    table.place(x=549,y=100)
    tab=ttk.Treeview(table)

    #Table columns
    tab['columns']=('g_BUS NAME','g_TIME')
    tab.column('#0',width=0,stretch=NO)
    tab.column("g_BUS NAME",anchor=CENTER,width=250)
    tab.column("g_TIME",anchor=CENTER,width=200)
    tab.heading('#0',text="",anchor=CENTER)
    tab.heading("g_BUS NAME",text="BUS NAME",anchor=CENTER)
    tab.heading("g_TIME",text="TIME",anchor=CENTER)
    tab.insert(parent='',index='end',iid=0,values=('Vishal','7:31 AM'))
    tab.insert(parent='',index='end',iid=1,values=('Navadurga Prasad','7:35 AM'))
    tab.insert(parent='',index='end',iid=2,values=('Kusuma','8:03 AM'))
    tab.insert(parent='',index='end',iid=3,values=('Vishal','8:10 AM'))
    tab.insert(parent='',index='end',iid=4,values=('Navadurga Prasad','8:36 AM'))
    tab.insert(parent='',index='end',iid=5,values=('Navadurga Prasad','8:41 AM'))
    tab.insert(parent='',index='end',iid=6,values=('Laxmi Ganesh','9:20 AM'))
    tab.insert(parent='',index='end',iid=7,values=('Padmambikaa','9:48 AM'))
    tab.insert(parent='',index='end',iid=8,values=('Padmambikaa','10:17 AM'))
    tab.insert(parent='',index='end',iid=9,values=('Vishal','11:33 AM'))
    tab.insert(parent='',index='end',iid=10,values=('Vishal','12:05 PM'))
    tab.insert(parent='',index='end',iid=11,values=('Vishal','12:11 PM'))
    tab.insert(parent='',index='end',iid=12,values=('Vishal','12:16 PM'))
    tab.insert(parent='',index='end',iid=13,values=('Navadurga Prasad','12:24 PM'))
    tab.insert(parent='',index='end',iid=14,values=('Bharati','12:44 PM'))
    tab.insert(parent='',index='end',iid=15,values=('Bharati','12:50 PM'))
    tab.insert(parent='',index='end',iid=16,values=('Navadurga Prasad','12:52 PM'))
    tab.insert(parent='',index='end',iid=17,values=('Vishal','1:03 PM'))
    tab.insert(parent='',index='end',iid=18,values=('Laxmi Ganesh','1:23 PM'))
    tab.insert(parent='',index='end',iid=19,values=('Reshma','1:35 PM'))
    tab.insert(parent='',index='end',iid=20,values=('Padmambikaa','1:47 PM'))
    tab.insert(parent='',index='end',iid=21,values=('Padmambikaa','2:08 PM'))
    tab.insert(parent='',index='end',iid=22,values=('Vishal','2:38 PM'))
    tab.insert(parent='',index='end',iid=23,values=('Padmambikaa','2:51 PM'))
    tab.insert(parent='',index='end',iid=24,values=('Christa kiran','2:52 PM'))
    tab.insert(parent='',index='end',iid=25,values=('Padmambikaa','3:09 PM'))
    tab.insert(parent='',index='end',iid=26,values=('Vishal','3:25 PM'))
    tab.insert(parent='',index='end',iid=27,values=('Ayra','3:28 PM'))
    tab.insert(parent='',index='end',iid=28,values=('Vishal','3:43 PM'))
    tab.insert(parent='',index='end',iid=29,values=('Shree Annapoorneshwari','3:55 PM'))
    tab.insert(parent='',index='end',iid=30,values=('Mercy','4:08 PM'))
    tab.insert(parent='',index='end',iid=31,values=('Navadurga Prasad','4:12 PM'))
    tab.insert(parent='',index='end',iid=32,values=('Vishal','4:26 PM'))
    tab.insert(parent='',index='end',iid=33,values=('Vishal','4:40 PM'))
    tab.insert(parent='',index='end',iid=34,values=('Vishal','4:46 PM'))
    tab.insert(parent='',index='end',iid=35,values=('Bharathi','4:58 PM'))
    tab.insert(parent='',index='end',iid=36,values=('Vishal','4:59 PM'))
    tab.pack()

    # Exit button
    exitButton= tk.Button(pypro,text = "EXIT",font=300,bg='#00CDCD', command =pypro.destroy )
    exitButton.pack()
    exitButton.place(x=750,y=660)
    pypro.mainloop()    

# Code for second window -  Nitte-Mangalore route    
elif st in nm and de in nm:

    # Main window
    pypro=tk.Tk()
    pypro.title("second")
    pypro.geometry('400x200')
    pypro.attributes('-fullscreen', True)

    #Background image
    #bacgr=PhotoImage(file="C:\\Users\\MITHUN\\OneDrive\\Desktop\\i.png")
    #j=Label(pypro,image=bacgr)
    #j.place(x=0,y=0)

    # Table
    table=Frame(pypro)
    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=50,font=100, background='#EEE8CD')
    s.configure('Treeview.Heading', rowheight=50,font=300,background='#00CDCD')
    table.pack()
    table.place(x=549,y=100)
    tab=ttk.Treeview(table)

    #Table columns
    tab['columns']=('g_BUS NAME','g_TIME')
    tab.column('#0',width=0,stretch=NO)
    tab.column("g_BUS NAME",anchor=CENTER,width=250)
    tab.column("g_TIME",anchor=CENTER,width=250)
    tab.heading('#0',text="S.NO",anchor=CENTER)
    tab.heading("g_BUS NAME",text="BUS NAME",anchor=CENTER)
    tab.heading("g_TIME",text="TIME",anchor=CENTER)
    tab.insert(parent='',index='end',iid=0,text='',values=('Vishal','8:00 AM'))
    tab.insert(parent='',index='end',iid=1,text='',values=('Vishal','8:10 AM')) 
    tab.insert(parent='',index='end',iid=2,text='',values=('Vishal','8:46 AM')) 
    tab.insert(parent='',index='end',iid=3,text='',values=('Navadurga','9:30 AM'))
    tab.insert(parent='',index='end',iid=4,text='',values=('Vishal','9:45 AM')) 
    tab.insert(parent='',index='end',iid=5,text='',values=('Vishal','9:58 AM'))
    tab.insert(parent='',index='end',iid=6,text='',values=('Laxmi Prasad','10:05 AM'))
    tab.insert(parent='',index='end',iid=7,text='',values=('Reshma','10:26 AM')) 
    tab.insert(parent='',index='end',iid=8,text='',values=('Padmambikaa','10:50AM')) 
    tab.insert(parent='',index='end',iid=9,text='',values=('Padmambikaa','11:10 AM'))
    tab.insert(parent='',index='end',iid=10,text='',values=('christa Kiran','11:20 AM')) 
    tab.insert(parent='',index='end',iid=11,text='',values=('Vishal','11:29 AM'))
    tab.insert(parent='',index='end',iid=12,text='',values=('Vishal','11:40 AM'))
    tab.insert(parent='',index='end',iid=13,text='',values=('Padmambikaa','11:51 AM')) 
    tab.insert(parent='',index='end',iid=14,text='',values=('Navadurga Prasad','12:00 PM')) 
    tab.insert(parent='',index='end',iid=15,text='',values=('Rajarajeshwari','12:09 PM'))
    tab.insert(parent='',index='end',iid=16,text='',values=('Shree Annapoorneshwari','12:09 PM')) 
    tab.insert(parent='',index='end',iid=17,text='',values=('Vishal','12:25 PM'))
    tab.insert(parent='',index='end',iid=18,text='',values=('Navadurga Prasad','12:33 PM'))
    tab.insert(parent='',index='end',iid=19,text='',values=('Vishal','12:35 PM')) 
    tab.insert(parent='',index='end',iid=20,text='',values=('Padmambikaa','12:45 PM')) 
    tab.insert(parent='',index='end',iid=21,text='',values=('Rajarajeshwari','12:56 PM'))
    tab.insert(parent='',index='end',iid=22,text='',values=('Navadurga Prasad','1:10 PM')) 
    tab.insert(parent='',index='end',iid=23,text='',values=('Vishal','1:21 PM'))
    tab.insert(parent='',index='end',iid=24,text='',values=('Vishal','1:32 PM'))
    tab.insert(parent='',index='end',iid=25,text='',values=('Laxmi Prasad','1:59 PM')) 
    tab.insert(parent='',index='end',iid=26,text='',values=('Vishal','2:00 PM')) 
    tab.insert(parent='',index='end',iid=27,text='',values=('Laxmi Ganesh','2:15 PM'))
    tab.insert(parent='',index='end',iid=28,text='',values=('Padmambikaa','2:37 PM')) 
    tab.insert(parent='',index='end',iid=29,text='',values=('Navadurga Prasad','2:44 PM'))
    tab.insert(parent='',index='end',iid=30,text='',values=('Padmambikaa','2:57 PM'))
    tab.insert(parent='',index='end',iid=31,text='',values=('Reshma','3:05 PM'))   
    tab.insert(parent='',index='end',iid=32,text='',values=('Vishal','3:20 PM'))
    tab.insert(parent='',index='end',iid=33,text='',values=('Vishal','3:33 PM'))
    tab.insert(parent='',index='end',iid=34,text='',values=('Vishal','3:48 PM'))
    tab.insert(parent='',index='end',iid=35,text='',values=('Padmambikaa','3:59 PM'))
    tab.insert(parent='',index='end',iid=36,text='',values=('Ayra','4:10 PM'))
    tab.insert(parent='',index='end',iid=37,text='',values=('Vishal','4:19 PM'))
    tab.insert(parent='',index='end',iid=38,text='',values=('Vishal','4:29 PM')) 
    tab.insert(parent='',index='end',iid=39,text='',values=('Bharati','4:30 PM'))
    tab.insert(parent='',index='end',iid=40,text='',values=('Vishal','4:41 PM')) 
    tab.insert(parent='',index='end',iid=41,text='',values=('Vishal','4:56 PM')) 
    tab.insert(parent='',index='end',iid=42,text='',values=('Navadurga Prasad','5:07 PM')) 
    tab.insert(parent='',index='end',iid=43,text='',values=('Navadurga Prasad','5:22 PM')) 
    tab.pack()

    # Exit button
    exitButton= tk.Button(pypro,text = "EXIT",font=300,bg='#00CDCD', command =pypro.destroy)
    exitButton.pack()
    exitButton.place(x=750,y=660)
    pypro.mainloop()

# Code for second window -  Nitte-Udupi route    
elif st in nu and de in nu:

    # Main window
    pypro=tk.Tk()
    pypro.title("second")
    pypro.geometry('400x200')
    pypro.attributes('-fullscreen', True)

    #Background image
    #bacgr=PhotoImage(file="C:\\Users\\MITHUN\\OneDrive\\Desktop\\i.png")
    #j=Label(pypro,image=bacgr)
    #j.place(x=0,y=0)

    # Table
    table=Frame(pypro)
    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=50,font=100, background='#EEE8CD')
    s.configure('Treeview.Heading', rowheight=50,font=300,background='#00CDCD')
    table.pack()
    table.place(x=549,y=100)
    tab=ttk.Treeview(table)

    #Table columns
    tab['columns']=('g_BUS NAME','g_TIME')
    tab.column('#0',width=0,stretch=NO)
    tab.column("g_BUS NAME",anchor=CENTER,width=250)
    tab.column("g_TIME",anchor=CENTER,width=250)
    tab.heading('#0',text="S.NO",anchor=CENTER)
    tab.heading("g_BUS NAME",text="BUS NAME",anchor=CENTER)
    tab.heading("g_TIME",text="TIME",anchor=CENTER)
    tab.insert(parent='',index='end',iid=0,text='',values=('Christa Jyothi','9:54 AM'))
    tab.insert(parent='',index='end',iid=1,text='',values=('Descent','9:59AM'))   
    tab.insert(parent='',index='end',iid=2,text='',values=('Christa Jyothi','10:23 AM'))
    tab.insert(parent='',index='end',iid=3,text='',values=('Sangam','10:36 AM'))
    tab.insert(parent='',index='end',iid=4,text='',values=('Naveen','11:26 AM'))
    tab.insert(parent='',index='end',iid=5,text='',values=('Naveen','11:28 AM'))
    tab.insert(parent='',index='end',iid=6,text='',values=('Naveen','11:33AM'))   
    tab.insert(parent='',index='end',iid=7,text='',values=('Naveen','12:18 PM'))
    tab.insert(parent='',index='end',iid=8,text='',values=('Shree Padma','12:38 PM'))
    tab.insert(parent='',index='end',iid=9,text='',values=('Christa Jyothi','1:07PM'))
    tab.insert(parent='',index='end',iid=10,text='',values=('Kanthi','1:30 PM'))
    tab.insert(parent='',index='end',iid=11,text='',values=('Kanthi','1:43PM'))   
    tab.insert(parent='',index='end',iid=12,text='',values=('Bharathi','1:50 PM'))
    tab.insert(parent='',index='end',iid=13,text='',values=('Sangam','2:10 PM'))
    tab.insert(parent='',index='end',iid=14,text='',values=('Christa Jyothi','3:12 PM'))
    tab.insert(parent='',index='end',iid=15,text='',values=('Naveen','3:31 PM'))
    tab.insert(parent='',index='end',iid=16,text='',values=('Naveen','3:45 PM'))   
    tab.insert(parent='',index='end',iid=17,text='',values=('Naveen','3:54 PM'))
    tab.insert(parent='',index='end',iid=18,text='',values=('Naveen','4:25 PM'))
    tab.insert(parent='',index='end',iid=19,text='',values=('Shree Padma','5:21 PM'))
    tab.pack()

    # Exit button
    exitButton= tk.Button(pypro,text = "EXIT",font=300,bg='#00CDCD', command =pypro.destroy)
    exitButton.pack()
    exitButton.place(x=750,y=660)
    pypro.mainloop()    
else:
    pass    

