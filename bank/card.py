class Card:
    # 创建一个card类用来存放卡的id,银行卡的密码以及存入的卡的钱数
    def __init__(self,cardId,cardPwd,money):
        self.cardId = cardId
        self.cardPwd = cardPwd
        self.money = money
        self.cardLock = False