from libdw import pyrebase
import threading
import sklearn
import time
import datetime

projectid = "dwproject-c7e59"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyBYOWKbicvwI99CoO45Whm-XxgVaEm_aJI"
email = "cawin.chan@gmail.com"
password = "Eejlno0412"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
sensor_lst = [False,False,False]
time_on = [[],[],[]]
time_occupied = ['0:00:00','0:00:00','0:00:00']

def occupant_checker():
    ''' takes in current state of sensors and returns the string of the time occupied in HH:MM:SS'''
    while True:
        for i in range(len(db.child("ultrasonic").get(user['idToken']).val())):
            sensor_lst[i] = db.child("ultrasonic").child(str(i)).get(user['idToken'])
            # print(i,db.child("ultrasonic").get(user['idToken']).val(),sensor_lst[i].val())
            if sensor_lst[i].val() == True:
                time_on[i].append(db.child("time").get(user['idToken']).val())
                if len(time_on) >= 2:
                    time_occupied[i] = str(datetime.timedelta(seconds=time_on[i][-1] - time_on[i][0]))
                    db.child("time_occupied").set(time_occupied, user['idToken'])
                continue
            if sensor_lst[i].val() == False:
                time_on[i] = []
                time_occupied[i] = '0:00:00'
                db.child("time_occupied").set(time_occupied, user['idToken'])
                continue




y = threading.Thread(target=occupant_checker, args=())

y.start()






# root = db.child("/").get(user['idToken'])
# print(root.key(), root.val())
#
# age = db.child("age").get(user['idToken'])
# print(age.key(), age.val())
#
# facts = db.child("facts_about_me").get(user['idToken'])
# print(facts.key(), facts.val())
#
# facts = db.child("facts_about_me").child("1").get(user['idToken'])
# print(facts.val())
#
#
# name = db.child("name").get(user['idToken'])
# print(name.key(), name.val())
#
# # to create a new node with our own key
# db.child("pie").set(3.14, user['idToken'])
# # to update existing entry
# db.child("pie").set(3.1415, user['idToken'])
# db.child("love_dw").set(True, user['idToken'])