# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:14:06 2020

@author: Agnij
"""
import tkinter as tk
from tkinter import Label,Button,ttk,StringVar,IntVar,W,scrolledtext,LabelFrame,Menu,filedialog,Entry,messagebox as msg,Spinbox,BOTTOM,TOP,INSERT,Canvas,YES,BOTH
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #, NavigationToolbarTkAgg
import psycopg2
import json
import traceback
import time

COLOR1 = "Gold"
COLOR2 = "Green"
COLOR3 = "Black"

class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        
        self.title("Tkinter Testing")
        self.minsize(500,400)
        self.wm_iconbitmap("check.ico")

        tab_control = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tab_control)
        tab_control.add(self.tab1, text ='Tab1')
        
        self.tab2 = ttk.Frame(tab_control)
        tab_control.add(self.tab2, text = 'Image')
        
        self.tab3 = ttk.Frame(tab_control)
        tab_control.add(self.tab3, text = 'Canvas')
        
        self.tab4 = ttk.Frame(tab_control)
        tab_control.add(self.tab4, text = 'Matplotlib Canvas')
        
        self.tab5 = ttk.Frame(tab_control)
        tab_control.add(self.tab5, text = 'File Opener')
        
        tab_control.pack(expan=1, fill = 'both')
        
        ## tab1
        self.add_widgets()
        
        ## tab3
        self.create_canvas()
        
        ## tab4
        self.create_matcanvas()
        
        ## tab5
        ## ADD POSTGRESQL Connection
        self.file()
        self.db()
        
        ## tab2
        label = tk.Label(self.tab2)
        img = Image.open('icon.jpg')
        label.img = ImageTk.PhotoImage(img)
        label['image'] = label.img
        label.pack()
        
    def createLabel(self):
        labelFont = ('times',13,'bold')
        label1 = Label(self.tab1, text = "Label")
        label1.config(font = labelFont, bg = 'black',fg='white')
        label1.grid(column = 0, row=0)
        
    def create_layout(self):
        Label(self.tab1, text = "Pack Layout Example").grid(column=0,row=0)
        Button(self.tab1, text = "No expansion").grid(column=0,row=1)
        
    def click_me(self):
        ## simple message
        msg.showinfo("Python GUI Tkinter", "This is a GUI tutorial")
        
        ## warning msg
        #msg.showwarning("Python GUI Tkinter","Warning!")
        
        ## error msg
        #msg.showerror("Python GUI Tkinter","Warning!")
        
        '''
        answer = msg.askyesnocancel("Multi-Choice Box","Keep Going?")
        if not answer:
            self.quit()
            self.destroy()
            exit()
        '''
        
        self.label.configure(text = "click_change")
        self.label.configure(foreground = 'green',background='black')
        self.button.configure(text='Si Amigos')
        
    def spin_callback(self):
        value = self.spin.get()
        ## self.controlText.insert(INSERT, value)
    
    def text_entry(self):
        self.name = StringVar()
        self.label2 = ttk.Label(self.tab1, text="Enter some text" )
        self.label2.grid(column=0,row=1)
        
        self.textbox = ttk.Entry(self.tab1, width=20, textvariable = self.name)
        self.textbox.focus()
        self.textbox.grid(column=0,row=2)
        
        self.button1 = ttk.Button(self.tab1, text = "Click", command=self.add)
        self.button1.grid(column=0,row=3)
    
    def add(self):
        self.button1.configure(text="Thanks for your response")
        self.button1.configure(state ='disabled')
        self.label2.configure(text="Entered Text -> "+self.name.get())
        
    def add1(self):
        self.button2.configure(text="Thanks for your response")
        self.button2.configure(state ='disabled')
        self.label3.configure(text="Selected Language -> "+self.languages.get())
        
        
    def create_combo(self):
        self.languages = StringVar()
        
        self.combobox = ttk.Combobox(self.tab1, width =20, textvariable = self.languages)
        self.combobox['values'] = ("Python","Java","Php","Scala")
        self.combobox.grid(column=3,row=5)
        
        self.label3 = ttk.Label(self.tab1, text='Select preferred Language')
        self.label3.grid(column=3,row=6)
        
        self.button2 = ttk.Button(self.tab1,text = 'Enter' ,command = self.add1)
        self.button2.grid(column=3,row=7)
        
    def rad_event(self):
        radSelected = self.radValues.get()
        
        if radSelected ==1:
            self.buttonx = ttk.Button(self.tab1,text = str(radSelected))
            self.buttonx.grid(column=8,row=8)
            
            #self.configure(background = 'Green')
        elif radSelected ==2:
            #self.configure(background = COLOR2)
            pass
        elif radSelected ==3:
            #self.configure(background = COLOR3)
            pass
        
    def create_radio(self):
        self.radValues = IntVar()
        self.rad1 = ttk.Radiobutton(self.tab1, text=COLOR1, value=1, variable=self.radValues ,command = self.rad_event)
        self.rad1.grid(column = 3,row=8, sticky=W ,columnspan=3)   
        
        self.rad2 = ttk.Radiobutton(self.tab1, text=COLOR2, value=2, variable=self.radValues ,command = self.rad_event)
        self.rad2.grid(column = 3,row=9, sticky=W ,columnspan=3) 
        
        self.rad3 = ttk.Radiobutton(self.tab1, text=COLOR3, value=3, variable=self.radValues ,command = self.rad_event)
        self.rad3.grid(column = 3,row=10, sticky=W ,columnspan=3) 
        
    def creat_checkbuttons(self):
        check1 = ttk.Checkbutton(self.tab1, text = 'Disabled')
        check1.grid(column=1,row=11)
    
    def create_scrolltext(self):
        scroll_w = 30
        scroll_h = 10

        scrollText = scrolledtext.ScrolledText(self.tab1, width=scroll_w, height=scroll_h,wrap =tk.WORD)
        scrollText.grid(column=0,columnspan=3)
        
        ## Spin Box
        self.spin= Spinbox(self.tab1,from_=0, to=3, command=self.spin_callback)
        self.spin.grid(column=4,row=12)
        
    def create_labelframe(self):
        ttk.Label(self.labelframe, text ='label1').grid(column=3,row=1)
        text_edit = Entry(self.labelframe, width=24)
        text_edit.grid(column=5,row=1)
        
        ttk.Label(self.labelframe, text ='label2').grid(column=3,row=2)
        text_edit1 = Entry(self.labelframe, width=24)
        text_edit1.grid(column=5,row=2)
        
    def window_close(self):
        self.quit()
        self.destroy()
        exit()
        
    def create_canvas(self):
        canvas  = Canvas(self.tab3, bg = 'black', height=250, width =300)
        coord = 10,50,240,210
        
        canvas.pack(expand =YES, fill =BOTH)
        
        #arc = canvas.create_arc(coord, start=0, extent =150, fill ='Green')
        #canvas.pack()
        img = Image.open('check.png')
        canvas.image = ImageTk.PhotoImage(img)
        canvas.create_image(0,0, image = canvas.image, anchor= 'nw')
        
    def create_matcanvas(self):
        f = Figure(figsize=(5,5), dpi = 100)
        a = f.add_subplot(111)
        
        a.plot([1,2,3,4,5,6],[9,8,7,6,5,4])
        canvas = FigureCanvasTkAgg(f, self.tab4)
        #canvas.show()
        
        canvas.get_tk_widget().pack(side =BOTTOM, fill=BOTH,expand=True)
        
        canvas._tkcanvas.pack(side=TOP, fill =BOTH, expand =True)
        
                    
    def create_menu(self):
        menuBar =Menu(self.tab1)
        self.config(menu = menuBar)
        
        filemenu = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='File', menu = filemenu)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Exit',command=self.window_close)
        filemenu.add_separator()
        filemenu.add_command(label='Open')
        
        helpmenu =Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Help', menu = helpmenu)
        helpmenu.add_command(label='About')
    
    def create_progressbar(self):
        self.btn1 = ttk.Button(self.labelframe, text = 'startProgressBar', command=self.start_progressbar)
        self.btn1.grid(column=3,row=1)
        
        self.btn2 = ttk.Button(self.labelframe, text = 'stopProgressBar', command=self.stop_progressbar)
        self.btn2.grid(column=3,row=2)
        
        self.progressbar = ttk.Progressbar(self.tab1, orient='horizontal', length= 240, mode = 'determinate')
        self.progressbar.grid(column=4,row=0, pady =10)
        
    def start_progressbar(self):
        self.progressbar.start()
        
    def stop_progressbar(self):
        self.progressbar.stop()
            
    def add_widgets(self):
        self.label = ttk.Label(self.tab1, text = 'TKinter Application')
        self.label.grid(column=1,row=0)

        self.labelframe = ttk.LabelFrame(self.tab1, text='Tkinter Label Frame Progess Bar')
        self.labelframe.grid(column=3,row=0,padx=24,pady=40)
        
        self.button = ttk.Button(self.tab1, text="Hola",command=self.click_me)
        self.button.grid(column=0,row=0)
        
        self.text_entry()
        self.create_combo()
        self.create_radio()
        self.creat_checkbuttons()
        self.create_scrolltext()
        self.create_labelframe()
        self.create_menu()
        #self.spin_box()
        self.create_progressbar()
        
    def file(self):
        self.label_frame = ttk.LabelFrame(self.tab5, text = 'Open A File')
        self.label_frame.grid(column=0,row=1,padx=20,pady=20)
        
        self.button_ = ttk.Button(self.label_frame, text='Browse a File', command=self.fialDialog)
        self.button_.grid(column =1,row=1)
        
    def fialDialog(self):
        file_name = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetype = (("jpeg","*.jpg"),("All Files", "*.*")))
        label = ttk.Label(self.label_frame, text ="")
        label.grid(column=1,row=2)
        
        label.configure(text = file_name)
        
        
    def connectToDB(self):
        try:
            self.params = json.load(open('DBSettings.json'))
            print ("Connecting to database\n	->%s" %(self.params['dbname']))
            self.conn = psycopg2.connect(**self.params)
            print ("Connected!\n")
            self.label4.configure(text="Connected to DB")
            
            self.query="""
            select id,file_name,contract_type,createdon from contract.lease where pdf_hash <> 'duplicate' order by id desc limit 1
            """
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.query)
            self.data = self.cursor.fetchone()
            
            ## GET VARIABLE FROM GUI ( QUERY PURPOSES )
            print(''.join(self.text_edit_.get()))
            
            self.id = self.data[0]
            self.filename =self.data[1]
            self.status =self.data[2]
            self.createdon=self.data[3]
            
            print('Latest File: ',str(self.createdon),' ', str(self.filename),' :: ',str(self.id), '  -->>  ',str(self.status))
            
            time.sleep(3)
            self.cursor.close()
            self.conn.close()
            self.label4.configure(text='Latest File: '+str(self.createdon)+' '+str(self.filename)+' :: '+str(self.id)+'  -->>  '+str(self.status))
            print('closed connection')
            
        except:
            print(traceback.format_exc())
            print ("Failed to connect to the DB")
            self.label4.configure(text="Connection Failed")
        
    def db(self):
        
        self.lframe = ttk.LabelFrame(self.tab5, text = 'DB Connection')
        self.lframe.grid(column=0,row=4,padx=20,pady=20)
        
        self.b_ = ttk.Button(self.lframe, text='Connection Status', command=self.connectToDB)
        self.b_.grid(column =1,row=5)
        
        self.label4 = ttk.Label(self.lframe, text='Hola')
        self.label4.grid(column=0, row=1)
        
        self.text_edit_ = Entry(self.lframe, width=24)
        self.text_edit_.grid(column=1,row=0)
        
        
window = Window()
window.mainloop()

## GUI
'''
win = tk.Tk()
win.title("Tkinter Testing")
win.minsize(500,400)

label = tk.Label(win)
img = Image.open('icon.jpg')
label.img = ImageTk.PhotoImage(img)
label['image'] = label.img

label.pack()
win.wm_iconbitmap("check.ico")
win.mainloop()
'''