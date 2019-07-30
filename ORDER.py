LOGIN_ADMIN = "admin"
PASSWORD_ADMIN = "admin"
PIZZES = {}
DRINKS = {}
MENU = [PIZZES, DRINKS]

def isAdmin(login, password):
    return login == LOGIN_ADMIN and password == PASSWORD_ADMIN


def auth():
    login = input("login")
    password = input("password")
    return {'login': login, 'password':password}


def getMenu():
    print('menu')
    h= open('pizza.txt')
    print(h.read())
    h.close()
    h = open('drink.txt')
    print(h.read())
    h.close()
   

def adminInterface():
    getMenu()
    while True:
        f= input('your changes: \nadd pizza\nadd drink\nadd NO\n')
        fileName = f
        if f == 'pizza':
            edit(PIZZES, fileName)
        elif f == 'drink':
            edit(DRINKS, fileName)
        elif f == 'no':
            break


def edit(field, fileName):
    dish = input("your dish: ")
    cost = input("it's cost: ")
    field[dish] = int(cost)
    f = open(fileName + '.txt', 'a')
    f.write('\n'+dish +' '+ cost)
    f.close()


def simpleUserInterface():
    check = 0
    getMenu()
    while True:
        g=input('Welcom to our restaurant!')
        order = input('Please create your order ')
        if order in PIZZES: check += PIZZES[order]
        if order in DRINKS: check += DRINKS[order]

        order = input('Thats all yes/1 more ')
        if order == '1 more':
            continue
        elif order == 'yes':
            break          
    print('To pay: %d ' % check)
    return check


if __name__ == "__main__":
    userList = auth()
    if isAdmin(userList['login'], userList['password']):
        adminInterface()
    else:
        simpleUserInterface()
