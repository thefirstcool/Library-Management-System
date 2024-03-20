count = 0
stats_1 = '已借出'
stats_2 = '未借出'
num = 0
a = open('bookname', 'r', encoding='UTF-8')
line_1 = a.readline()
for line_1 in a:
    num += 1


def showallbook():
    print('-----------图书库-----------')
    b = open('bookstate', 'r', encoding='UTF-8')
    for line in b:
        print(line.strip())
    print(f'目前一共拥有图书{num}本')