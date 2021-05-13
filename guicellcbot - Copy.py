from tkinter import *
import tkinter
import os
from tkinter import messagebox
from tkinter import filedialog
import csv
import mysql.connector
from mysql.connector import Error
from tkinter import scrolledtext
from datetime import datetime
import time
import threading
####################################################################################################
## Replace cf_847 with your custom field you'd like to use for assiging contacts to people with   ##
##                                                                                                ##
####################################################################################################
root = Tk()
root.bg="black"
root.title('QA CELLC BOT')
today = datetime.today().strftime('%Y-%m-%d')
counter2 = 0
global stop_Threads 

stop_Threads = True
loopEnder=True
def btnClick2():
    #Create new thread so that while loop for gui can run        
    th = threading.Thread(target=btnClick)
    th.start()    

loopEnder2=0 


def btnClick():    
    print("working")
    agent=[]
    counter=0
    today = datetime.today().strftime('%Y-%m-%d')
    counter2 = 0
    texta.insert(INSERT,"Starting Bot..."+"\n")
    if var1.get()==1:
        agent.append('Abbygail')
        counter=counter+1
    if var2.get()==1:
        agent.append('SundeepR')
        counter=counter+1
    if var3.get()==1:
        agent.append('Rowan')
        counter=counter+1
    if var4.get()==1:
        agent.append('CalebP')
        counter=counter+1
    if var5.get()==1:
        agent.append('MarcoM')
        counter=counter+1
    if var6.get()==1:
        agent.append('Stacey')
        counter=counter+1
    if var7.get()==1:
        agent.append('NicolinN')
        counter=counter+1
    if var8.get()==1:
        agent.append('TmeraE')
        counter=counter+1
    if var9.get()==1:
        agent.append('VarshaS')
        counter=counter+1
    print(agent)    
    while loopEnder:  
        global loopEnder2 
        print(loopEnder2)        
        if loopEnder2==1:
            texta.insert(INSERT,"BOT HAS STOPPED"+"\n")
            break               
        st = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mydb = mysql.connector.connect(
            host="dbhost",
            user="dbusername",
            passwd="dbpassword",
            database="dbname",
        )
        mycursor = mydb.cursor()
        mycursor2 = mydb.cursor()
        mycursor3 = mydb.cursor()
        agentml = ''
        saleid = 0
        ccnum=''

        unallocated_stmt = """SELECT vtiger_contactscf.contactid AS saleid,vtiger_contactscf.cf_797 as idnum,vtiger_contactdetails.contact_no FROM vtiger_contactscf INNER JOIN vtiger_crmentity ON vtiger_crmentity.crmid=vtiger_contactscf.contactid INNER JOIN vtiger_users ON vtiger_users.id=vtiger_crmentity.smcreatorid INNER JOIN vtiger_contactdetails ON vtiger_contactdetails.contactid=vtiger_crmentity.crmid WHERE vtiger_users.user_name NOT IN('') AND vtiger_crmentity.createdtime LIKE '%s' AND setype='Contacts' AND vtiger_contactscf.cf_847='' LIMIT 1""" % (
                    today + '%')
        mycursor2.execute(unallocated_stmt)
        myresult2 = mycursor2.fetchall()
        for row in myresult2:
            saleid = row[0]
            idnum = row[1]
            ccnum= row[2]
        if saleid > 1:
            findmultiliner_stmt = """SELECT vtiger_contactscf.contactid,cf_847 FROM vtiger_contactscf INNER JOIN vtiger_crmentity ON vtiger_crmentity.crmid=vtiger_contactscf.contactid INNER JOIN vtiger_users ON vtiger_users.id=vtiger_crmentity.smcreatorid WHERE vtiger_users.user_name NOT IN('') AND cf_797='%s' AND cf_847<>'' AND vtiger_crmentity.createdtime LIKE '%s'""" % (
            idnum, today + '%')
            mycursor.execute(findmultiliner_stmt)
            myresult = mycursor.fetchall()
            for row in myresult:
                agentml = row[1]
            if agentml == '' and saleid > 1:
                assignsale_stmt = """UPDATE vtiger_contactscf SET cf_847='%s' WHERE contactid='%s'""" % (
                agent[counter2], saleid)
                mycursor.execute(assignsale_stmt)
                mydb.commit()
                texta.insert(INSERT,"Sale Assigned To:" + agent[counter2]+" at "+str(datetime.now().strftime("%H:%M:%S"))+"\n")
                counter2 = counter2 + 1                
            else:
                assignmultiliner_stmt = """UPDATE vtiger_contactscf SET cf_847='%s' WHERE contactid='%s'""" % (
                agentml, saleid)
                mycursor.execute(assignmultiliner_stmt)
                mydb.commit()
                texta.insert(INSERT,"MultiSale Assigned To: "+agentml+" at "+str(datetime.now().strftime("%H:%M:%S"))+"\n")
        if saleid == 0:           
            time.sleep(5)
            print("sleep ended")
        counter3 = counter - 1
        if counter2 >= counter:
            counter2 = 0        
         
                        
       

        

    

    
#Check boxes for selecting users to allocate to

var1 = IntVar()
Checkbutton(root, text="Abbygail", variable=var1).grid(row=1, sticky=W)

var2 = IntVar()
Checkbutton(root, text="SundeepR", variable=var2).grid(row=2, sticky=W)

var3 = IntVar()
Checkbutton(root, text="Rowan", variable=var3).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(root, text="CalebP", variable=var4).grid(row=4, sticky=W)

var5 = IntVar()
Checkbutton(root, text="MarcoM", variable=var5).grid(row=5, sticky=W)
var6 = IntVar()
Checkbutton(root, text="Stacey", variable=var6).grid(row=6, sticky=W)

var7 = IntVar()
Checkbutton(root, text="NicolinN", variable=var7).grid(row=7, sticky=W)

var8 = IntVar()
Checkbutton(root, text="TmeraE", variable=var8).grid(row=8, sticky=W)

var9 = IntVar()
Checkbutton(root, text="VarshaS", variable=var9).grid(row=9, sticky=W)


Label(root,text="\t \t ").grid(row=1,column=2, columnspan=5)

texta = Text(root, height=15, width=60,wrap=tkinter.NONE)

scrollH = tkinter.Scrollbar(root, orient=tkinter.HORIZONTAL)
scrollH.config(command=texta.xview)
texta.configure(xscrollcommand=scrollH.set)

texta.grid(row=1,column=7,rowspan=10)

#Button to break the allocation loop
def btnStop():
            global loopEnder2 
            stop=False
            stop_Threads=False                    
            loopEnder=False
            loopEnder2=1
            print(loopEnder2) 
stopButton =Button(root,text="STOP",  command=btnStop, fg="green").grid(row=11, column=1)

Label(root,text=" ").grid(row=10,column=0)

importButton =Button(root,text="RUN",  command=btnClick2, fg="green").grid(row=11, column=0)

root.mainloop()
