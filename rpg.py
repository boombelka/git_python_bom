import json
import random as r
import pickle
from user import User
import globalmap
#Классы персонажей

class GlobalMap(object):
    def __init__(self, map=[]):
        self.map = map

    def generate_new_map(self, map, title):
        self.map = map
        self.title = title

        for j in range(11):
            d2 = []
            for i in range(10):
                item = random.choice(complect_teritory())
                d2.append(item)
            self.map.append(d2)
            return (self.map)

    def print_map(self):
        for i in range(0, 10):
            print(f'{self.map[i][0]}{self.map[i][1]}{self.map[i][2]}{self.map[i][3]}{self.map[i][4]}{self.map[i][5]}{self.map[i][6]}{self.map[i][7]}{self.map[i][8]}{self.map[i][9]}')


# Классы обслуживающие
class Menu(object):
    def __init__(self):
        pass

    def stand_menu(self):
        print(f'[1] - Заполнить профиль пользователя')
        print(f'[2] - Начать игру')
        print(f'[3] - Сохранить игру')
        print(f'[4] - Загрузить игру')
        print(f'[5] - Вернуться в игру')
        print(f'[6] - Выйти из игры')
        x = (int(input('Выберите действие').lower()))
        return(x)

    def data_user(self, user):
        pass

    def load_data(self):
        with open("file_sv", "rb") as read_file:
            data = pickle.load(read_file)
        return(data)

    def save_date(self, massive, file_sv):

        with open(file_sv, 'wb') as f:
            pickle.dump(massive, f)
            #f.write(strin)

    def return_to_game(self):
        pass

    def game_exit(self):
        pass

    def error(self):
        pass

class Error(object):
    def __init__(self, questionce, answer_string_yes, yes_answer, no_answer, answer_string_no,  error_answer, if_answer=0):
        self.questionce = questionce
        self.answer_string_yes = answer_string_yes
        self.answer_string_no = answer_string_no
        self.yes_answer = yes_answer
        self.no_answer = no_answer
        self.error_answer = error_answer
# маркер разновидности проверки на ошибку ввода
# 0 - без выхода если нет
# 1 - выходом если нет
        self.if_answer = if_answer

    def processing_result(self):
        if self.if_answer == 0:
            query = input(f'{self.questionce}')
            if query == self.yes_answer:
                return(f'{self.answer_string_yes}')
            elif query == 'exit':
                os.exit()
            elif query == self.no_answer:
                return(f'{self.answer_string_no}')
            else:
                return (f'{self.error_answer}')


# Класс перемещения героя по карте
class HeroCoordinate(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def coord_x(self):
        return(self.x)

    def coord_y(self):
        return(self.y)

    def step(self):
        print('Управление:')
        print()
        st = input('Куда вы пойдете w,s,a,d')
        if st == 'w':
            self.y = self.y + 1
        elif st == 's':
            self.y = self.y - 1

        elif st == 'a':
            self.x = self.x - 1

        elif st == 'd':
            self.x = self.x + 1

# Классы инвентаря
class GameProccess(object):
    def __init__(self):
        pass

    def intro(self, curent_user):
        self.curent_user = curent_user
        print('Добро пожаловать в R.P.G')
        print('В нелегкое время встретились мы НЕЗНАКОМЕЦ')
        print('Как тебя зовут достойный представитель человечества?')
        self.curent_user.input_data()
        print(f'Итак. Добро пожаловать.')
        print(f'текущий статус {self.curent_user.__str__()}')
        print('***********************************************')
        print('Что делаем?')
        return ()

    def begin_game(self, map_new_gl):
        self.map_new_gl = map_new_gl
        map_new_gl = GlobalMap().generate_new_map(map_new)


    def interface(self, map):
        self.map = map
        print('******************************************************')
        print('        КАРТА                        ИНВЕНТАРЬ        ')
        print(' --------------    [{}]                               ')
        print(f' |{map[Hero_coordinate().coord_x()-1][Hero_coordinate().coord_y()+1]}|{map[Hero_coordinate().coord_x()][Hero_coordinate().coord_y()+1]}|{map[Hero_coordinate().coord_x()+1][Hero_coordinate().coord_y()+1]}                                                        ')
        print(f' |{map[Hero_coordinate().coord_x()-1][Hero_coordinate().coord_y()]}|{map[Hero_coordinate().coord_x()][Hero_coordinate().coord_y()]}|{[Hero_coordinate().coord_x()+1][Hero_coordinate().coord_y()]}                             ')
        print(f' |{map[Hero_coordinate().coord_x()-1][Hero_coordinate().coord_y()-1]}|{[Hero_coordinate().coord_x()-1][Hero_coordinate().coord_y()-1]}|{map[i][j]}                             ')
        print(f'                                                     ')
        print(f'   Управление w,s,a,d - ходьба                       ')
        print(f' *****************************************************')
if __name__ == '__main__':
    pass
curent_user = User()
GameProccess().intro(curent_user)
map_new = []
pilligrim = HeroCoordinate()
while True:
    user_new = User()
    ask = Menu().stand_menu()
    if ask == 1:
        user_new.input_data()
    elif ask == 2:
        GameProccess().begin_game(map_new)
    elif ask == 1:
        pass
    elif ask == 1:
        pass
    elif ask == 1:
        pass

    gameover = False

    while gameover == False:
        GameProccess.interface(map_new)
        pilligrim.step()
#       Hero_coordinate().step()
#       Hero_coordinate.coord_y()
#       Hero_coordinate.coord_x()



'''
    a = Hero_coordinate()
    #map = [[0 for x in range(10)] for y in range(10)]
    map11 = []
    title = []
    title = complect_teritory(title)
  
    h = []
    for i in range(0,100):
        for j in range(0, 10):
            for k in range(0, 10):
                h.append(d1[j][k])
    Menu().save_date(h, 'map_temp.txt')

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
'''