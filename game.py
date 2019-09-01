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
    def __init__ (self, nic, name, password):
        self.nic = nic is str
        self.name = name is str
        self.password = password


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
    def __init__(self, shield= 0, impassability= 0):
        Territory.__init__(shield, impassability, lot= None, person= None)
        self.impassability = 1

    def __str__(self):
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
def complect_teritory()
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

# отрисовка карты
#
def global_map(map):
    for i in range(0, 10):
        print('---|---|---|---|---|---|---|---|---|---|')
        print(f'{map[i]}|{map[i + 1]}|{map[i + 2]}|{map[i + 3]}|{map[i + 4]}|{map[i + 5]}|{map[i + 6]}|{map[i + 7]}|{map[i + 8]}|{map[i + 9]}')
    print('---|---|---|---|---|---|---|---|---|---|')



#palyers = []
#gameover = False
#while gameover is not False:
#    menu()
while True
# Создаем список территорий, из которых будет составлена карта

    #map = []
    complect_teritory()
    map = generation_territory(title)
    global_map(map)


#print(sos)




# Сохранение нерабочее
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