"""Создать класс Student: id, Фамилия, Имя,  Отчество, Дата рождения, Адрес, Телефон, Факультет, Курс, Группа.
Функции-члены реализуют запись и считывание полей (проверка корректности),
расчет возраста студента
Создать список объектов.
Вывести:
a) список студентов заданного факультета;
d) список учебной группы.

"""


class Student:
    current_year = 2021
    idS = 0
    def __init__(self,  SurnameS = '', NameStudentS = '', BirthdayS = 2000, AdresS = '', NameFacultet = '', TelefonS = '', KursS = 1, NumberGroup= ''):

        self.nameS = SurnameS
        self.SurSt = NameStudentS
        self.Birt = BirthdayS
        self.Adr = AdresS
        self.Tel = TelefonS
        self.Facul = NameFacultet
        self.Kurs = KursS
        self.Group = NumberGroup
        self.group_dict = {}

    def display_info(self):
        print(f'id: {self.idS}'
            f'\nИмя: {self.nameS}'
            f'\nФамилия: {self.SurSt}'
            f'\nДата рождения: {self.Birt}'
            f'\nВозраст: {self.current_year - self.Birt}'
            f'\nАдрес: {self.Adr}'
            f'\nТелефон: {self.Tel}'
            f'\nФакультет: {self.Facul}'
            f'\nКурс: {self.Kurs}'
            f'\nГруппа: {self.Group}')

    def add_students(self):
        age = int(self.current_year) - int(self.Birt)
        #self.group_dict[self.i] = None
        self.group_dict[self.idS] = [self.nameS,self.SurSt, self.Birt, age, self.Adr, self.Tel, self.Facul, self.Kurs, self.Group]
        #print(self.group_dict)
        Student.idS += 1

    def print_facul(self, Facul):
        for key, value in self.group_dict.items():
            if Facul in value:
                print(f'\nID: {key}\
                \nИмя: {value[0]}\
                \nФамилия: {value[1]}\
                \nДата рождения: {value[2]}\
                \nВозраст: {value[3]}\
                \nАдрес: {value[4]}\
                \nТелефон: {value[5]}\
                \nФакультет: {value[6]}\
                \nКурс: {value[7]}\
                \nГруппа: {value[8]}')
                print('********************')

    def print_group(self, Group):
        for key, value in self.group_dict.items():
            if Group in value:
                print(f'\nID: {key}\
                \nИмя: {value[0]}\
                \nФамилия: {value[1]}\
                \nДата рождения: {value[2]}\
                \nВозраст: {value[3]}\
                \nАдрес: {value[4]}\
                \nТелефон: {value[5]}\
                \nФакультет: {value[6]}\
                \nКурс: {value[7]}\
                \nГруппа: {value[8]}')
                print('********************')


st = Student()

Kol = int(input('Сколько студентов добавить в список?\n'))
for i in range(Kol):
    print("Введите Имя: ")
    st.nameS = input()
    print("Введите Фамилию: ")
    st.SurSt = input()
    print("Введите год рождения: ")
    st.Birt = input()
    print("Введите адрес: ")
    st.Adr = input()
    print("Введите телефон: ")
    st.Tel = input()
    print("Введите факультет: ")
    st.Facul = input()
    print("Введите курс: ")
    st.Kurs= input()
    print("Введите группу: ")
    st.Group = input()
    st.add_students()


print('Вывод студентов по факулету')
st.print_facul(input('Введите факультет ->  '))

print('Вывод студентов по группе')
st.print_group(input('Введите номер группы ->  '))



