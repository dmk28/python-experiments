from os import remove
import random
import getpass
from numpy import delete
import passlib
from passlib.context import CryptContext
import json

users = {}


context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=10000
)

def userQuery():
    option = input("What would you like to do?" + 
            "<I> Insert an User" +
            "<S> Search an User" +
            "<D> Delete an User"
            "<L> List Users  " ).upper()
    while option=="I" or option == "S" or option == "D" or option == "L":
        match(option):
            case "I":
               return makeUser(users)
            case "S":
                return searchUser(users, key=input("Please type the username you wish to search. "))
            case "D":
                return excludeUser(users,key=input("Please type the username you wish to delete: "))
            case "L":
                return listUsers(users)






def makeUser(users):
    continueThis = 'Y' or 'Yes'
    
    while (continueThis == 'Y'):
     userIndex = random.randint(2,8)
     userName = str(input("Please input the username to create. "))
     userPassword = getpass.getpass("Input the user's password: ")
     userPassword = context.hash(userPassword)
     userLevel = int(input("Enter the user's level from 0-7."))
     users[(userIndex, [userName])] = [(input("Please write the user's full name: ").upper(), input("Please write the user's function: "), userPassword, userLevel )]
     lastLogin = input("Type the date of the user's last login")
     users[(userIndex, [userName])].append(lastLogin)
     continueAsk = str(input("Do you wish to continue? Y or N "))
     print(users)
     with open("sample.json", "w") as i:
         json.dump(users, i)
     continueThis = continueAsk   
    userQuery()

def searchUser(users,key):
    
    
    thisList = users.get(key)
    if thisList != None: 
        print("....Name: ", thisList[0])
        print("....Function: ", thisList[1])
    userQuery()
    # userList = filter(lambda userfilter: userfilter.haskey(key),users)
    # print(userList)

def excludeUser(users, key):

    deletionList = users.get(key)
    if deletionList != None:
         del users[key]
         print("User deleted")
    userQuery()


def listUsers(users):
    for key, value in users.items():
        print("... Entrada de Dados:")
        print("Login: ", key)
        print("Data: ", value)
    userQuery()

def passwordMatch(users, key):
    thisPassword = users.get(key)
    comparePassword = thisPassword[2]
    loginPW = getpass.getpass("Input password: ")
    context.verify(loginPW,comparePassword)