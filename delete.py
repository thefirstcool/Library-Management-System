count = 0
stats_1 = '已借出'
stats_2 = '未借出'
num = 0
num_1=0
a = open('bookname', 'r', encoding='UTF-8')
line_1 = a.readline()
for line_1 in a:
    num += 1
    num_1 += 1




def delete():
    name = input('请输入你说要删除的书籍:')
    stats_3 = name + stats_1
    stats_4 = name + stats_2
    a = open('bookname', 'r', encoding='UTF-8')
    line_1 = a.readline()
    b = open('bookstate', 'r', encoding='UTF-8')
    line_2 = b.readline()
    for line_1 in a:
        line_1 = line_1.strip()
        if name == line_1:
            with open('bookname', 'r', encoding='UTF-8') as f:
                content = f.read()
                new = content.replace(f'{line_1}\n', '')
                f.seek(0)
            with open('bookname', 'w', encoding='UTF-8') as f:
                f.write(f'{new}')
                f.truncate()
            for line_2 in b:
                line_2 = line_2.strip()
                if line_2 == stats_3 or line_2 == stats_4:
                    with open('bookstate', 'r', encoding='UTF-8') as f:
                        content = f.read()
                        new = content.replace(f'{line_2}\n', '')
                        f.seek(0)
                    with open('bookstate', 'w', encoding='UTF-8') as f:
                        f.write(f'{new}')
                        f.truncate()
                        global num_1
                        num_1-=1
                        print(f'删除成功,当前剩余图书{num_1}本')
                    break
                else:
                    pass
        elif name != line_1:
            global count
            count += 1
            if count == num:
                print('数据异常，请重试')
                break


