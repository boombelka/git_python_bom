# Классы территорий
class Territory(object):
    # проходимость местности и изменяемость при катаклизмах
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


class Mountin(Territory):
    def __init__(self, patency= 1, mutability= 0):
        Territory.__init__(self, patency, mutability)
        self.mutability = 1

    def __str__(self):
        return ('MMM')


class Field(Territory):
    def __init__(self, patency=1, mutability=1, terranian='Поле', godsend='Ничегошеньки'):
        Territory.__init__(self, patency, mutability)
        self.patency = 1
        self.mutability = 1
        self.terranian = terranian
        self.godsend = godsend

    def __str__(self):
        return('===')


class Forest(Territory):
    def __init__(self, patency=1, mutability=1, terranian='Лес', godsend='Ничегошеньки'):
        Territory.__init__(self, patency, mutability)
        self.patency = 1
        self.mutability = 1
        self.terranian = terranian
        self.godsend = godsend

    def __str__(self):
        return ('FFF')


class FieldCoin(Territory):
    def __init__(self, patency=1, mutability=1, terranian='Поле', godsend='Монета'):
        Territory.__init__(self, patency, mutability)
        self.patency = 1
        self.mutability = 1
        self.terranian = terranian
        self.godsend = godsend

    def __str__(self):
        return ('==O')


class FieldRubin(Territory):
    def __init__(self, patency=1, mutability=1, terranian='Поле', godsend='Рубин'):
        Territory.__init__(self, patency, mutability)
        self.patency = 1
        self.mutability = 1
        self.terranian = terranian
        self.godsend = godsend

    def __str__(self):
        return ('==R')

class FieldMigth(Territory):
    def __init__(self, patency=1, mutability=1, terranian='Поле', godsend='Меч'):
        Territory.__init__(self, patency, mutability)
        self.patency = 1
        self.mutability = 1
        self.terranian = terranian
        self.godsend = godsend

    def __str__(self):
        return ('==/')

# функция создания списка территорий для генерации карты
def complectteritory(list_territory):
    list_territory.append(Water())
    list_territory.append(Field())
    list_territory.append(Mountin())
    list_territory.append(Field())
    list_territory.append(FieldCoin())
    list_territory.append(FieldRubin())
    list_territory.append(FieldMigth())
    return list_territory