#-*-coding:utf-8-*-


class NumberError(ValueError):
    pass


def ContentDict(): # 名称下标表
    dic = {}
    contents = open('content.dat', 'r', encoding='utf-8').readlines()
    for i in range(len(contents)):
        name = contents[i].split(' ')[0]
        dic.update({name: i})
    return dic

contentdict = ContentDict()


def AddContent(cont):  # 添加景点
    content = open("content.dat", "a", encoding="utf-8")
    content.write(cont + '\n')
    content.close()

    links = open("links.dat", "r", encoding="utf-8").readlines()
    links.append('\n')
    file = open("links.dat", "w", encoding="utf-8")
    file.writelines(links)
    file.close()


def EditContent(p, cont):  # 修改景点，cont为“圆明园 北京 历史文化”格式的字符串
    content = open("content.dat", "r", encoding="utf-8")
    con = content.readlines()
    con[p] = cont + '\n'
    content = open("content.dat", "w", encoding="utf-8")
    content.writelines(con)
    content.close()


def DelContent(p):  # 删除景点
    content = open("content.dat", "r", encoding="utf-8")
    con = content.readlines()
    del(con[p])
    content = open("content.dat", "w", encoding="utf-8")
    content.writelines(con)
    content.close()

    # 删除与景点链接的路线
    links = open("links.dat", "r", encoding="utf-8").readlines()
    if p < len(links):
        del(links[p])
    for i in range(len(links)):
        link = links[i].strip('\n').split(sep=' ')
        if link == ['']:
            continue
        k = 0
        while k < len(link):
            lin = link[k].split(sep=',')
            if lin[0] == str(p):
                del(link[k])
                continue
            elif int(lin[0]) > p:
                lin[0] = str(int(lin[0]) - 1)
                link[k] = ','.join(lin)
            k += 1
        links[i] = ' '.join(link) + '\n'
    file = open("links.dat", "w", encoding="utf-8")
    file.writelines(links)
    file.close()


def AELink(p, li):  # 添加或修改路线
    q = contentdict.get(li[0])
    li[0] = str(q)
    links = open("links.dat", "r", encoding="utf-8").readlines()
    link = links[p].strip('\n').split(sep=' ')
    for k in range(len(link)):
        lin = link[k].split(sep=',')
        if lin[0] == li[0]:
            link[k] = ','.join(li)
            links[p] = ' '.join(link) + '\n'
            file = open("links.dat", "w", encoding="utf-8")
            file.writelines(links)
            file.close()
            break
    else:
        link.append(','.join(li))
        link.pop(0)
        links[p] = ' '.join(link) + '\n'
        file = open("links.dat", "w", encoding="utf-8")
        file.writelines(links)
        file.close()


def DelLink(p, q):  # 删除路线
    links = open("links.dat", "r", encoding="utf-8").readlines()
    link = links[p].strip('\n').split(sep=' ')
    for k in range(len(link)):
        lin = link[k].split(sep=',')
        if lin[0] == str(q):
            del(link[k])
            links[p] = ' '.join(link) + '\n'
            file = open("links.dat", "w", encoding="utf-8")
            file.writelines(links)
            file.close()
            break
