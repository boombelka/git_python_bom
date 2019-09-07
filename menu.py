


'''
class Service():
    def __init__(self):
        pass
    def save_user(self):
        pass
    def fill_user(self):
        User.fill(self)
class error:
    def __init__(self):
        self.errorCode="server issue"
        self.errorMessage="201"
class BaseRespone():
    def __init__(self):
        self.success = "data fetch successfully"
        self.data={"succss":"msg"}
        self.error1 = error()
def obj_to_dict(obj):
   return obj.__dict__


# Сохранение и загрузка.
bs = User()
json_string = json.dumps(bs.__dict__,  default = obj_to_dict, indent=4)
with open('data.txt', 'w') as f:
    f.write(json_string)
print(json_string)
with open("data.txt", "r") as f:
    data_again = json.load(f)
    f.close()
#json_string1 = json.loads(json_string)
print(data_again)
print(data_again['rers'])

'''
