count = 0
stats_1 = '已借出'
stats_2 = '未借出'
num = 0
a = open('bookname', 'r', encoding='UTF-8')
line_1 = a.readline()
for line_1 in a:
    num += 1


def returnbook():
    name = input('归还图书名字:')
    stats_3 = name + stats_1
    stats_4 = name + stats_2
    a = open('bookname', 'r', encoding='UTF-8')
    line_1 = a.readline()
    b = open('bookstate', 'r', encoding='UTF-8')
    line_2 = b.readline()
    for line_1 in a:
        line_1 = line_1.strip()
        if name == line_1:
            for line_2 in b:
                line_2 = line_2.strip()
                reture(line_2, stats_3, name, stats_4)
        elif name != line_1:
            global count
            count += 1
            if count == num:
                print('当前书库中不存在所查询书籍。')
                break



def reture(line_2,stats_3,name,stats_4):
    if line_2 == stats_3:
        with open('bookstate', 'r', encoding='UTF-8') as f:
            content = f.read()
            new = content.replace(f'{name}已借出', f'{name}未借出')
            f.seek(0)
        with open('bookstate', 'w', encoding='UTF-8') as f:
            f.write(f'{new}')
            f.truncate()
            print(f'{name}归还成功')
        pass
    elif line_2 == stats_4:
        print('数据异常')
    else:
        pass

