count=0
stats_1 = '已借出'
stats_2 = '未借出'
num=0
a = open('bookname', 'r', encoding='UTF-8')
line_1=a.readline()
for line_1 in a:
    num += 1


def addbook():
    a = open('bookname', 'a', encoding='UTF-8')
    b = open('bookstate', 'a', encoding='UTF-8')
    name = input('图书名字:')
    a.write(f'{name}\n')
    b.write(f'{name}未借出\n')
    a.flush()
    b.flush()
    print(f'图书《{name}》添加成功')
    global num
    num += 1