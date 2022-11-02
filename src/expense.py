from PyInquirer import prompt


def get_users():
    users = []
    with open("users.csv", 'r') as file:
        for line in file:
            users.append(line.split('\n')[0])
    return users

def users_and_stop():
    res = get_users()
    res.append("STOP")
    return res

amount_question = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    }
]
label_question = [
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]
spender_questions = [
    {
        "type": "list",
        "name": "spender",
        "choices": get_users(),
        "message": "Choose an existing user please"
    },
]
involved_questions = [
    
    {
        'type': 'list',
        'name': 'involvedPeople',
        'message': 'Who are the involved people ?',
        'choices': users_and_stop(),
    },


]

def write_expense(infos):
    with open("expense_report.csv", 'a') as outfile:
        outfile.write(f"{infos['amount']},{infos['label']},{infos['spender']},{infos['involvedPeople']}\n")


def new_expense(*args):

    infos = {}

    amount = prompt(amount_question)

    famount = float(amount['amount'])
    label = prompt(label_question)

    spender = prompt(spender_questions)

    involved = prompt(involved_questions)
    involvedPpl = []
    while involved['involvedPeople'] != "STOP":
        involvedPpl.append(involved['involvedPeople'])
        involved = prompt(involved_questions)
    

    amount['amount'] = round(famount / (len(involvedPpl) + 1), 2)
    infos.update(amount)
    infos.update(label)
    infos.update(spender)
    infos.update({'involvedPeople': involvedPpl})

    write_expense(infos)
    print("Expense Added !")
    return True


