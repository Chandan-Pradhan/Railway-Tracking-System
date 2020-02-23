#RAILWAY TRACKING SYSTEM

import tkinter as tk
import requests

root = tk.Tk()

#=========================================HEADING=====================================

root.title('Railway Tracking System')
root.geometry('1420x780+50+6')

api_key = '78rgdx4n19'

date2 = ''
u_dest = ''

# https://api.railwayapi.com/v2/between/source/<stn code>/dest/<stn code>/date/<dd-mm-yyyy>/apikey/<apikey>/

#===============================================METHODS=================================================

#FUNCTION TO GET THE REQUIRED INFORMATION USING THE RAILWAY API


def get_values(source, destination, date, month, year):
    global date2
    global u_dest
    u_dest = destination
    date1 = date + "-" + month + "-" + year
    date2 = date1
    base_url = 'https://api.railwayapi.com/v2/between/source/'
    complete_url = base_url + source + "/dest/" + destination + "/date/" + date1 + "/apikey/" + api_key + "/"
    response = requests.get(complete_url)
    result = response.json()
    show_result(result)


#FUNCTION TO DISPLAY THE LIST OF TRAINS


def show_result(result):
    if result['response_code'] == 200:
        b = ""
        q = ""
        for x in range(0, result['total']):
            a = result['trains'][x]['name']
            c = result['trains'][x]['number']
            b = b + a + " " + "-" + c + ' \n'
        label4["text"] = b
    else:
        print('There was some problem retrieving the information \n'
              '1.Please check you have entered \n the correct station codes')


#FUNCTION TO FIND OUT THE DISTANCE OF THE TRAIN FROM ITS DESTINATION


def show_result1(train_number):
    base_url = 'https://api.railwayapi.com/v2/live/train/'
    complete_url1 = base_url + train_number + "/station/" + u_dest + "/date/" + date2 + '/apikey/' + api_key + "/"
    response = requests.get(complete_url1)
    result1 = response.json()
    a = result1['position']
    b = result1['train']['name']
    c = result1['start_date']
    h = a + '\n' + b + '\n' + c
    label5['text'] = h


#============================CODE FOR THE USER INTERFACE=======================================


background_image = tk.PhotoImage(file='train.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)

frame1 = tk.Frame(root, bg='#13BFBF', bd=2, relief='groove')
frame1.place(relx=0, rely=0, relheight=0.1, relwidth=1)

label1 = tk.Label(frame1, bg='#13BFBF', text='Railway Tracking System', font=('arial', 32))
label1.place(relheight=1, relwidth=1)

label2 = tk.Label(root, text='Source', bg='#E4EDED', bd=2, relief='ridge', font=('arial', 12))
label2.place(relx=0.03, rely=0.15, relheight=0.04, relwidth=0.1)

label3 = tk.Label(root, text='Destination', bg='#E4EDED' , bd=2, relief='ridge', font=('arial', 12))
label3.place(relx=0.03, rely=0.2, relheight=0.04, relwidth=0.1)

entry1 = tk.Entry(root, bd=2, relief='sunken',  font=('arial', 12))
entry1.place(relx=0.14, rely=0.15, relheight=0.04, relwidth=0.15)

entry2 = tk.Entry(root, bd=2, relief='sunken',  font=('arial', 12))
entry2.place(relx=0.14, rely=0.2, relheight=0.04, relwidth=0.15)

label5 = tk.Label(root, bg='#E4EDED',text='Date', font=('arial', 11))
label5.place(relx=0.03, rely=0.258, relheight=0.04, relwidth=0.1)

entry3 = tk.Entry(root, bd=2, relief='sunken',  font=('arial', 12))
entry3.place(relx=0.14, rely=0.258, relheight=0.04, relwidth=0.025)

entry4 = tk.Entry(root, bd=2, relief='sunken',  font=('arial', 12))
entry4.place(relx=0.18, rely=0.258, relheight=0.04, relwidth=0.034)

entry5 = tk.Entry(root, bd=2, relief='sunken',  font=('arial', 12))
entry5.place(relx=0.23, rely=0.258, relheight=0.04, relwidth=0.059)

button1 = tk.Button(root, text='Submit', bg='#E4EDED', font=('arial', 11), bd=2, command=lambda: get_values(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get()))
button1.place(relx=0.3, rely=0.175, relheight=0.041, relwidth=0.055)

label4 = tk.Label(root, bg='#13BFBF', font=('arial', 12), bd=2, relief='groove')
label4.place(relx=0.03, rely=0.32, relheight=0.65, relwidth=0.26)

label2 = tk.Label(root, text='Train No -', bg='#E4EDED', bd=2, relief='ridge', font=('arial', 12))
label2.place(relx=0.5, rely=0.2, relheight=0.04, relwidth=0.1)

entry6 = tk.Entry(root, bd=2, relief='sunken',  font=('arial', 12))
entry6.place(relx=0.61, rely=0.2, relheight=0.04, relwidth=0.17)

label5 = tk.Label(root, bg='#13BFBF', bd=2, relief='ridge', font=('arial', 10))
label5.place(relx=0.61, rely=0.26, relheight=0.35, relwidth=0.35)

button2 = tk.Button(root, text='Submit', bg='#E4EDED', font=('arial', 11), bd=2, command=lambda: show_result1(entry6.get()))
button2.place(relx=0.79, rely=0.2, relheight=0.041, relwidth=0.055)


root.mainloop()