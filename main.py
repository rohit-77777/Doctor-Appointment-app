from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import PIL
import pymysql
import json
import requests
import pyrebase
from requests.api import head






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
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()	


def login():
	if user_name.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password",parent=win)	
	else:
		try:			
			fire_url = 'https://the-day-before-default-rtdb.firebaseio.com/.json'
			request  = requests.get(fire_url)
			data = request.json()
			if user_name.get() not in data:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)
			else:
				if password.get() not in data[f"{user_name.get()}"]['password']:
					messagebox.showerror("Error" , "Invalid Password", parent = win)
				else:
					messagebox.showinfo("Success" , "Successfully Login" , parent = win)
					close()
					deshboard(user_name.get())
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)

#---------------------------------------------------------------End Login Function ---------------------------------

#---------------------------------------------------- DeshBoard Panel -----------------------------------------
def deshboard(key_user):

	def book():
		if doctor_var.get() =="" or day.get() =="" or month.get() == "" or year.get() == "":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = des)

		else:
			book_url = f"https://the-day-before-default-rtdb.firebaseio.com/{key_user}.json"
			print(book_url)
			request  = requests.get(book_url)
			print(key_user)
			data = request.json()
			print(data)
			if 'doctor_info' not in data:
				fire_storage = str({f'\"doctor_info\":{{"d_appoint":\"{doctor_var.get()}\","day":\"{day.get()}\","month":\"{month.get()}\","year":\"{year.get()}\"}}'})
				print(fire_storage)
				fire_storage = fire_storage.replace(".","-")
				fire_storage = fire_storage.replace("\'","")
				to_database = json.loads(fire_storage)
				requests.patch(url = book_url,json = to_database)
				
			else:
				db = firebase.database()
				db.child(f'{user_name.get()}').child("doctor_info").update({'d_appoint':f'{doctor_var.get()}'})
				db.child(f'{user_name.get()}').child("doctor_info").update({'day':f'{day.get()}'})
				db.child(f'{user_name.get()}').child("doctor_info").update({'month':f'{month.get()}'})
				db.child(f'{user_name.get()}').child("doctor_info").update({'year':f'{year.get()}'})
			messagebox.showinfo("Success" , "Booked Appointment " , parent = des)




	fire_url = 'https://the-day-before-default-rtdb.firebaseio.com/.json'
	request  = requests.get(fire_url)
	data = request.json()
	data = data[key_user]



	des = Tk()
	des.config(bg="#ccff33")
	des.title("Admin Panel doctor App")	
	des.maxsize(width=1000 ,  height=520)
	des.minsize(width=1000 ,  height=520)		

		#heading label
	heading = Label(des , text = f"User Name : {key_user}" , font = 'cambri 35 bold',bg='#ccff33',fg='#ff0000')
	heading.place(x=190 , y=10)

	f=Frame(des,height=1,width=460,bg="dark green")
	f.place(x=0,y=85)

	

	a=Frame(des,height=1,width=460,bg="dark green")
	a.place(x=0,y=230)

	b=Frame(des,height=145,width=1,bg="dark green")
	b.place(x=460,y=85)

	for database in data: 
		first_name = Label(des, text= f"First Name : {data['f_name']}" , font='cambri 15 bold')
		first_name.place(x=20,y=95)

		last_name = Label(des, text= f"Last Name : {data['l_name']}" , font='cambri 15 bold')
		last_name.place(x=20,y=145)

		add = Label(des, text= f"Address : {data['address']}" , font='cambri 15 bold')
		add.place(x=40,y=194)

		gender = Label(des, text= f"ID : {data['gender']}" , font='cambri 15 bold')
		gender.place(x=277,y=95)

		city = Label(des, text= f"City : {data['city']}" , font='cambri 15 bold')
		city.place(x=260,y=145)

		
		age = Label(des, text= f"Age : {data['age']}" , font='cambri 15 bold')
		age.place(x=260,y=194)

	# Book doctor Appointment App
	heading = Label(des , text = "Book Appointment" , font = 'cambri 27 bold',fg='#9900cc')
	heading.place(x=590 , y=79)	

	# Book doctorLabel 
	doctor= Label(des, text= "Doctor:" , font='cambri 15 bold')
	doctor.place(x=598,y=146)

	Day = Label(des, text= "Day:" , font='cambri 15 bold')
	Day.place(x=625,y=189)

	Month = Label(des, text= "Month:" , font='cambri 15 bold')
	Month.place(x=602,y=235)

	Year = Label(des, text= "Year:" , font='cambri 15 bold')
	Year.place(x=620,y=280)

	heading.config(bg='#ccff33')
	first_name.config(bg='#ccff33')
	last_name.config(bg='#ccff33')
	age.config(bg='#ccff33')
	gender.config(bg='#ccff33')
	doctor.config(bg='#ccff33')
	Day.config(bg='#ccff33')
	Month.config(bg='#ccff33')
	Year.config(bg='#ccff33')
	city.config(bg='#ccff33')
	add.config(bg='#ccff33')
	# Book doctor Entry Box



	doctor_var = tk.StringVar()
	day = StringVar()
	month = tk.StringVar()
	year = StringVar()

	doctor_box= ttk.Combobox(des, width=30, textvariable= doctor_var, state='readonly')
	doctor_box['values']=('Andy','Charlie','Shetal','Danish','Sunil')
	doctor_box.current(0)
	doctor_box.place(x=685,y=152)

	Day = Entry(des, width=33 , textvariable = day)
	Day.place(x=685 , y=195)

	Month_Box= ttk.Combobox(des, width=30, textvariable=month, state='readonly')
	Month_Box['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
	Month_Box.current(0)
	Month_Box.place(x=685,y=240)

	Year = Entry(des, width=33 , textvariable = year)
	Year.place(x=685 , y=287)

	# button 

	btn= Button(des, text = "Search" ,font='cambri 11 bold', width = 20, command = book)
	btn.place(x=691, y=340)




	

	# book Appoitment Details
	heading = Label(des , text = f"{key_user} Appointments" , font = 'cambri 24 bold',fg='#00c462')
	heading.place(x=20 , y=252)
	heading.config(bg='#ccff33')

	for database in data:
		d1 = Label(des, text= f"Doctor: {data['doctor_info']['d_appoint']}" , font='cambri 15 bold')
		d1.place(x=20,y=310)

		d2 = Label(des, text= f"Day: {data['doctor_info']['day']}" , font='cambri 15 bold')
		d2.place(x=20,y=360)

		d3 = Label(des, text= f"Month: {data['doctor_info']['month']}" , font='cambri 15 bold')
		d3.place(x=20,y=410)

		d4 = Label(des, text= f"Year: {data['doctor_info']['year']}" , font='cambri 15 bold')
		d4.place(x=20,y=460)		

	d1.config(bg='#ccff33')
	d2.config(bg='#ccff33')
	d3.config(bg='#ccff33')
	d4.config(bg='#ccff33')


					
#-----------------------------------------------------End Deshboard Panel -------------------------------------
#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
	# signup database connect 
	def action():
		if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
		elif password.get() != very_pass.get():
			messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
		else:
			fire_url = 'https://the-day-before-default-rtdb.firebaseio.com/.json'
			request  = requests.get(fire_url)
			data = request.json()
			if f"{user_name.get()}" in data:
				messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
			else:
				fire_url = 'https://the-day-before-default-rtdb.firebaseio.com/.json'
				fire_storage = str({f'\"{user_name.get()}\":{{"password":\"{password.get()}\","f_name":\"{first_name.get()}\","l_name":\"{last_name.get()}\","age":\"{age.get()}\","gender":\"{var.get()}\","city":\"{city.get()}\","address":\"{add.get()}\"}}'})
				
				

				

				print(fire_storage)


				fire_storage = fire_storage.replace(".","-")
				fire_storage = fire_storage.replace("\'","")
				to_database = json.loads(fire_storage)

				print((to_database))
				requests.patch(url = fire_url,json = to_database)
				messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
				clear()
				switch()
	# close signup function			
	def switch():
		winsignup.destroy()

	# clear data function
	def clear():
		first_name.delete(0,END)
		last_name.delete(0,END)
		age.delete(0,END)
		var.set("Male")
		city.delete(0,END)
		add.delete(0,END)
		user_name.delete(0,END)
		password.delete(0,END)
		very_pass.delete(0,END)


	# start Signup Window	

	winsignup = Tk()
	winsignup.title("doctor Appointment App")
	winsignup.maxsize(width=500 ,  height=600)
	winsignup.minsize(width=500 ,  height=600)


	#heading label
	heading = Label(winsignup , text = "Signup" , font = 'cambri 30 bold',fg='blue')
	heading.place(x=80 , y=60)

	
	# form data label
	first_name = Label(winsignup, text= "First Name :" , font='cambri 12 bold')
	first_name.place(x=73,y=130)

	last_name = Label(winsignup, text= "Last Name :" , font='cambri 12 bold')
	last_name.place(x=73,y=160)

	age = Label(winsignup, text= "Age :" , font='cambri 12 bold')
	age.place(x=125,y=190)

	Gender = Label(winsignup, text= "Gender :" , font='cambri 12 bold')
	Gender.place(x=99,y=220)

	city = Label(winsignup, text= "City :" , font='cambri 12 bold')
	city.place(x=127,y=260)

	add = Label(winsignup, text= "Address :" , font='cambri 12 bold')
	add.place(x=93,y=290)

	user_name = Label(winsignup, text= "User Name :" , font='cambri 12 bold')
	user_name.place(x=73,y=320)

	password = Label(winsignup, text= "Password :" , font='cambri 12 bold')
	password.place(x=80,y=350)

	very_pass = Label(winsignup, text= "Verify \n Password:" , font='cambri 12 bold')
	very_pass.place(x=80,y=380)

	heading.config(bg='#ff00ff')
	first_name.config(bg='#ff00ff')
	last_name.config(bg='#ff00ff')
	age.config(bg='#ff00ff')
	Gender.config(bg='#ff00ff')
	very_pass.config(bg='#ff00ff')
	password.config(bg='#ff00ff')
	city.config(bg='#ff00ff')
	add.config(bg='#ff00ff')
	user_name.config(bg='#ff00ff')

	# Entry Box ------------------------------------------------------------------

	first_name = StringVar()
	last_name = StringVar()
	age = IntVar(winsignup, value='0')
	var= StringVar()
	city= StringVar()
	add = StringVar()
	 
	user_name = StringVar()
	
	password = StringVar()
	
	very_pass = StringVar()


	

	first_name = Entry(winsignup, width=40 , textvariable = first_name)
	first_name.place(x=200 , y=133)


	
	last_name = Entry(winsignup, width=40 , textvariable = last_name)
	last_name.place(x=200 , y=163)

	
	age = Entry(winsignup, width=40, textvariable=age)
	age.place(x=200 , y=193)

	
	Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
	Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 238)
    
	city = Entry(winsignup, width=40,textvariable = city)
	city.place(x=200 , y=263)


	
	add = Entry(winsignup, width=40 , textvariable = add)
	add.place(x=200 , y=293)

	
	user_name = Entry(winsignup, width=40,textvariable = user_name)
	user_name.place(x=200 , y=323)

	
	password = Entry(winsignup, width=40, textvariable = password)
	password.place(x=200 , y=353)

	
	very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
	very_pass.place(x=200 , y=395)


	# button login and clear

	btn_signup = Button(winsignup, text = "Signup" ,font='cambria 12 bold', command = action)
	btn_signup.place(x=210, y=439)


	btn_login = Button(winsignup, text = "Clear" ,font='cambria 12 bold' , command = clear)
	btn_login.place(x=290, y=439)


	sign_up_btn = Button(winsignup , text="Switch To Login",font='cambria 12 bold' , command = switch )
	sign_up_btn.place(x=350 , y =20)

	


	winsignup.config(bg='#ff00ff')
	winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------	


	

#------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()





# app title
win.title("Doctor Appointment App")

# window size
win.maxsize(width=600 ,  height=500)
win.minsize(width=600 ,  height=500)


#heading label
heading = Label(win , text = "Login" , font = 'cambria 50 bold',bg="#ff3300",fg='gold')
heading.place(x=210 , y=80)

username = Label(win, text= "User Name :" , font='cambria  15 bold',bg="#ff3300")
username.place(x=80,y=204)

userpass = Label(win, text= "Password :" , font='cambria 15 bold',bg="#ff3300")
userpass.place(x=90,y=254)



# Entry Box
user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=210)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)


# button login and clear

btn_login = Button(win, text = "Login" ,font='cambria 12 bold',command = login)
btn_login.place(x=215, y=299)


btn_login = Button(win, text = "Clear" ,font='cambria 12 bold', command = clear)
btn_login.place(x=287, y=299)

# signup button

sign_up_btn = Button(win , text="Switch To Sign up" ,font='cambria 9 bold', command = signup )
sign_up_btn.place(x=459 , y =20)



win.config(bg="#ff3300")
win.mainloop()

#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------