import json
import menu
import random as r

class inventory(object):
    def __init__(self, wegth= 0, size = 0, lvl= 0):
        self.wegth : int
        self.size: int
        self.lvl : int

class Migth(inventory):
    def __init__(self, wegth= 5, size= 3, lvl= 40 ):
        inventory.__init__(wegth, size, lvl)


class Alebard(inventory):
    def __init__(self, wegth= 7, size= 5, lvl= 50 ):
        inventory.__init__(wegth, size, lvl)


class Stick(inventory):
    def __init__(self, wegth= 3, size= 5, lvl= 50 ):
        inventory.__init__(wegth, size, lvl)


class Rubin(inventory):
    def __init__(self, wegth= 1, size= 1, lvl= 0 ):
        inventory.__init__(wegth, size, lvl)


class Coin(inventory):
    def __init__(self, wegth= 1, size= 1, lvl= 0 ):
        inventory.__init__(wegth, size, lvl)

class Creature(object):
    def __init__(self):
        self.po : int
        self.hp : int
        self.intelligence : int


class Mage(object):
    def __init__(self):
        pass

class Warrior(object):
    def __init__(self):
        pass

class Profile(object):
    def __init__ (self, nic, name, password, pers):
        self.nic = nic is str
        self.name = name is str
        self.password = password is str
        self.pers = object


class Territory:
    def __init__(self, shield= 0, impassability= 0, lot = None, person= None):
        self.impassability :int
        self.shield : int
        self.lot : object
        self.person : object

    def __str__(self):
        return(' X ')

class Water(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(shield, impassability)

    def __str__(self):
        return f' ~ '


class Field(Territory):
    def __init__(self, shield= 0, impassability= 1):
        Territory.__init__(shield, impassability, lot= None, person= None)
        self.impassability = 1

    def __str__(self):2
        return(f' = ')


class FieldCoin(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Coin()

    def __str__(self):
        return(f' =O')


class FieldRubin(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Rubin()

    def __str__(self):
        return(f' =*')


class FieldMight(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Migth()

    def __str__(self):
        return(f' =/')


class FieldStick(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Stick()

    def __str__(self):
        return(f' =!')


class FieldAlebarda(Territory):
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(shield, impassability, lot= None, person= None)
        self.impassability = 1
        self.lot = Alebard()

    def __str__(self):
        return(f' =(')

# собираем список всех типов территорий для генерации карты
def complect_teritory():
    title = []
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


def menu_personage():
    nicname = input('Напишите ваше логин')
    name = input('Введите ваш пароль')
    password = input('Введите ваш пароль')
    while True:
        hero = int(input('Кем вы хотите играть? 1 - Маг, 2 - Воин').lower())
        if hero == 1:
            print(f'Вы выбрали МАГА. Добро пожаловать в братство')
            pers = Mage
            break
        elif hero == 2:
            print(f'Вы выбрали ВОИНА. Добро пожаловать в гильдию Воинов')
            pers = Warrior()
            break
        else:
            print('Вы неправильно выбрали персонаж')
            continue
    user = Profile(nicname, name, password, pers)
    return(user)

def menu():
    while True:
        print(f'[1] - Заполнить профиль пользователя')
        print(f'[2] - Начать игру')
        print(f'[3] - Сохранить игру')
        print(f'[4] - Загрузить игру')
        print(f'[5] - Вернуться в игру')
        print(f'[6] - Выйти из игры')
        x = (int(input('Выберите действие').lower()))
        if 0 < x < 7:
            if x == 1:
                menu_personage()
            elif x == 2:
                pass
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

# отрисовка карты
# Не могу нормально добавить объекты lot и person - вернее не могу их запрашивать и делать с ними какие либо действия.
def global_map(map):
    for i in range(0, 10):
        print('---|---|---|---|---|---|---|---|---|---|')
        print(f'{map[i]}|{map[i + 1]}|{map[i + 2]}|{map[i + 3]}|{map[i + 4]}|{map[i + 5]}|{map[i + 6]}|{map[i + 7]}|{map[i + 8]}|{map[i + 9]}')
    print('---|---|---|---|---|---|---|---|---|---|')


def begin_name(user):
    print(f'В нелегкое время появились вы в этой дальней стране, {user}')


#palyers = []
#gameover = False
#while gameover is not False:
while True:
# Создаем список территорий, из которых будет составлена карта

    menu()
    #map = []
    complect_teritory()
    map = generation_territory(title)
    global_map(map)

# Сохранение нерабочее
# не видит lot, person при сохранении в словари объектов вложенных в объект map[]
#for i in range(0, 99):
#cl = map[1]
#cl_1 = map[1]
#result = json.dumps(cl.__dict__)
#print(result)

#with open('data.txt', 'w', encoding='UTF-8') as file:
 #   file.write(results)


if __name__ == "__main__":
    print('Запущена вручную')
else:
    ('Запущена автоматически')