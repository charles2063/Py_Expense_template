from PyInquirer import prompt
import json

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def write_user(infos):
    with open("users.csv", 'a') as outfile:
        outfile.write(f"{infos['name']}\n")

def add_user():
    infos = prompt(user_questions)
    write_user(infos)
    # This function should create a new user, asking for its name
    print("User Added !")
    return