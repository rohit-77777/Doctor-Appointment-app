from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import json
import requests
import pyrebase






#---------------------------------------------------------------FireBase Authentication ------------------

firebaseConfig={
    "apiKey": "AIzaSyCI6x9T000vok4BLsPzpJzHvUwrhQWBJH4",
  "authDomain": "the-day-before.firebaseapp.com",
  "databaseURL": "https://the-day-before-default-rtdb.firebaseio.com",
  "projectId": "the-day-before",
  "storageBucket": "the-day-before.appspot.com",
  "messagingSenderId": "920012516542",
  "appId": "1:920012516542:web:21f3a0c3da6001c7e042ef",
  "measurementId": "G-95VGWKCNJ6"
  }

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()



#---------------------------------------------------------------Login Function --------------------------------------

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.login)
        self.signupbutton.clicked.connect(self.create)

    def warningbox(self,message_req):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setText(f"{message_req}")
        messageBox.setWindowTitle("Error")
        messageBox.setStandardButtons(QMessageBox.Ok)

        messageBox.exec()
    def successbox(self,message_req):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setText(f"{message_req}")
        messageBox.setWindowTitle("Success")
        messageBox.setStandardButtons(QMessageBox.Ok)

        messageBox.exec()

    def login(self):
        user_name = self.user_name
        password = self.password
        if user_name.get()=="" or password.get()=="":
            self.warningbox("Enter Username and Password!")	
	    else:
            try:
                fire_url = 'https://the-day-before-default-rtdb.firebaseio.com/.json'
                request  = requests.get(fire_url)
                data = request.json()
                if user_name.get() not in data:
                    self.warningbox("Invalid User Name And Password")
                else:
                    if password.get() not in data[f"{user_name.get()}"]['password']:
                        self.warningbox("Invalid Password")
                    else:
                        self.successbox("Successfully Log in.")
                        self.close()
                        self.deshboard(user_name.get())
            except Exception as es:
                self.warningbox(f"Error Dui to : {str(es)}")   
    

    def deshboard(self,key_user):
        def book():
            if doctor_var.get() =="" or day.get() =="" or month.get() == "" or year.get() == "":
                self.warningbox("All Fields Are Required")

            else:
                db = firebase.database()
                db.child(f'{user_name.get()}').update({'doctor_info':f'{doctor_var.get()}'})
                db.child(f'{user_name.get()}').child("d_appoint").update({'day':f'{day.get()}'})
                db.child(f'{user_name.get()}').child("d_appoint").update({'month':f'{month.get()}'})
                db.child(f'{user_name.get()}').child("d_appoint").update({'year':f'{year.get()}'})

                self.successbox("Booked Appointment ")

        fire_url = 'https://the-day-before-default-rtdb.firebaseio.com/.json'
        request  = requests.get(fire_url)
        data = request.json()
        data = data[key_user]
        print(data['doctor_info'])



        des = Tk()
        des.title("Admin Panel doctor App")	
        des.maxsize(width=900 ,  height=600)
        des.minsize(width=900 ,  height=500)		

            #heading label
        heading = Label(des , text = f"User Name : {key_user}" , font = 'Verdana 20 bold',bg='red')
        heading.place(x=220 , y=50)

        f=Frame(des,height=1,width=800,bg="green")
        f.place(x=0,y=500)

        

        a=Frame(des,height=1,width=400,bg="green")
        a.place(x=0,y=195)

        b=Frame(des,height=100,width=1,bg="green")
        b.place(x=900,y=500)

        for database in data: 
            first_name = Label(des, text= f"First Name : {data['f_name']}" , font='Verdana 10 bold')
            first_name.place(x=20,y=100)

            last_name = Label(des, text= f"Last Name : {data['l_name']}" , font='Verdana 10 bold')
            last_name.place(x=20,y=130)

            age = Label(des, text= f"Age : {data['age']}" , font='Verdana 10 bold')
            age.place(x=20,y=160)

            gender = Label(des, text= f"ID : {data['gender']}" , font='Verdana 10 bold')
            gender.place(x=250,y=100)

            city = Label(des, text= f"City : {data['city']}" , font='Verdana 10 bold')
            city.place(x=250,y=130)

            add = Label(des, text= f"Address : {data['address']}" , font='Verdana 10 bold')
            add.place(x=250,y=160)

        # Book doctor Appointment App
        heading = Label(des , text = "Book Appointment" , font = 'Verdana 20 bold')
        heading.place(x=470 , y=100)	

        # Book doctorLabel 
        doctor= Label(des, text= "doctor:" , font='Verdana 10 bold')
        doctor.place(x=480,y=145)

        Day = Label(des, text= "Day:" , font='Verdana 10 bold')
        Day.place(x=480,y=165)

        Month = Label(des, text= "Month:" , font='Verdana 10 bold')
        Month.place(x=480,y=185)

        Year = Label(des, text= "Year:" , font='Verdana 10 bold')
        Year.place(x=480,y=205)


        # Book doctor Entry Box



        doctor_var = tk.StringVar()
        day = StringVar()
        month = tk.StringVar()
        year = StringVar()

        doctor_box= ttk.Combobox(des, width=30, textvariable= doctor_var, state='readonly')
        doctor_box['values']=('Andy','Charlie','Shetal','Danish','Sunil')
        doctor_box.current(0)
        doctor_box.place(x=550,y=145)

        Day = Entry(des, width=33 , textvariable = day)
        Day.place(x=550 , y=168)

        Month_Box= ttk.Combobox(des, width=30, textvariable=month, state='readonly')
        Month_Box['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
        Month_Box.current(0)
        Month_Box.place(x=550,y=188)

        Year = Entry(des, width=33 , textvariable = year)
        Year.place(x=550 , y=208)

        # button 

        btn= Button(des, text = "Search" ,font='Verdana 10 bold', width = 20, command = book)
        btn.place(x=553, y=230)




        

        # book Appoitment Details
        heading = Label(des , text = f"{user_name.get()} Appointments" , font = 'Verdana 15 bold')
        heading.place(x=20 , y=250)	

        for database in data:
            d1 = Label(des, text= f"doctor: {data['doctor_info']}" , font='Verdana 10 bold')
            d1.place(x=20,y=300)

            d2 = Label(des, text= f"Day: {data['d_appoint']['day']}" , font='Verdana 10 bold')
            d2.place(x=20,y=320)

            d3 = Label(des, text= f"Month: {data['d_appoint']['month']}" , font='Verdana 10 bold')
            d3.place(x=20,y=340)

            d4 = Label(des, text= f"Year: {data['d_appoint']['year']}" , font='Verdana 10 bold')
            d4.place(x=20,y=360)		




					
#-----------------------------------------------------End Deshboard Panel -------------------------------------
