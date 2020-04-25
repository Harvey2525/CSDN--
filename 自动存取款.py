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
a=1000
b=2000
c=3000
account_list =[
    {'name':'zhiyong','balance':a,'account':'Account001'},
    {'name':'zhiyong','balance':b,'account':'Account002'},
    {'name':'zhiyong','balance':c,'account':'Account003'}]


#2.查看余额信息
def show_account_info():
    if len(account_list)==0:
        print('='*20,'没有存款信息','='*20)
        return

    print('|{0:<6}|{1:<10}|{2:<10}|{3:<10}|'.format('userid','name','balance','account'))
    print('-'*40)
    for i, acc_dict in enumerate(account_list):
        print('|{0:<6}|{1:<10}|{2:<10}|{3:<10}|'.format(i+1,acc_dict['name'],acc_dict['balance'],acc_dict['account']))

# Test
# show_account_info()


#3.存款
x = 0
a = a + x

# 测试 3.存款
# show_account_info()


# 4.取款
y = 0
a = a - y

# test
# show_account_info()

# 5 .exit 6.UI

while True:
    # 初始界面
    print('='*12,'自动存取款系统','='*12)
    print('{:1}{:13}{:15}'.format(' ','1.查看余额信息','2.存款'))
    print('{:1}{:13}{:15}'.format(' ', '3.取款', '4.退出系统'))
    print('=' * 40)
    key = input ('请输入对应的选择: ')
    #根据输入值，执行操作
    if key=='1':
        print('='*12,'余额信息浏览','='*12)
        show_account_info()
        input('按回车继续')
    elif key=='2':
        print('=' * 12, '存款', '=' * 12)
        x = input ('请输入要存款的金额: ')
        show_account_info()
        input('按回车继续: ')
    elif key == '3':
        print('=' * 12, '删除学员信息', '=' * 12)
        show_account_info()
        y = input('请输入要取款的金额: ')
        show_account_info()
        input('按回车继续: ')
    elif key =='4':
        loginout()
        print('='*12,'再见','='*12)
        break
    else:
        print('=' * 12, '操作无效', '=' * 12)
