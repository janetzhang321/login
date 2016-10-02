#! /usr/bin/python


#Janet Zhang
#Pd 6 SoftDev DW

import csv
import hashlib

myDict = {}

h = hashlib.sha512()

with open('data/userInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user = row['usr']
        pw = row['pw']
        myDict[user] = pw

def addUser () :
    return ""


def addUser (user,pw) :
    #check if user in dict
    if myDict.has_key(user):
        return "username exists!"
    #not in dict, so add
    else :
        #hash pass
        h.update(pw)
        myDict[user]=hashlib.sha512(pw).hexdigest()
        #add to file
        with open('data/userInfo.csv', 'w') as csvfile:
            fieldnames = ['usr', 'pw']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user in myDict: 
                writer.writerow({"usr": user, "pw": myDict[user]})
        return "account created!"
    
def login (user,pw) :
    for usr in myDict:
        if usr == user and hashlib.sha512(pw).hexdigest() == myDict[usr]:
            return "successfully logged in"
    
    return "login failed"


#addUser("a","a")
#addUser("a","a")
#addUser("c","b")


#print myDict