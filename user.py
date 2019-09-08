# Классы Юзеров
class UserIter(object):
    def __init__(self):
        pass


class User(object):
    def __init__(self, nic='', name=''):
        self.nic = nic
        self.name = name

    def input_data(self):
        self.nic = input(f'Введите свой nic')
        self.name = input(f'Введите своt имя')

    def __str__(self):
        print(f'NIC: {self.nic},Имя: {self.name}')