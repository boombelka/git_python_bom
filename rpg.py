import json
import random
#from game import
# Классы персонажей

# Классы инвентаря

# Классы территорий
class Territory(object):
    # проходимость местности и изменяемость при катаклизамах
    def __init__(self, patency= 0,mutability =0):
        self.patency = patency
        self.mutability = mutability

    def __str__(self):
        return (f'XXX')


class Water(Territory):
    def __init__(self, patency= 0, mutability= 0):
        Territory.__init__(self, patency, mutability)
        self.mutability = 1

    def __str__(self):
        return ('~~~')


class Field(Territory):
    def __init__(self, patency=1, mutability=1):
        Territory.__init__(self, patency, mutability)
        self.patency = 1
        self.mutability = 1

    def __str__(self):
        return('===')


# Классы Юзеров
class UserIter(object):
    def __init__(self, user_list, start= 0):
        self.idx = start
        self.user_list =user_list

    def __next__(self):
        self.idx = self.idx - 1
        if self.idx - 1 >= len(self.user_list):
            return(self.user_list[self.idx - 1])
        raise StopIteration

class User(object):
    def __init__(self, user_list):
        self.user_list = user_list

    def __iter__(self):
        return


# Классы обслуживающие
class Menu(object):
    def __init__(self):
        pass

    def stand_menu(self, lusr):
        print(f'[1] - Заполнить профиль пользователя')
        print(f'[2] - Начать игру')
        print(f'[3] - Сохранить игру')
        print(f'[4] - Загрузить игру')
        print(f'[5] - Вернуться в игру')
        print(f'[6] - Выйти из игры')
        x = (int(input('Выберите действие').lower()))
        return(x)

    def data_user(self, lusr):
        print(f'Список имеющихся пользователей: {lusr}')
        real_user = input(f'Введите пожалуйста ваш ник.')
        if real_user is lusr:
            pass


    def load_data(self):
        with open("map_temple.txt", "r") as read_file:
            data = json.load(read_file)
        return(data)

    def save_date(self, massive, file_sv):

        with open(file_sv, 'w', encoding='utf-8') as f:
            json_string = json.dumps(massive)
            f.write(json_string)

    def return_to_game(self):
        pass

    def game_exit(self):
        pass

    def error(self):
        pass

def global_map(map):
    for i in range(0, 10):
        print('---|---|---|---|---|---|---|---|---|---|')
        print(f'{map[i]}|{map[i + 1]}|{map[i + 2]}|{map[i + 3]}|{map[i + 4]}|{map[i + 5]}|{map[i + 6]}|{map[i + 7]}|{map[i + 8]}|{map[i + 9]}')
    print('---|---|---|---|---|---|---|---|---|---|')

class Hero_coordinate(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def coord_x(self):
        return(self.x)

    def coord_y(self):
        return(self.y)

    def step(self):
        st = input('Куда вы пойдете w,s,a,d')
        if st == 'w':
            self.y = self.y + 1
        elif st == 's':
            self.y = self.y - 1

        elif st == 'a':
            self.x = self.x - 1

        elif st == 'd':
            self.x = self.x + 1


class GlobalMap(object):
    def __init__(self, w_map):
        self.w_map = w_map

    def paint(self):
        for i in range(0, 9):
            print(f'{self.w_map[0]} {self.w_map[1]} {self.w_map[2]} {self.w_map[3]} {self.w_map[4]} {self.w_map[5]} {self.w_map[6]} {self.w_map[7]} {self.w_map[8]} {self.w_map[9]}')


    def picture_map(self):

        for i in range(0 , 9):
            for j in range(0, 9):
                self.w_map[i][j] = random.choice([Field(patency=1, mutability=1), Water(patency=0, mutability=0)])
        return self.w_map

def complect_teritory(title):
    title.append(Water())
    title.append(Field())
    return title


if __name__ == '__main__':
    pass
    a = Hero_coordinate()
    #map = [[0 for x in range(10)] for y in range(10)]
    map11 = []
    title = []
    title = complect_teritory(title)

    d1 = []
    for j in range(10):
        d2 = []
        for i in range(10):
            item = random.choice(title)
            d2.append(item)
        d1.append(d2)


    for i in range(0,10):
        print(f'{d1[i][0]}{d1[i][1]}{d1[i][2]}{d1[i][3]}{d1[i][4]}{d1[i][5]}{d1[i][6]}{d1[i][7]}{d1[i][8]}{d1[i][9]}')

    Menu().save_date(d1, 'map_temp.json')






"""

while True:
    list_user = []
    #Menu
    ask = Menu().stand_menu(list_user)
    if ask == 1:
        Menu().data_user(list_user)
    elif ask == 2:
        pass
    elif ask == 3:
        Menu().save_date()
    elif ask == 4:
        world_map = Menu().load_data()
    elif ask == 5:
        global_map(map)
    elif ask == 6:
        os.exit

    print(world_map)
"""