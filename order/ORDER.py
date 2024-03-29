from colorama import Fore, Back, Style
from colorama import init
init()
print(Fore.BLACK)
print(Back.YELLOW)

LOGIN_ADMIN = "admin"
PASSWORD_ADMIN = "admin"
PIZZES = {}
DRINKS = {}
MENU = [PIZZES, DRINKS]

def auth():
    login = input("login")
    password = input("password")
    return {'login': login, 'password':password}

def Admin(login, password):
    return login == LOGIN_ADMIN and password == PASSWORD_ADMIN

def Menu():
    print(Back.GREEN)
    pizza= open('pizza.txt')
    print(pizza.read())
    pizza.close()
    drink= open('drink.txt')
    print(drink.read())
    drink.close()
   

def adminInterface():
    Menu()
    while True:
        print(Back.MAGENTA)
        print( "Your changes")

        f= input( '\nadd pizza\nadd drink\nadd nothing\n')
        fileName = f
        if f == 'pizza':
            Changes(PIZZES, fileName)
        elif f == 'drink':
            Changes(DRINKS, fileName)
        elif f == 'nothing':
            break
        else:
            break    


def Changes(tipe,file):
    dish = input("your dish: ")
    cost = input("it's cost: ")
    tipe[dish] = int(cost)
    f = open(file + '.txt', 'a')
    f.write('\n'+dish +' '+ cost)
    f.close()


def UserInterface():
    print(Back.CYAN)
    sum = 0
    Menu()
    while True:
        order = input('Please create your order ')
        if order in PIZZES: 
            sum += PIZZES[order]
        if order in DRINKS: 
            sum += DRINKS[order]
        else:
            break    

        order = input('something else?  yes/no')
        if order == 'yes':
            continue
        else:
            break

    print('To pay: %d ' % sum)
    return sum

if __name__ == "__main__":
    user = auth()
    if Admin(user['login'], user['password']):
        adminInterface()
    else:
        UserInterface()

input()
