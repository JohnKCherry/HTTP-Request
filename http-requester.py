#!/usr/bin/env python2.7

import requests
import time
import webbrowser


def post_request():
    print ("You Selected POST Request")
    site = raw_input("Insert domain with http  : ")
    cg = raw_input("Would you like to change user agent? (Y/N) ")
    if cg == ("Y") or cg == ("y"):
        insertua = raw_input("Insert User Agent : ")
        headers = {'user-agent' : insertua  } 
        r = requests.post( site , headers = headers , data = raw_input("Insert Data : "))
    elif cg ==("N") or cg == ("n") :    
        r = requests.post(site , data = raw_input("Insert Data : "))
    else:
        print("Wrong Option");
        post_request()
    print ("You requested a POST request on : ", r.url)
    print ("Status Code : ", r)
    print ("Request from the Server : ", r.request.headers)
    space()    
    print ("Server Reply : ", r.headers)
    print ("Website Text : ", r.text)
    open = raw_input("Would you like to open the webpage on Default Browser (Y/N) ")
    if open == ("Y") or open == ("y"):
        webbrowser.open(r.url, autoraise=True)

def get_request():
    print("You Selected GET Request")
    site = raw_input("Insert domain with http : ")
    cg = raw_input("Would you like to change user agent? (Y/N) ")
    if cg == ("Y") or cg == ("y"):
        insertua = raw_input("Insert User Agent : ")
        headers = {'user-agent' : insertua } 
        r = requests.get(site, headers = headers )            
    elif cg ==("N") or cg == ("n") : 
        r = requests.get(site)
    else:
        print("Wrong Option");
        get_request()
    print ("You requested a GET request on : ", r.url)
    print ("Status Code : ", r )
    print ("Request from the Server : ", r.request.headers)
    space()    
    print ("Server Reply : ", r.headers)
    print ("Website Text : ", r.text)
    open = raw_input("Would you like to open the webpage on Default Browser (Y/N) ")
    if open == ("Y") or open == ("y"):
        webbrowser.open(r.url, autoraise=True)

def put_request():
    print ("You Selected PUT Request")
    site = raw_input("Insert domain with http  : ")
    cg = raw_input("Would you like to change user agent? (Y/N) ")
    if cg == ("Y") or cg == ("y"):
        insertua = raw_input("Insert User Agent : ")
        headers = {'user-agent' : insertua } 
        r = requests.put(site, headers = headers, data = raw_input("Insert Data : " ))          
    elif cg ==("N") or cg == ("n") : 
        r = requests.put(site , data = raw_input("Insert Data : "))
    else:
        print("Wrong Option");
        put_request()
    print ("You requested a PUT request on : ", r.url)
    print ("Status Code : ", r)
    print ("Request from the Server : ", r.request.headers)
    space()    
    print ("Server Reply : ", r.headers)
    print ("Website Text : ", r.text)
    open = raw_input("Would you like to open the webpage on Default Browser (Y/N) ")
    if open == ("Y") or open == ("y"):
        webbrowser.open(r.url, autoraise=True)

def delete_request():
    print ("You Selected DELETE Request")
    site = raw_input("Insert domain with http  : ")
    cg = raw_input("Would you like to change user agent? (Y/N) ")
    if cg == ("Y") or cg == ("y"):
        insertua = raw_input("Insert User Agent : ")
        headers = {'user-agent' : insertua } 
        r = requests.delete(site, headers = headers)            
    elif cg ==("N") or cg == ("n") :
        r = requests.delete(site)
    else:
        print("Wrong Option");
        delete_request()
    print ("You requested a DELETE request on : ", r.url)
    print ("Status Code : ", r)
    print ("Request from the Server : ", r.request.headers)
    space()    
    print ("Server Reply : ", r.headers)
    print ("Website Text : ", r.text)
    open = raw_input("Would you like to open the webpage on Default Browser (Y/N) ")
    if open == ("Y") or open == ("y"):
        webbrowser.open(r.url, autoraise=True)

def head_request():
    print ("You Selected HEAD Request")
    site = raw_input("Insert domain with http  : ")
    cg = raw_input("Would you like to change user agent? (Y/N) ")
    if cg == ("Y") or cg == ("y"):
        insertua = raw_input("Insert User Agent : ")
        headers = {'user-agent' : insertua  } 
        r = requests.head(site, headers = headers )            
    elif cg ==("N") or cg == ("n") : 
        r = requests.head(site)
    else:
        print("Wrong Option");
        head_request()
    print ("You requested a HEAD request on : ", r.url)
    print ("Status Code : ", r)
    print ("Request from the Server : ", r.request.headers)
    space()    
    print ("Server Reply : ", r.headers)
    print ("Website Text : ", r.text)
    open = raw_input("Would you like to open the webpage on Default Browser (Y/N) ")
    if open == ("Y") or open == ("y"):
        webbrowser.open(r.url,autoraise=True)

def options_request():
    print ("You Selected OPTIONS Request")
    site = raw_input("Insert domain with http  : ")
    print ("You requested a OPTIONS request on : ", site)
    cg = raw_input("Would you like to change user agent? (Y/N) ")
    if cg == ("Y") or cg == ("y"):
        insertua = raw_input("Insert User Agent : ")
        headers = {'user-agent' : insertua  } 
        r = requests.options(site, headers = headers )            
    elif cg ==("N") or cg == ("n") : 
        r = requests.options(site)
    else:
        print("Wrong Option");
        options_request()
    print ("Status Code : ", r)
    print ("Request from the Server : ", r.request.headers)
    space()    
    print ("Server Reply : ", r.headers)
    print ("Website Text : ", r.text)
    open = raw_input("Would you like to open the webpage on Default Browser (Y/N) ")
    if open == ("Y") or open == ("y"):
        webbrowser.open(r.url, autoraise=True)

def sleep():
    time.sleep(0.2)

def space():
    print("\n")
    
def logo():
    print ("""
    
 _   _ _____ ___________  ______ _____ _____ _   _ _____ _____ _____ 
| | | |_   _|_   _| ___ \ | ___ \  ___|  _  | | | |  ___/  ___|_   _|
| |_| | | |   | | | |_/ / | |_/ / |__ | | | | | | | |__ \ `--.  | |  
|  _  | | |   | | |  __/  |    /|  __|| | | | | | |  __| `--. \ | |  
| | | | | |   | | | |     | |\ \| |___\ \/' / |_| | |___/\__/ / | |  
\_| |_/ \_/   \_/ \_|     \_| \_\____/ \_/\_\\___/\____/\____/  \_/  
                                                     By JohnKCherry                
""")

def menu():
    print ("1)POST     Request ")
    sleep()
    print ("2)GET      Request ")
    sleep()
    print ("3)PUT      Request ")
    sleep()
    print ("4)DELETE   Request ")
    sleep()
    print ("5)HEAD     Request ")
    sleep()
    print ("6)OPTIONS  Request ")
    sleep()
    print ("7)QUIT")

def options():
    select = raw_input("Select REQUEST type  : ")
    space()
    if (select == "1") or (select == "post"):
        post_request()
    elif (select == "2") or (select == "get"):
        get_request()
    elif (select == "3") or (select == "put"):
        put_request()
    elif (select == "4") or (select == "delete"):
        delete_request()
    elif (select == "5") or (select == "head"):
        head_request()
    elif (select == "6") or (select == "options"):
        options_request()
    elif (select == "7") or (select == "quit") :
        print ("GoodBye!!!")
        sleep()
        quit()
    else:
        print ("Wrong option select again :) ")
        menu()
        options()

logo()
space()
menu()
space()
options()
space()
