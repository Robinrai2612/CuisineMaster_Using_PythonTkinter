### Importing required libraries ###
from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def system():
    root = Tk()
    root.geometry("1700x900")
    root.title("Restaurant Management System")

    ############database###########
    def Database():
        global conn, cursor
        # creating system database
        conn = sqlite3.connect("Restaurant.db")
        cursor = conn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS RECORD(ordno text, fr text ,piz text,bur text,noo text,ice text, dr text, ct text,sb text,tax text,sr text,tot text)")

    # variable datatype assignment
    orderno = StringVar()
    french = StringVar()
    pizza = StringVar()
    burger = StringVar()
    noodles = StringVar()
    icecream = StringVar()
    drinks = StringVar()
    cost = StringVar()
    subtotal = StringVar()
    tax = StringVar()
    service = StringVar()
    total = StringVar()

    # defining total function
    def tottal():
        order = (orderno.get())
        fr = (float(french.get()))
        pi = float(pizza.get())
        bu = float(burger.get())
        noo = float(noodles.get())
        ice = float(icecream.get())
        dr = float(drinks.get())

        # computing cost of items
        costfr = fr * 60
        costpi = pi * 220
        costbu = bu * 120
        costnoo = noo * 80
        costice = ice * 100
        costdr = dr * 50

        # computing the charges
        costofmeal = (costfr + costpi + costbu + costnoo + costice + costdr)
        ptax = ((costfr + costpi + costbu + costnoo + costice + costdr) * 0.18)
        sub = (costfr + costpi + costbu + costnoo + costice + costdr)
        ser = ((costfr + costpi + costbu + costnoo + costice + costdr) / 99)
        paidtax = str(ptax)
        Service = str(ser)
        overall = str(ptax + ser + sub)

        # Displaying values
        cost.set(costofmeal)
        tax.set(ptax)
        subtotal.set(sub)
        service.set(ser)
        total.set(overall)

      def reset():
        orderno.set("")
        french.set("")
        pizza.set("")
        burger.set("")
        noodles.set("")
        icecream.set("")
        drinks.set("")
        cost.set("")
        subtotal.set("")
        tax.set("")
        service.set("")
        total.set("")

       def exit():
        root.destroy()

    # Topframe
    topframe = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
    topframe.pack(side=TOP)
    # Leftframe
    leftframe = Frame(root, width=900, height=700, relief=SUNKEN)
    leftframe.pack(side=LEFT)
    # rightframe
    rightframe = Frame(root, width=400, height=700, relief=SUNKEN)
    rightframe.pack(side=RIGHT)

    ################## display data ####################
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = conn.execute("SELECT * FROM RECORD")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

   
    # add some style
    style = ttk.Style()
    style.theme_use("classic")

    style.configure("Treeview",
                    background="#ffd699",
                    foregroung="black",
                    rowheight=30,
                    fieldbackground="white"
                    )
    style.map('Treeview',
              background=[('selected', '#e67f30')])

    ###########  Creating table #############
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("ordno", "fr", "piz", "bur", "noo", "ice", "dr", "ct", "sb", "tax", "sr", "tot")
    ############ creating  for table ################
    hsb = ttk.Scrollbar(rightframe, orient="horizontal")
    hsb.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    vsb = ttk.Scrollbar(rightframe, orient="vertical")
    vsb.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)
    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("fr", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("piz", anchor=CENTER, width=60, minwidth=25)
    my_tree.column("bur", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("noo", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ice", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("dr", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sr", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=50, minwidth=25)
    # defining  headings for table
    my_tree.heading("ordno", text="Order No", anchor=CENTER)
    my_tree.heading("fr", text="French fries", anchor=CENTER)
    my_tree.heading("piz", text="Pizza", anchor=CENTER)
    my_tree.heading("bur", text="Burger", anchor=CENTER)
    my_tree.heading("noo", text="Noodles", anchor=CENTER)
    my_tree.heading("ice", text="Ice cream", anchor=CENTER)
    my_tree.heading("dr", text="Drinks", anchor=CENTER)
    my_tree.heading("ct", text="Cost", anchor=CENTER)
    my_tree.heading("sb", text="Subtotal", anchor=CENTER)
    my_tree.heading("tax", text="Tax", anchor=CENTER)
    my_tree.heading("sr", text="Service", anchor=CENTER)
    my_tree.heading("tot", text="Total", anchor=CENTER)

    my_tree.pack()
    DisplayData()

    def add():
        Database()
        
        ord1 = orderno.get()
        french1 = french.get()
        pizza1 = pizza.get()
        burger1 = burger.get()
        noodles1 = noodles.get()
        ice1 = icecream.get()
        drinks1 = drinks.get()
        cost1 = cost.get()
        subtotal1 = subtotal.get()
        tax1 = tax.get()
        service1 = service.get()
        total1 = total.get()
        if ord1 == "" or french1 == "" or pizza1 == "" or burger1 == "" or noodles1 == "" or ice1 == "" or drinks1 == "" or cost1 == "" or subtotal1 == "" or tax1 == "" or service1 == "" or total1 == "":
            messagebox.showinfo("Warning", "fill the empty field!!!")
        else:
            conn.execute(
                'INSERT INTO RECORD (ordno, fr, piz, bur ,noo, ice ,dr ,ct ,sb ,tax, sr, tot) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
                (ord1, french1, pizza1, burger1, noodles1, ice1, drinks1, cost1, subtotal1, tax1, service1, total1));
            conn.commit()
            messagebox.showinfo("Message", "Stored successfully")
       
        DisplayData()
        conn.close()

   #access data from sqlite
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = conn.execute("SELECT * FROM RECORD")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    # defining function to delete record
    def Delete():
        # open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)
            cursor = conn.execute("DELETE FROM RECORD WHERE ordno= %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


    localtime = time.asctime(time.localtime(time.time()))
  
    infolb = Label(topframe, font=('vardana', 30, 'bold'), text="Restaurant Management System", fg="#e67f30", bd=10,
                   anchor=W)
    infolb.grid(row=0, column=0)
    infolb = Label(topframe, font=('varadana', 20,), text=localtime, fg="black", anchor=W)
    infolb.grid(row=1, column=0)


    # items
    ordlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Order No.", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                             column=0)
    ordtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                   textvariable=orderno).grid(row=1, column=1)
    # french fries
    frlbl = Label(leftframe, font=('aria', 16, 'bold'), text="French Fries", fg="black", bd=10, anchor=W).grid(row=2,
                                                                                                               column=0)
    frtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                  textvariable=french).grid(row=2, column=1)
    # Pizza
    pizlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Pizza", fg="black", bd=10, anchor=W).grid(row=3,
                                                                                                         column=0)
    piztxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                   textvariable=pizza).grid(row=3, column=1)
    # burger
    burlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Burger", fg="black", bd=10, anchor=W).grid(row=4,
                                                                                                          column=0)
    burtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                   textvariable=burger).grid(row=4, column=1)
    # Hakka Noodles
    noolbl = Label(leftframe, font=('aria', 16, 'bold'), text="Noodles", fg="black", bd=10, anchor=W).grid(row=5,
                                                                                                           column=0)
    nootxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                   textvariable=noodles).grid(row=5, column=1)
    # icecream
    icelbl = Label(leftframe, font=('aria', 16, 'bold'), text="Ice Cream", fg="black", bd=10, anchor=W).grid(row=6,
                                                                                                             column=0)
    icetxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                   textvariable=icecream).grid(row=6, column=1)
    # drinks
    drinklbl = Label(leftframe, font=('aria', 16, 'bold'), text="Drinks", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                            column=2)
    drinktxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                     textvariable=drinks).grid(row=1, column=3)
    # cost
    costlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Cost", fg="blue", bd=10, anchor=W).grid(row=2, column=2)
    costtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                    textvariable=cost).grid(row=2, column=3)
    # subtotal
    sublbl = Label(leftframe, font=('aria', 16, 'bold'), text="Subtotal", fg="blue", bd=10, anchor=W).grid(row=3,
                                                                                                           column=2)
    subtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                   textvariable=subtotal).grid(row=3, column=3)
    # tax
    taxlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Tax", fg="blue", bd=10, anchor=W).grid(row=4, column=2)
    taxtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                   textvariable=tax).grid(row=4, column=3)
    # service
    servicelbl = Label(leftframe, font=('aria', 16, 'bold'), text="Service", fg="blue", bd=10, anchor=W).grid(row=5,
                                                                                                              column=2)
    servicetxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                       textvariable=service).grid(row=5, column=3)
    # total
    totallbl = Label(leftframe, font=('aria', 16, 'bold'), text="Total", fg="blue", bd=10, anchor=W).grid(row=6,
                                                                                                          column=2)
    totaltxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, bg="#e67f30", justify='right',
                     textvariable=total).grid(row=6, column=3)
    # ---button--

    # totalbutton
    totbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Total", bg="blue", fg="white", bd=10, padx=5, pady=5,
                    width=10, command=tottal).grid(row=8, column=1)
    # resetbutton
    resetbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Reset", bg="blue", fg="white", bd=10, padx=5,
                      pady=5, width=10, command=reset).grid(row=8, column=2)
    # exitbutton
    exitbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Exit", bg="#e67f30", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=exit).grid(row=8, column=3)
    # Add  recordbutton
    addbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Add", bg="blue", fg="white", bd=10, padx=5, pady=5,
                    width=10, command=add).grid(row=10, column=0)
    # Deleterecordbutton
    deletebtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Delete Record", bg="blue", fg="white", bd=10,
                       padx=5, pady=5, width=10, command=Delete).grid(row=10, column=3)

 

    def feedbackk():
        feed = Tk()
        feed.geometry("600x500")
        feed.title("Feedback form")
        conn = sqlite3.connect("Restaurant.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS FEEDBACK(n text,eid text,feedback5 text,com text)")
      
        name = StringVar()
        email = StringVar()
        comments = StringVar()

        # defining submit 
        def submit():
            n = name.get()
            eid = email.get()
            com = txt.get('1.0', END)
            feedback1 = ""
            feedback2 = ""
            feedback3 = ""
            feedback4 = ""
            if (checkvar1.get() == "1"):
                feedback1 = "Excellent"
            if (checkvar2.get() == "1"):
                feedback2 = "Good"
            if (checkvar3.get() == "1"):
                feedback2 = "Average"
            if (checkvar4.get() == "1"):
                feedback2 = "Poor"
            feedback5 = feedback1 + " " + feedback2 + " " + feedback3 + " " + feedback4
            conn = sqlite3.connect("Restaurant.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO FEEDBACK VALUES ('" + n + "','" + eid + "','" + com + "','" + feedback5 + "')")
            messagebox.showinfo("message", "data inserted !")
            feed.destroy()

        # defining cancel 
        def cancel():
            feed.destroy()

        # label#
        lb1 = Label(feed, font=("Calisto MT", 15, "bold"), text="Thanks for Visiting!", fg="black").pack(side=TOP)
        lbl2 = Label(feed, font=("calisto MT", 15), text="We're glad you chose us ! Please tell us how it was!",
                     fg="black").pack(side=TOP)
        # name
        namelbl = Label(feed, font=('vardana', 15), text="Name:-", fg="black", bd=10, anchor=W).place(x=10, y=150)
        nametxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                        textvariable=name).place(x=15, y=185)
        # email
        emaillbl = Label(feed, font=('vardana', 15), text="Email:-", fg="black", bd=10, anchor=W).place(x=280, y=150)
        emailtxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                         textvariable=email).place(x=285, y=185)
        ###checkbutton
        ratelbl = Label(feed, font=('vardana', 15), text="How would you rate us?", fg="black", bd=10, anchor=W).place(
            x=10, y=215)
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        checkvar4 = StringVar()
        c1 = Checkbutton(feed, font=('vardana', 10, "bold"), text="Excellent", bg="white", variable=checkvar1)
        c1.deselect()
        c1.place(x=15, y=265)
        c2 = Checkbutton(feed, font=('vardana', 10, "bold"), text="Good", bg="white", variable=checkvar2, )
        c2.deselect()
        c2.place(x=120, y=265)
        c3 = Checkbutton(feed, font=('vardana', 10, "bold"), text=" Average", bg="white", variable=checkvar3, )
        c3.deselect()
        c3.place(x=220, y=265)
        c4 = Checkbutton(feed, font=('vardana', 10, "bold"), text="   Poor  ", bg="white", variable=checkvar4, )
        c4.deselect()
        c4.place(x=320, y=265)
        # comments"
        commentslbl = Label(feed, font=('vardana', 15), text="Comments", fg="black", bd=10, anchor=W).place(x=10, y=300)
        txt = Text(feed, width=50, height=5)
        txt.place(x=15, y=335)
        # button
        submit = Button(feed, font=("vardana", 15), text="Submit", fg="black", bg="green", bd=2, command=submit).place(
            x=145, y=430)
        cancel = Button(feed, font=("vardana", 15), text="Cancel", fg="black", bg="red", bd=2, command=cancel).place(
            x=245, y=430)
        feed.mainloop()

    # Feedbackbutton
    feedbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Feedback", fg="black", bg="#e67f30", bd=10, padx=10,
                     pady=10, width=15, command=feedbackk).grid(row=10, column=1, columnspan=2)

   #menu
    def menu():
        roott = Tk()
        roott.title("Price Menu")
        roott.geometry("300x400")
        lblinfo = Label(roott, font=("Times New Roman", 20, "bold"), text="ITEM LIST", fg="black", bd=10)
        lblinfo.grid(row=0, column=0)
        lblprice = Label(roott, font=("Times New Roman", 20, "bold"), text="Prices", fg="black", bd=10)
        lblprice.grid(row=0, column=3)
        lblfries = Label(roott, font=("Times New Roman", 20, "bold"), text=" French Fries", fg="#e67f30", bd=10)
        lblfries.grid(row=1, column=0)
        lblpricef = Label(roott, font=("Times New Roman", 20, "bold"), text="60/-", fg="blue", bd=10)
        lblpricef.grid(row=1, column=3)
        lblpizza = Label(roott, font=("Times New Roman", 20, "bold"), text="Pizza", fg="#e67f30", bd=10)
        lblpizza.grid(row=2, column=0)
        lblpricep = Label(roott, font=("Times New Roman", 20, "bold"), text="220/-", fg="blue", bd=10)
        lblpricep.grid(row=2, column=3)
        lblburger = Label(roott, font=("Times New Roman", 20, "bold"), text="Burger", fg="#e67f30", bd=10)
        lblburger.grid(row=3, column=0)
        lblpriceb = Label(roott, font=("Times New Roman", 20, "bold"), text="120/-", fg="blue", bd=10)
        lblpriceb.grid(row=3, column=3)
        lblnoodles = Label(roott, font=("Times New Roman", 20, "bold"), text="Noodles", fg="#e67f30", bd=10)
        lblnoodles.grid(row=4, column=0)
        lblpricen = Label(roott, font=("Times New Roman", 20, "bold"), text="80/-", fg="blue", bd=10)
        lblpricen.grid(row=4, column=3)
        lblicecream = Label(roott, font=("Times New Roman", 20, "bold"), text="Ice-Cream", fg="#e67f30", bd=10)
        lblicecream.grid(row=5, column=0)
        lblpricei = Label(roott, font=("Times New Roman", 20, "bold"), text="100/-", fg="blue", bd=10)
        lblpricei.grid(row=5, column=3)
        lbldrinks = Label(roott, font=("Times New Roman", 20, "bold"), text="Drinks", fg="#e67f30", bd=10)
        lbldrinks.grid(row=6, column=0)
        lblpriced = Label(roott, font=("Times New Roman", 20, "bold"), text="50/-", fg="blue", bd=10)
        lblpriced.grid(row=6, column=3)
        roott.mainloop()
    # menubutton
    menubtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Menu", bg="#e67f30", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=menu).grid(row=8, column=0)
    root.mainloop()
system()
