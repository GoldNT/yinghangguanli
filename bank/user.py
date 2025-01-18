class User:
    # 创建一个用户类，用来存放用户名，id ，手机号，银行卡号
    def __init__(self, name, id, phone, card):
        self.name = name
        self.id = id
        self.phone = phone
        self.card = card