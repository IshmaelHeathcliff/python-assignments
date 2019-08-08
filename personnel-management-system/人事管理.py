# 不解决同名问题，修改名字后不能继续同一对象下修改，查询信息不支持单独一项信息的查询
# 程序结构未进行专门简化（精力不足=_=），重复的地方比较多
# 只能对一次运行中的数据进行操作，每次需重新输入数据，!设想!将输入数据保存进文本（=_=）
# 使用循环双链表原因：好不容易写出来了，不要浪费了（还要再写一个啊，好麻烦）
# 抽象数据类型描述：见书P56～57

from DLCL import DLCList
from Person import*


stuManage = DLCList()
staffManage = DLCList()

while True:
    inp1 = input("输入信息：1;查询信息：2;修改信息：3;其他键退出:")
    if inp1 == "q":
        break

    kin = input("教职工：0;学生：1:")
    if kin not in ("1", "0"):
        raise ValueError(kin)
    if kin == "0":
        exuList = staffManage
    else:
        exuList = stuManage

    if inp1 == "1":
        while True:
            name = input("名字：")
            sex = input("性别：")
            byear = int(input("生日年："))
            bmonth = int(input("生日月："))
            bday = int(input("生日天："))
            birth = (byear, bmonth, bday)
            if kin == "1":
                department = input("院系：")
                stuManage.append(Student(name, sex, birth, department))
            else:
                staffManage.append(Staff(name, sex, birth))

            con1 = input("添加成功，继续：1；返回：2:")
            if con1 == "1":
                pass
            elif con1 == "2":
                break
            else:
                raise ValueError("con1", con1)

    if inp1 == "2":
        while 1:
            searchElem = input("通过名字：1；通过id：2:")
            if searchElem == "1":
                name = input("请输入名字：")

                def search(p):
                    if p._name == name:
                        print(p)
                exuList.forEach(search)
            elif searchElem == "2":
                id = input("请输入id：")

                def search(p):
                    if p._id == id:
                        print(p)
                exuList.forEach(search)
            else:
                raise ValueError(searchElem)

            con2 = input("查询结束(若无结果则无匹配项)\n继续：1；返回：2:")
            if con2 == "1":
                pass
            elif con2 == "2":
                break
            else:
                raise ValueError("con2", con2)

    if inp1 == "3":
        while 1:
            name = input("修改对象名字：")
            while 1:
                if kin == "0":
                    edi = input("姓名：1；薪水：2；职位：3；院系：4:")
                    if edi == "2":
                        salary = int(input("请输入薪水："))

                        def edit(p):
                            if p._name == name:
                                p._salary = salary
                                print("修改预览：\n", p)
                        exuList.forEach(edit)
                    if edi == "3":
                        position = input("请输入职位：")

                        def edit(p):
                            if p._name == name:
                                p._pos = position
                                print("修改预览：\n", p)
                        exuList.forEach(edit)
                    if edi == "4":
                        department = input("请输入院系：")

                        def edit(p):
                            if p._name == name:
                                p._dep = department
                                print("修改预览：\n", p)
                        exuList.forEach(edit)

                if kin == "1":
                    edi = input("姓名：1；添加课程：2；添加分数：3:")
                    if edi == "2":
                        course = input("请输入课程：")

                        def edit(p):
                            if p._name == name:
                                p.set_course(course)
                                print("修改预览：\n", p)
                        exuList.forEach(edit)
                    if edi == "3":
                        course = input("请输入课程：")
                        score = input("请输入分数：")

                        def edit(p):
                            if p._name == name:
                                p.set_score(course, score)
                                print("修改预览：\n", p)
                        exuList.forEach(edit)

                if edi == "1":
                    nam = input("请输入新名字：")

                    def edit(p):
                        if p._name == name:
                            p._name = nam
                            print("修改预览：\n", p)
                    exuList.forEach(edit)

                con3 = input("修改成功，继续此姓名下：1；返回：2:")
                if con3 == "1":
                    pass
                elif con3 == "2":
                    break
                else:
                    raise ValueError("con3", con3)

            con4 = input("其他名字：1；返回：2:")
            if con4 == "1":
                pass
            elif con4 == "2":
                break
            else:
                raise ValueError("con4", con4)
