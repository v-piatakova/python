LOGIN_ADMIN = "admin"
PASSWORD_ADMIN = "admin"
PIZZES = {}
DRINKS = {}

MENU = [PIZZES, DRINKS, ]


def isAdmin(login, password):
    return login == LOGIN_ADMIN and password == PASSWORD_ADMIN


def auth():
    login = input("login: ")
    password = input("password: ")
    return {'login': login, 'password': password}


def getMenu():
    print('Our menu')
    f = open('pizza.txt')
    print(f.read())
    f.close()
    f = open('drink.txt')
    print(f.read())
    f.close()
    

def adminInterface():
    getMenu()
    while True:
        add = input('what you want to add? pizza/drink/snack/nothing\n')
        fileName = add
        if add == 'pizza':
            edit(PIZZES, fileName)
        elif add == 'drink':
            edit(DRINKS, fileName)
        elif add == 'nothing':
            break
        else:
            print('ERROR')
            raise ProcessLookupError


def edit(field, fileName):
    dish = input("new dish: ")
    cost = input("input cost: ")
    field[dish] = int(cost)
    f = open(fileName + '.txt', 'a')
    f.write('\n'+dish +' '+ cost)
    f.close()


def simpleUserInterface():
    count = 0
    getMenu()
    while True:
        order = input('What is your choise? ')
        if order in PIZZES: count += PIZZES[order]
        if order in DRINKS: count += DRINKS[order]
        

        order = input('Do you want order more? yes/no ')
        if order == 'yes':
            continue
        elif order == 'no':
            break
        else:
            print('ERROR')
            raise ProcessLookupError
    print('Your lunch cost: %d rubles' % count)
    return count


if __name__ == "__main__":
    userList = auth()
    if isAdmin(userList['login'], userList['password']):
        adminInterface()
    else:
        simpleUserInterface()

print('come again')