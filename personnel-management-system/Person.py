import datetime

class PersonTypeError (TypeError):
    pass


class PersonValueError(ValueError):
    pass


class Person:
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        # str, str, tuple, str, str
        if not (isinstance(name, str) and sex in ("女", "男")):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError("Wrong date:", birthday)
        self._name = name
        self._sex = sex
        self._bir = birth
        self._id = ident
        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._bir

    def age(self):
        return datetime.date.today().year - self._bir.year

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another._id

    @classmethod
    def num(cls):
        return Person._num

    def __str__(self):
        return " ".join((self._id, self._name, self._sex, str(self._bir)))

    def details(self):
        return " ".join(("编号：" + self._id,
                         "姓名：" + self._name,
                         "性别：" + self._sex,
                         "出生日期：" + str(self._bir)))


class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_gen())
        self._dep = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def en_year(self):
        return self._enroll_date

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("No this course selected:", course_name)
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    def details(self):
        return " ".join((Person.details(self),
                         "入学日期：" + str(self._enroll_date),
                         "院系：" + self._dep,
                         "课程记录：" + str(self.scores())))

    def __str__(self):
        return self.details()


class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday, Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError("Wrong date:", entry_date)
        else:
            self._entry_date = datetime.date.today()
        self._salary = 1720
        self._dep = "未定"
        self._pos = "未定"

    def salary(self):
        return self._salary

    def entry_date(self):
        return self._entry_date

    def position(self):
        return self._pos

    def department(self):
        return self._dep

    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_position(self, position):
        self._pos = position

    def set_department(self, department):
        self._dep = department

    def details(self):
        return " ".join((Person.details(self),
                         "入职日期：" + str(self._entry_date),
                         "院系：" + self._dep,
                         "职位：" + self._pos,
                         "工资：" + str(self._salary)))

    def __str__(self):
        return self.details()
