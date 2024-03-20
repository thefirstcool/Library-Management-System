count=0
stats_1 = '已借出'
stats_2 = '未借出'
num=0
a = open('bookname', 'r', encoding='UTF-8')
line_1=a.readline()
for line_1 in a:
    num += 1


def check():
    name = input('请问你需要查找的书籍为:')
    a = open('bookname', 'r', encoding='UTF-8')
    line_1 = a.readline()
    for line_1 in a:
        line_1 = line_1.strip()
        if name == line_1:
            print(f"{name}存在")
            state(name)
            break
        elif name != line_1:
            global count
            count += 1
            if count == num:
                print('当前书库中不存在所查询书籍。')
                break



def state(name):
    stats_3 = name + stats_1
    stats_4 = name + stats_2
    b = open('bookstate', 'r', encoding='UTF-8')
    line_2 = b.readline()
    for line_2 in b:
        line_2 = line_2.strip()
        if line_2 == stats_3:
            print(f'{stats_3}')
            pass
        elif line_2 == stats_4:
            print(f'{stats_4}')







































