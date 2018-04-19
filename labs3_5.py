users = {0: ["misha", "lol", "admin"]}
lenthusers = len(users)
filedatabase = "DataBase.txt"

def writedatabase():
    global users
    file = open(filedatabase, 'w')
    for i in range(lenthusers):
        file.write(str(i) + " " + users[i][0] + " " + users[i][1] + " " + users[i][2] + "\n")
    file.close()

def readdatabase():
    global lenthusers
    global users
    OpenFile = True
    try:
        file = open(filedatabase, 'r')
    except FileNotFoundError:
        OpenFile = False
    if OpenFile:
        file = open(filedatabase, 'r')
        for line in file:
            data = line
            data = data.split(' ')
            data[3] = data[3][0:-1]
            users[int(data[0])] = data[1:]
        lenthusers = len(users)
        file.close()
    else:
        writedatabase()
    return 
                               

def createusers(role = False):
    global users
    print("Регистрация:")
    reg = 1
    defroles = "user"
    global lenthusers
    while reg:
        login = input("Придумайте логин: ")
        if not login:
            print("Логин не может быть пустым!")
            login = input("Придумайте логин: ")
        reg = 0
        for i in range(lenthusers):
            if login == users[i][0]:
                print("Логин уже занят!")
                reg = 1
                break
    if len(login) != 0:             
        password = input("Введите пароль: ")
        f = 0
        while f == 0:
            if ' ' in password:
                print('Пароль содержить недопустимые символы')
                password = input("Введите пароль: ")
            else:
                f = 1;
        if not password:
            print("Пароль не может быть пустым!")
            password = input("Введите пароль: ")
        if len(password) != 0:
            users[lenthusers] = [login, password, defroles]
            lenthusers = len(users)
            writedatabase()
            print("Регистрация прошла успешно!")
            return

def changelogin(id):
    global users
    print("Смена логина:")
    f = 1
    while f:
        login = input("Придумайте новый логин: ")
        chan = 0
        for i in range(lenthusers):
            if login == users[i][0]:
                print("Логин уже занят!")
                f = 1
                break
    users[id][0] = login
    writedatabase()
    print("Изменение логина прошло успешно!")
    return

def changedpas(id):
    global users
    print("Изменение пароля:")
    fpas = 1
    while  fpas:
        password = input("Введите свой старый пароль: ")
        if password == users[id][1]:
            print("Ваш старый пароль введен верно!")
            users[id][1] = input("Придумайте новый пароль: ")
            f = 0
            while f == 0:
                if ' ' in users[id][1]:
                    print('Пароль содержить недопустимые символы')
                    users[id][1] = input("Введите пароль: ")
                else:
                    f = 1;
            fpas = 0
        else:
            print("Ваш старый пароль введен не правильно!")
            fpas = 1
    writedatabase()
    print("Изменение прошло успешно!")
    return

def resetpas():
    global users
    standardPassword = "qwerty1"
    print("Сброс пароля у пользователя:")
    fpas = 1
    while fpas:
        id = int(input("Введите id пользователя: "))
        if id >= lenthusers:
            print("Такого пользователя не существует!")
            print("Введите другой id!")
            fpas = 1
        else:
            users[id][1] = standardPassword
            print("Вы сбросили пароль у пользователя!("+users[id][0]+")")
            fpas = 0
    writedatabase()
    return

def changeroles():
    global users
    print("Изменение роли пользователя:")
    char = 1
    while char:
        id = int(input("Введите id пользователя: "))
        if id >= lenthusers:
            print("Такого пользователя не существует!")
            print("Введите другой id!")
            char = 1
        else:
            print("Выбирете роль:")
            print(" 1. Admin \n 2. User")
            pick = int(input("Выбирете роль: "))
            if pick == 1:
                defroles = "admin"
                users[id][2] = defroles
                print(users[id][0] + " стал " + users[id][2])
                break
            elif pick == 2:
                defroles = "user"
                users[id][2] = defroles
                print(users[id][0] + " стал " + users[id][2])
                break
    writedatabase()
    return

def changeselfroles(selfusersid):
    global users
    print('Изменение вашей текущей роли')
    char = 1
    id = selfusersid
    while char:
        print("Выбирете роль:")
        print(" 1. Admin \n 2. User")
        pick = int(input("Выбирете роль: "))
        if pick == 1:
            defroles = "admin"
            users[id][2] = defroles
            print(users[id][0] + " стал " + users[id][2])
            sigin()
            break
        elif pick == 2:
            defroles = "user"
            users[id][2] = defroles
            print(users[id][0] + " стал " + users[id][2])
            sigin()
            break
    writedatabase()
    return


def delusers(id):
    global users
    global lenthusers
    print("Удаление аккаунта: ")
    if users[id][2] == 'admin':
        print('Аккаунт админа удалять нельзя, если хотите удалить аккаунт, то нужно изменить роль на пользователя!')
        adminmod(id)
    elif users[id][2] != 'admin':
        while id + 1 < lenthusers:
            users[id][0] = users[id + 1][0]
            users[id][1] = users[id + 1][1]
            users[id][2] = users[id + 1][2]    
        users.pop(len(users) - 1)
        lenthusers = len(users)
        print("Вы успешно удалили аккаунт")
    writedatabase()
    mainmenu()
    return

def allusers():
    global users

    print("ID\t\tLogin\t\tPassword\t\tRole")
    for i in range(lenthusers):
        print(str(i)+"\t\t"+users[i][0]+"\t\t"+users[i][1]+"\t\t\t"+users[i][2])
    return

def adminmod(id):
    global users
    adminmod = 1
    usersid = id
    selfusersid = usersid
    print("Вы вошли как: "+ users[usersid][0] +"")
    print("Ваша роль: "+ users[usersid][2] +"")
    while adminmod:
        print(" 1. Cоздать пользователя \n 2. Изменить логин \n 3. Изменить пароль \n 4. Сбросить пароль у пользователя")
        print(" 5. Все пользователи \n 6. Изменить роль пользователя \n 7. Удалить аккаунт \n 8. Выйти из аккаунта ")
        print(" 9. Выход")
        change = int(input("Ваш выбор: "))
        if change == 1:
            createusers(True)
        elif change == 2:
            changelogin(usersid)
        elif change == 3:
            changedpas(usersid)
        elif change == 4:
            resetpas()
        elif change == 5:
            allusers()
        elif change == 6:
            print('Введите \n 1: Изменить чужую роль \n 2: Изменить свою роль')
            fc = int(input('Выберите пункт меню: '))
            if fc == 1:
                changeroles()
            if fc == 2:
                changeselfroles(selfusersid)
        elif change == 7:
            delusers(usersid)
        elif change == 8:
            adminmod = 0
        elif change == 9:
             exit(0)

def usersmod(id):
    global users
    usersmod = 1
    usersid = id
    print("Вы вошли как: "+users[usersid][0]+"")
    print("Ваша роль: "+users[usersid][2]+"")
    while usersmod:
        print(" 1. Изменить логин \n 2. Изменить пароль \n 3. Удалить аккаунт \n 4. Выйти из аккаунта")
        print(" 5. Выход")
        pick = int(input("Ваш выбор: "))
        if pick == 1:
            changelogin(usersid)
        elif pick == 2:
            changedpas(usersid)
        elif pick == 3:
            delusers(usersid)
        elif pick == 4:
            usersmod = 0
        elif pick == 5:
            exit(0)

def sigin():
    global users
    print("Вход в аккаунт:")
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    for i in range(lenthusers):
        if len(password) == 0:
            print('Ваш пароль не существует')
            mainmenu()
        if (login == users[i][0]) and (password == users[i][1]):
            print("Вы вошли в аккаунт!")
            if users[i][2] == "admin":
                adminmod(i)
            else:
                usersmod(i)
            return
    print("Вы ввели неправильный логин или пароль")
    return

def mainmenu():
    readdatabase()
    mainm = 1
    while mainm:
        print("Меню: ")
        print("1. Войти")
        print("2. Регистрация")
        print("3. Выход")
        p = int(input("Ваш выбор: "))
        if p == 1:
            sigin()
        elif p == 2:
            createusers()
        elif p == 3:
            exit(0)
    return

mainmenu()
