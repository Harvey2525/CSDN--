'''
自动存取款系统
1.数据源
2.查看余额信息
3.存款
4.取款
5.登录 退出系统
6.界面交互
'''
#1.数据源
import getpass


#一般下面这个数据是来自数据库接口 或者网络接口
User_Information =[
    {'name':'zhiyong','password':'11111','balance':500000,'account_status':True,'error_count':0},
    {'name':'zhangnan','password':'11111','balance':900,'account_status':True,'error_count':0},
    {'name':'Wupin','password':'11111','balance':886,'account_status':False,'error_count':0}]
#密码错误次数
Error_Count = 0
#账号认证
def Account_Verification (sName, sPassword):

    global User_Information
    for User_Id in range (len(User_Information)):
        #查询用户名是否存在
        if sName == User_Information[User_Id]['User_Name']:
            #检测密码是否正确
            if sPassword ==User_Information[User_Id]['Password']:
             #检查账户是否被锁定
                if User_Information[User_Id]['Account_Status']==True:
                    print('欢迎使用')
                    return User_Id
                else:
                    print('账号已被锁定！')
                    return -2
            else:
                err_count = User_Information[User_Id]['Error_Count']
                err_count +=1
               # if err_count >2:
                #    User_Information[User_Id]['Account_Status']=false
                print('密码错误，密码错误3次 您的账号将被锁定，您还有{}次机会'.format(3 - User_Information[User_Id]['Error_Count']))
                return -1
        #else:


#2.查看余额信息
def Account_Balance(User_Id):
    global User_Information
    print('您的余额为{}元！'.format(User_Information[User_Id]['balance']))

#3.存款
def deposit_Money(User_Id):
    global User_Information
    while True:
        money = input('请输入您的存款金额: ')
        if float(money)<=0:
            print("请输入大于0的金额！")
        else:
            User_Information[User_Id]['balance']+= int(money)
            print('您已存款{}元，余额为{}元'.format(money,User_Information[User_Id]['balance']))
            break #跳出循环 或者return

# 4.取款
def withdraw__Money(User_Id):
    global User_Information
    while True:
        money = input('请输入您的取款金额: ')
        if float(money)<=0:
            print("请输入大于0的金额！")
        elif float(money)>User_Information[User_Id]['balance']:
            print('你的余额不足')
        else:
            User_Information[User_Id]['balance']-= int(money)
            print('您已取款{}元，余额为{}元'.format(money,User_Information[User_Id]['balance']))
            break

#修改密码
def change_password(User_Id):
    global User_Information
    global Error_Count
    while True:
        if User_Information[User_Id]['Error_Count'] == 3:
            User_Information[User_Id]['Account_State'] = False
            print('账号已被锁定')
            break
        sPassword_Old = input ('请输入原密码（输入q取消):')
        if str(sPassword_Old) == 'q':
            break
        if str(sPassword_Old)!=User_Information[User_Id]['Password']:
            User_Information[User_Id]['Error_Count'] += 1
            print('密码错误！输错3次密码将被锁定！您还有{}次机会'.format(3-User_Information[User_Id]['Error_Count']))
            continue

        #3次修改密码机会
        for n in range(3):
            sPassword_New1 = input('请输入新密码：')
            sPassword_New2 = input('请再次输入新密码：')
            if sPassword_New1 != sPassword_New2:
                print('密码不一致!')
                print('密码不一致3次，修改密码将失败！目前错误次数{}.format(n+1)')
            User_Information[User_Id]['Password'] = str(sPassword_New2)
            print('密码修改成功!')
            break
        break

# 5 .exit 6.UI

while True:
    # 初始界面
    print('='*12,'自动存取款系统','='*12)
    #输入用户名密码并校验
    sUser_Name = input ('请输入用户名')
    sPass_word = getpass.getpass('请输入密码')
    User_Id = Account_Verification(sUser_Name,sPass_Word)
    if User_Id < 0:
        continue
    #功能选择界面
    while True:
        if User_Information[User_Id]['Account_State'] == False:
            print('账号已被锁定')
            break
        print('='*22,'请选择业务','='*22)
        print('{:1}{:13}{:15}'.format(' ','1.查看余额信息','2.存款'))
        print('{:1}{:13}{:15}'.format(' ', '3.取款', '4.修改密码'))
        print('{:1}{:13}'.format(' ','5.退出系统'))
        print('=' * 40)
        key = input ('请输入对应的选择: ')
    #根据输入值，执行操作
    if key=='1':
        print('='*12,'余额信息浏览','='*12)
        Account_Balance(User_Id)
        input('按回车继续')
    elif key=='2':
        print('=' * 12, '存款', '=' * 12)
        x = input ('请输入要存款的金额: ')
        deposit_Money(User_Id)
        input('按回车继续: ')
    elif key == '3':
        print('=' * 12, '取款', '=' * 12)
        withdraw_Money(User_Id)
        y = input('请输入要取款的金额: ')
        input('按回车继续: ')
    elif key == '4':
        print('=' * 12, '修改密码', '=' * 12)
        show_account_info()
        y = input('请输入新密码 ')
        show_account_info()
        input('按回车继续: ')
    elif key =='5':
        loginout()
        print('='*12,'再见','='*12)
        break
    else:
        print('=' * 12, '操作无效', '=' * 12)
