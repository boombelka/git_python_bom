class Human:
    hands = ('left', 'right')
    leg = 2
    head = 1
    body = 1
    heart = 1

    def __init__(self, name, surname, age=None):
        self.name = name
        self.surname = surname
        self.age = age or 0

    def move_head(self):
        print('head moved')

    def tell_name(self):
        print(f'My name {self.name}')


class HumanMars(Human):
    hands = ('left', 'right', 'center')
    super_power = 'FIRE'
    def __init__(self, name, surname, born_to, age=None):
        Human.__init__(self, name, surname, age)
        self.born_to = born_to



vasy = Human('Вася', 'Иванов', 22)
vasy.tell_name()
ilon = HumanMars('illon', 'Mask', 'mars', 40)

#ilon.tell_name()