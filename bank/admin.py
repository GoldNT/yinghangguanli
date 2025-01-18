

class Admin:
    """
    admin.py是整个项目的主页面，同时也是管理员登录的页面，在这里设置或配置管理员密码和账户
    此时管理员密码为000000
    管理员账户为000000
    """
    adminU = '000000'  # 管理员的账号
    adpwd = '000000'  # 管理员的密码


    # 这个是登录页面
    # 将登录页面封装为方法printAdminView
    # 操作页面封装为方法printsysFunctionView

    def printAdminView(self):#
        print("******************************************")
        print("***                                    ***")
        print("***         欢迎登录银行系统            ***")
        print("***                                    ***")
        print("******************************************")
    def printsysFunctionView(self):
        print("***********************************************")
        print("***                                         ***")
        print("***    1.开户(1)                2.查询(2)   ***")
        print("***    3.取款(3)                4.存款(4)   ***")
        print("***    5.转账(5)                6.锁定(6)   ***")
        print("***    7.解锁(7)                            ***")
        print("***                                         ***")
        print("***    退出(Q)                              ***")
        print("***                                         ***")
        print("***********************************************")

    def adminOption(self):
        adminInput = input("请输入管理员账户：")
        if self.adminU != adminInput:
            print("管理员账户输入错误......")
            return -1
        passwordInput = input("请输入密码：")
        if self.adpwd != passwordInput:
            print("输入密码有误......")
            return -1
        else:
            print("操作成功，请稍后......")
            return 0

