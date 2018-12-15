import pyodbc
from datetime import *
import smtplib
import getpass
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\HP\Desktop\soorya.accdb;')
cursor = conn.cursor()
cursor.execute('select * from students')
lis=[]
receiver=[]
sender="soorya262000@gmail.com"
today=date.today()
for row in cursor.fetchall():
    dob=row.s_dob
    dob=dob.split('-')
    print(dob)
    if dob[1]==str(today.month) and dob[2]==str(today.day):
        receiver.append(row.s_mail_id)
        lis.append(row.s_name)

sm=smtplib.SMTP_SSL('smtp.gmail.com',465)
password=getpass.getpass()
sm.login(sender,password)
msg="Happy Birthday"
for i in range(len(lis)):
    msg=msg+' '+lis[i]+"wishes from soorya"
    rec=[receiver[i]]
    sm.sendmail(sender,rec,msg)
    print("success")

    
       
    
    
    
