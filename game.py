import json
import menu
import random as r
load os

class inventory(object):
    def __init__(self, wegth= 0, size = 0, lvl= 0):
        self.wegth = wegth
        self.size = size
        self.lvl = lvl

class Migth(inventory):
    def __init__(self, wegth= 5, size= 3, lvl= 40 ):
        inventory.__init__(self, wegth, size, lvl)


class Alebard(inventory):
    def __init__(self, wegth= 7, size= 5, lvl= 50 ):
        inventory.__init__(self, wegth, size, lvl)


class Stick(inventory):
    def __init__(self, wegth= 3, size= 5, lvl= 50 ):
        inventory.__init__(self, wegth, size, lvl)


class Rubin(inventory):
    def __init__(self, wegth= 1, size= 1, lvl= 0 ):
        inventory.__init__(self, wegth, size, lvl)


class Coin(inventory):
    def __init__(self, wegth= 1, size= 1, lvl= 0 ):
        inventory.__init__(self, wegth, size, lvl)

class Creature(object):
    def __init__(self):
        self.po = po
        self.hp = hp
        self.intelligence = intelligence


class Mage(object):
    def __init__(self):
        pass

class Warrior(object):
    def __init__(self):
        pass


class ProfileData(object):
    def __init__(self, *args):
        pass


class Profile(object):
    def __init__ (self, nic, name, password, pers):
        self.nic = nic is str
        self.name = name is str
        self.password = password is str
        self.pers = object

    def __str__(self):
        print(f'Имя {self.name}')
        print(f'Имя {self.nic}')
        # добавить сюда шифрование
        print(f'Имя {self.password}')
        print(f'Имя {self.pers}')

    def error(self):
        err_nic = f'Нет такого ника'
        err_name = f'Нет такого имени'
        err_passw = f'Неверный пароль'
        err_pers = f'Нет такого персонажа'

class Territory:
    def __init__(self, shield= 0, impassability= 0, lot = None, person= None):
        self.impassability = impassability
        self.shield = shield
        self.lot = lot
        self.person = person

    def __str__(self):
        return(' X ')

class Water(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(self, shield, impassability)

    def __str__(self):
        return f' ~ '


class Field(Territory):
    def __init__(self, shield= 0, impassability= 1):
        Territory.__init__(self, shield, impassability, lot= None, person= None)
        self.impassability = 1

    def __str__(self):
        return(f' = ')


class FieldCoin(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(self, shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Coin()

    def __str__(self):
        return(f' =O')


class FieldRubin(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(self, shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Rubin()

    def __str__(self):
        return(f' =*')


class FieldMight(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(self, shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Migth()

    def __str__(self):
        return(f' =/')


class FieldStick(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(self, shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Stick()

    def __str__(self):
        return(f' =!')


class FieldAlebarda(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(self, shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Alebard()

    def __str__(self):
        return(f' =(')


class GameBoard(object):
    def __init__(self):
        pass
    def generator_gameboard(self):
        pass


class LoadData(object):
    def __init__(self):
        pass


# собираем список всех типов территорий для генерации карты
def complect_teritory(title):
    title.append(Water())
    title.append(Field())
    title.append(FieldAlebarda())
    title.append(FieldCoin())
    title.append(FieldMight())
    title.append(FieldRubin())
    title.append(FieldStick())
    return title

# генерация карты со всеми сокровищами
def generation_territory(list_territory):
    arr = []
    for i in range(1, 100):
        item = r.choice(list_territory)
        arr.append(item)
    return (arr)

def save_game():
    pass

'''
def menu_personage(user):
    user.nicname = input('Напишите ваш логин')
    user.name = input('Введите ваше имя')
    user.password = input('Введите ваш пароль')
    while True:
        hero = int(input('Кем вы хотите играть? 1 - Маг, 2 - Воин').lower())
        if hero == 1:
            print(f'Вы выбрали МАГА. Добро пожаловать в братство')
            user.pers = Mage
            break
        elif hero == 2:
            print(f'Вы выбрали ВОИНА. Добро пожаловать в гильдию Воинов')
            user.pers = Warrior()
            break
        else:
            print('Вы неправильно выбрали персонаж')
            continue
    print(f'Проверьте вашу учетную запись')
    print(user)
    return(user)

'''



def menu(user, title):
    i = True
    while i == True:
        print(f'[1] - Заполнить профиль пользователя')
        print(f'[2] - Начать игру')
        print(f'[3] - Сохранить игру')
        print(f'[4] - Загрузить игру')
        print(f'[5] - Вернуться в игру')
        print(f'[6] - Выйти из игры')
        x = (int(input('Выберите действие').lower()))
        if 0 < x < 7:
            if x == 1:
                menu_personage(user)
            elif x == 2:
                begin_game(user, title)
                i = False
                break
            elif x == 3:
                save_game()
            elif x == 4:
                load_game()
            elif x == 5:
                break
            else:
                exit_marker = input('Вы действительно хотите закончить игру ДА? (Да/Нет)').lower()
                if exit_marker == 'да':
                    print('До свидания, до скорых встреч')
                    os.exit()
                elif exit_marker == 'нет':
                    print('Мы рады, что вы передумали')
                else:
                    print('Вы неправильно ответили на вопрос - попробуйте еще.')
        else:
            print('Вы очень неправильно ответили на вопрос - попробуйте еще.')
    return(user, title)
# отрисовка карты
# Не могу нормально добавить объекты lot и person - вернее не могу их запрашивать и делать с ними какие либо действия.
def global_map(map):
    for i in range(0, 10):
        print('---|---|---|---|---|---|---|---|---|---|')
        print(f'{map[i]}|{map[i + 1]}|{map[i + 2]}|{map[i + 3]}|{map[i + 4]}|{map[i + 5]}|{map[i + 6]}|{map[i + 7]}|{map[i + 8]}|{map[i + 9]}')
    print('---|---|---|---|---|---|---|---|---|---|')

# Модуль отслеживания позиции на карте и хода игрока
def move_position():
    pass

# Модуль начала игры (генерит начальную карту)
def begin_game(user, title):
    print(f'В нелегкое время появились вы в этой дальней стране, {user}')
    title = complect_teritory(title)
    return title


class Menu(object):
    def __init__(self, x= 0):
        self.x = x
    def stand_menu(self):
        print(f'[1] - Заполнить профиль пользователя')
        print(f'[2] - Начать игру')
        print(f'[3] - Сохранить игру')
        print(f'[4] - Загрузить игру')
        print(f'[5] - Вернуться в игру')
        print(f'[6] - Выйти из игры')
        x = (int(input('Выберите действие').lower()))
        if x == 1:
            self.data_user()
        elif x == 2:
            pass
        elif x == 3:
            self.save()
        elif x == 4:
            self.load()
        elif x == 6:
            os.exit
        return(x)

    def data_user(self):

        input(f'Введите пожалуйста ваш ник')
        if
    def save(self):
        pass
    def load(self):
        pass
    def gameover(self):
        pass
    def error(self):
        print(f'Вы выбрали неуществующий пункт. Попробуйте еще раз')

#palyers = []
#gameover = False
#while gameover is not False:
# Начало игры
while True:
#    title = []
#    user = Profile
#    menu(user, title)
    # отрисовка карты из массива
#    map = generation_territory(title)
#    global_map(map)
    x = 0
    Menu(x).stand_menu()


# Сохранение нерабочее
# не видит lot, person при сохранении в словари объектов вложенных в объект map[]
#for i in range(0, 99):
#cl = map[1]
#cl_1 = map[1]
#result = json.dumps(cl.__dict__)
#print(result)

#with open('data.txt', 'w', encoding='UTF-8') as file:
 #   file.write(results)

'''
1511115111
1131113111
1111315111
1161111311
2221211111
1111222222
1164111311
1141171111
1113111311
1914118111

 '''


if __name__ == "__main__":
    print('Запущена вручную')
else:
    ('Запущена автоматически')


