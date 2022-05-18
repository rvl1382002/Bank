from tkinter import *
from datetime import date
import mysql.connector as mc
from tkinter import messagebox

mycon=mc.connect(host="localhost",user="root",password="Ridd 13@ug",database="bank")
todays_date=date.today()

#1------------------------------------------------------------------------------   
def aboutus():
    we=open("aboutus.txt")
    text=we.read()
    print("\n",text)
    we.close()
#2-----------------------------------------------------------------------------
def cont():
    print("\n")
    ask=input("Would you like to continue(y/n): ")
    print()
    if(ask=='y' or ask=='Y'):
        return '1'
    else:
        return '2'

#3-------------------------------------------------------------------------------
def update_acc(n):
    cur=mycon.cursor()
    q="select * from ac_holder where ac_number=%s"%(n)
    cur.execute(q)
    data=cur.fetchall()
    update=int(input('''
        What would you like to change?
            1) Aadhar number
            2) Address
            3) Mobile Number
            4) Email id
            5) City
            6) State
            7) Nationality\n'''))
    if update==1:
        adhar=int(input("Enter your new Aadhar number: "))
        q="update ac_holder set Aadhar={} where ac_number={}".format(adhar,n)
        cur.execute(q)
        mycon.commit()
        print("Your account has been updated successfully...")

    elif update==2:
        ad=input("Enter your new Address: ")
        q="update ac_holder set Address='{}' where ac_number={}".format(ad,n)
        cur.execute(q)
        mycon.commit()
        print("Your account has been updated successfully...")
    elif update==3:
        mob=int(input("Enter your new Mobile number: "))
        q="update ac_holder set Mobile={} where ac_number={}".format(mob,n)
        cur.execute(q)
        mycon.commit()
        print("Your account has been updated successfully...")
    elif update==4:
        e_id=input("Enter your new email id: ")
        q="update ac_holder set email_id='{}' where ac_number={}".format(e_id,n)
        cur.execute(q)
        mycon.commit()
        print("Your account has been updated successfully...")
    elif update==5:
        city=input("Enter your new City name: ")
        q="update ac_holder set City='{}' where ac_number={}".format(city,n)
        cur.execute(q)
        mycon.commit()
        print("Your account has been updated successfully...")
    elif update==6:
        state=input("Enter your new State name: ")
        q="update ac_holder set State='{}' where ac_number={}".format(state,n)
        cur.execute(q)
        mycon.commit()
        print("Your account has been updated successfully...")
    elif update==7:
        nation=input("Enter your new Nationality: ")
        q="update ac_holder set Nationality='{}' where ac_number={}".format(nation,n)
        cur.execute(q)
        mycon.commit()
        print("Your account has been updated successfully...")
    else:
        print("Invalid Input")
#4-------------------------------------------------------------------------------
def check_balance(n):
    cur=mycon.cursor()
    q="select * from ac_holder where ac_number=%s"%(n)
    cur.execute(q)
    data=cur.fetchall()
    print("Hello",data[0][0],"your account balance is",data[0][-3])
#5-------------------------------------------------------------------------------
def transfer(n):
    cur=mycon.cursor()
    new_ac=int(input("Enter the account no. to which the amount is to be transferred: "))
    q="select * from ac_holder where ac_number=%s"%(n)
    cur.execute(q)
    data=cur.fetchall()
    if exists(new_ac):
        amt=float(input("Enter the amount to be transferred: "))
        if data[0][-3]>amt:
            q1="update ac_holder set Balance=Balance-{} where ac_number={}".format(amt,n)
            q2="update ac_holder set Balance=Balance+{} where ac_number={}".format(amt,new_ac)
            cur.execute(q1)
            mycon.commit()
            cur.execute(q2)
            mycon.commit()
            print("Transactions completed successfully")
        else:
            print("Insufficient Balance")
    else:
        print("Invalid account number: ")
#6--------------------------------------------------------------------------------
def ac_details(n):
    cur=mycon.cursor()
    exists(n)
    print("Account No.: ",record[-3])
    print("First Name: ",record[0])
    print("Middle Name: ",record[1])
    print("Last Name: ",record[2])
    print("Date of Birth Name: ",record[3])
    print("Gender: ",record[4])
    print("Nationality: ",record[5])
    print("Address: ",record[6])
    print("State: ",record[7])
    print("City: ",record[8])
    print("Aadhar no.: ",record[9])
    print("Mobile no.: ",record[10])
    print("email_id: ",record[11])
    print("Balance: ",record[13])
    print("Date of account creation: ",record[14])
#7----------------------------------------------------------------------------
def deposit(n):
    cur=mycon.cursor()
    amt=float(input("Enter the amount: "))
    depo="update ac_holder set Balance=Balance+{} where ac_number={}".format(amt,n)
    cur.execute(depo)
    mycon.commit()
    print("Your account has been updated successfully...")
    cur.execute("select * from ac_holder where ac_number=%s"%(n))
    data=cur.fetchall()
    print("Now,\n\tYour balance is",data[0][-3])
#8------------------------------------------------------------------------------
def withdraw(n):
    cur=mycon.cursor()
    q="select * from ac_holder where ac_number=%s"%(n)
    cur.execute(q)
    data=cur.fetchall()
    amt=float(input("Enter the amount: "))
    if(amt>0 and amt<=data[0][-3]):
        draw="update ac_holder set Balance=Balance-{} where ac_number={}".format(amt,n)
        cur.execute(draw)
        mycon.commit()
        print("Your account has been updated successfully...")
        cur.execute("select * from ac_holder where ac_number=%s"%(n))
        data=cur.fetchall()
        print("Now,\n\tYour balance is",data[0][-3])
    else:
        print("We are sorry to inform you that you have Insufficient Balance")
#9-----------------------------------------------------------------------------
def delete(n):
    cur=mycon.cursor()
    q1="delete from ac_holder where ac_number={}".format(n)
    q="select * from ac_holder where ac_number=%s"%(n)
    cur.execute(q)
    data=cur.fetchall()
    a=int(input('''
                   1. Transfer your balance to other account
                   2. Withdraw all balance\n'''))    
    if(a==2):
        cur.execute(q1)
        mycon.commit()
    elif(a==1):
        new_ac=int(input("Enter the account number to which your balance is to be transferred"))
        q2="update ac_holder set Balance=Balance+{} where ac_number={}".format(data[0][-3],new_ac)
        cur.execute(q1)
        mycon.commit()
        cur.execute(q2)
        mycon.commit()
    else:
        print("Invalid Input")
#10-----------------------------------------------------------------------------
def create_ac():
    global name_1
    global name_2
    global name_3
    global var1
    global var2
    global var3
    global gender
    global nationality
    global address
    global var4
    global city
    global aadhar
    global mobile
    global email
    global t

    t=Tk()
    t.geometry('1100x750')
    t.title("My Bank! Your own bank")
    head=Label(t,text="Create Account",width=20,font=("bold",25))#.grid(row=0)
    head.place(x=300,y=20)

    
    label1=Label(t,text="First Name: ", width=20,font=("bold",15))#.grid(row=100)
    label1.place(x=50,y=100)
    name_1=Entry(t)
    name_1.place(x=250,y=105)
    
    label2=Label(t,text="Middle Name: ",width=20,font=("bold",15))
    label2.place(x=400,y=100)
    name_2=Entry(t)
    name_2.place(x=600,y=105)
    
    label3=Label(t,text="Last Name: ",width=20,font=("bold",15))
    label3.place(x=750,y=100)
    name_3=Entry(t)
    name_3.place(x=950,y=105)
    
    label4=Label(t,text="Date of birth: ",width=20,font=("bold",15))
    label4.place(x=50,y=150)
    var1=StringVar(t)
    var2=StringVar(t)
    var3=StringVar(t)
    var1.set("1")
    var2.set("January")
    var3.set("2019")
    date=OptionMenu(t,var1, '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
    date.place(x=250,y=150)
    month=OptionMenu(t,var2," January","February","March","April","May","June","July","August","September","October","November","December")
    month.place(x=300,y=150)
    year=OptionMenu(t,var3, '2019','2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003','2002','2001','2000','1999','1998','1997','1996','1995','1994','1993','1992','1991','1990','1989','1988',' 1987','1986',' 1985','1984','1983','1982','1981','1980','1979','1978','1977','1976','1975','1974','1973','1972','1971','1970','1969','1968','1967','1966','1965','1964','1963','1962','1961','1960','1959','1958','1957','1956','1955','1954','1953','1952','1951','1950','1949','1948','1947','1946','1945','1944','1943','1942','1941','1940','1939','1938','1937','1936','1935','1934','1933','1932','1931','1930','1929','1928','1927','1926','1925','1924','1923','1922','1921','1920','1919','1918','1917','1916','1915','1914','1913','1912','1911','1910','1909','1908','1907','1906','1905','1904','1903','1902','1901','1900')
    year.place(x=385,y=150)
    
    label5=Label(t,text="Gender: ",width=20,font=("bold",15))
    label5.place(x=500,y=150)
    gender = IntVar()
    Radiobutton(t, text="Male",padx = 5, variable=gender, value='1').place(x=700,y=155)
    Radiobutton(t, text="Female",padx = 20, variable=gender, value='2').place(x=750,y=155)
    
    label6=Label(t,text="Nationality: ",width=20,font=("bold",15))
    label6.place(x=50,y=200)
    nationality=Entry(t)
    nationality.place(x=250,y=205)
    
    label7=Label(t,text="Address: ",width=20,font=("bold",15))
    label7.place(x=50,y=250)
    address=Entry(t,width=100)
    address.place(x=250,y=255)
    
    label8=Label(t,text="State",width=20,font=("bold",15))
    label8.place(x=50,y=300)
    var4=StringVar(t)   
    var4.set("Andhra Pradesh")
    state=OptionMenu(t, var4, "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman & Diu","The Government of NCT of Delhi","Jammu & Kashmir","Ladakh","Lakshadweep","Puducherry")
    state.place(x=250,y=300)
    
    label9=Label(t,text="City",width=20,font=("bold",15))
    label9.place(x=50,y=350)
    city=Entry(t)
    city.place(x=250,y=355)
    
    label10=Label(t,text="Aadhar no.: ",width=20,font=("bold",15))
    label10.place(x=50,y=400)
    aadhar=Entry(t)
    aadhar.place(x=250,y=405)
    
    label11=Label(t,text="Mobile no.: ",width=20,font=("bold",15))
    label11.place(x=50,y=450)
    mobile=Entry(t)
    mobile.place(x=250,y=455)
    
    label12=Label(t,text="Email id: ",width=20,font=("bold",15))
    label12.place(x=50,y=500)
    email=Entry(t,width=30)
    email.place(x=250,y=505)
    
    Button(t,text="Submit",bg='brown',fg='white',command=submit).place(x=600,y=580)
    t.mainloop()
    return new_ac_no
#11---------------------------------------------------------------------------
def submit():
    n1=name_1.get()
    n2=name_2.get()
    n3=name_3.get()
    dict1={"January":'1',"February":'2',"March":'3',"April":'4',"May":'5',"June":'6',"July":'7',"August":'8',"September":'9',"October":'10',"November":'11',"December":'12'}
    dob=var3.get()+'-'+dict1[var2.get()]+'-'+var1.get()
    dict2={1:'M',2:'F'}
    sex=dict2[gender.get()]
    national=nationality.get()
    add=address.get()
    s=var4.get()
    c=city.get()
    adhar=aadhar.get()
    mob=mobile.get()
    e_id=email.get()
    name_1.delete(first=0,last=100)
    name_2.delete(first=0,last=100)
    name_3.delete(first=0,last=100)
    nationality.delete(first=0,last=100)
    address.delete(first=0,last=100)
    city.delete(first=0,last=100)
    aadhar.delete(first=0,last=100)
    mobile.delete(first=0,last=100)
    email.delete(first=0,last=100)
    #print(n1,n2,n3,dob,sex,national,add,s,c,adhar,mob,e_id,todays_date)
    
    cur=mycon.cursor()
    query="insert into ac_holder(first_name,middlename,lastname,DOB,Gender,Nationality,Address,State,City,Aadhar,Mobile,email,Date_of_creation) values('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}')".format(n1,n2,n3,dob,sex,national,add,s,c,adhar,mob,e_id,todays_date)
    cur.execute(query)
    mycon.commit()
    destroy(t)
    pass_entry()    
#12-------------------------------------------------------------------------
def destroy(n):
    n.destroy()
#13-------------------------------------------------------------------------
def pass_entry():
    global t2
    global passwd
    global passwd_confirm
    global new_ac_no
    cur=mycon.cursor()
    cur.execute("select * from ac_holder")
    data=cur.fetchall()
    new_ac_no=data[-1][12]
    t2=Tk()
    t2.geometry("1200x600")
    t2.title("My Bank")
    heading1=Label(t2,text="Congrats...",width=20,font=("bold",25))
    heading2=Label(t2,text=" You have successfully created an account in My Bank",width=60,font=("bold",20))
    heading1.place(x=20,y=10)
    heading2.place(x=80,y=70)
    
    lab1=Label(t2,text="Your account number is ",width=50,font=("bold",20))
    lab1.place(x=50,y=180)
    lab2=Label(t2,text=new_ac_no,width=13,font=("bold",22))
    lab2.place(x=600,y=180)

    lab3=Label(t2,text="Enter a Password: ",font=("bold",20))
    lab3.place(x=150,y=250)
    passwd=Entry(t2,show="#")
    passwd.place(x=400,y=260)
    
    lab4=Label(t2,text="Confirm Password: ",font=("bold",20))
    lab4.place(x=150,y=300)
    passwd_confirm=Entry(t2,show="#")
    passwd_confirm.place(x=400,y=310)

    Button(t2,text="Done",bg='brown',fg='white',command=passwd_store).place(x=500,y=400)
    t2.mainloop()
#14----------------------------------------------------------------------------
def passwd_store():
    password=passwd.get()
    confirm=passwd_confirm.get()
    cur=mycon.cursor()
    cur.execute("select * from ac_holder")
    x=cur.fetchall()
    n=x[-1][-4]
    if(password==confirm):
        query="update ac_holder set Password='{}' WHERE ac_number={}".format(password,n)
        cur.execute(query)
        mycon.commit()
        destroy(t2)
    else:
        messagebox.showinfo("Error","Password Doesnt match!!! try again")
        pass_entry()
        destroy(t2)

#-------------------------------------------------------------------
def exists(n):
    global record
    cur=mycon.cursor()
    cur.execute("select * from ac_holder")
    data=cur.fetchall()
    for ac in data:
        if ac[-4]==n:
            record=ac
            return True
    else:
        return False
#------------------------------------------------------------------------------
def log():
    global z
    global ac_num
    z='2'
    ac_num=int(ac_no.get())
    password=passwd.get()
    cur=mycon.cursor()
    cur.execute("select * from ac_holder")
    data=cur.fetchall()
    for x in data:
        a=x[-4]
        if a==ac_num and x[-1]==password:
            print("Logged in Successfully")
            z='abc'
            tk.destroy()
    
    if z=='2':
        messagebox.showinfo("Oops","Id or password incorrect! Try again")
        ac_no.delete(first=0,last=50)
        passwd.delete(first=0,last=50)
        login()
    

def login():
    global ac_no
    global passwd
    
    tk.geometry("1000x600")
    tk.title("My Bank")
    heading1=Label(tk,text="Welcome",width=20,font=("bold",25))
    heading2=Label(tk,text="User Login",width=25,font=("bold",20))
    heading1.place(x=20,y=10)
    heading2.place(x=80,y=70)

    lab3=Label(tk,text="Account number: ",font=("bold",20))
    lab3.place(x=150,y=150)
    ac_no=Entry(tk)
    ac_no.place(x=400,y=160)

    lab4=Label(tk,text="Password: ",font=("bold",20))
    lab4.place(x=150,y=200)
    passwd=Entry(tk,show="*")
    passwd.place(x=400,y=210)

    Button(tk,text="Login",bg='brown',fg='white',command=log).place(x=500,y=400)
    tk.mainloop()
    return z

def check_login():
    global tk
    tk=Tk()
    return login(),ac_num
#--------------------------------------------------------