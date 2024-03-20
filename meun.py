import show
import check
import borrow
import returnbook
import add
import delete



print('欢迎使用图书管理系统')
while True:
    print('以下是服务内容:')
    print('1.浏览书籍\t\t\t\t【输入1】')
    print('2.查询书籍\t\t\t\t【输入2】')
    print('3.借阅书籍\t\t\t\t【输入3】')
    print('4.归还书籍\t\t\t\t【输入4】')
    print('5.增加书籍\t\t\t\t【输入5】')
    print('6.删减书籍\t\t\t\t【输入6】')
    print('7.退出系统\t\t\t\t【输入7】')
    select = float(input('请选择你所需要的服务:'))
    if select == 1:
        show.showallbook()
        pass
    if select == 2:
        check.check()
        pass
    if select == 3:
        borrow.borrowbook()
        pass
    if select == 4:
        returnbook.returnbook()
        pass
    if select == 5:
        add.addbook()
        pass
    if select == 6:
        delete.delete()
        pass
    if select == 7:
        print('欢迎下次使用......')
        break
    else:
        print('请输入正确的选项')