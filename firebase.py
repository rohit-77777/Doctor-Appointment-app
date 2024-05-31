
#=======================FireBase Storage INput Data ===========================================#


# fire_url = 'https://the-day-before-default-rtdb.firebaseio.com/.json'


# fire_storage = str({f'\"{username.get()}\":{{"First Name":\"{first_name.get()}\","Last name":\"{last_name.get()}\","Age":\"{age.get()}\","Gender":\"{gender.get()}\","City":\"{city.get()}\","Address":\"{address.get()}\"}}'})



# fire_storage = fire_storage.replace(".","-")
# fire_storage = fire_storage.replace("\'","")
# to_database = json.loads(fire_storage)
# print((to_database))
# requests.patch(url = fire_url,json = to_database)


#==============================FireBase Get Data===============================================#


request  = requests.get(url)
data = request.json()
