"""Создать класс Student: id, Фамилия, Имя,  Отчество, Дата рождения, Адрес, Телефон, Факультет, Курс, Группа.
Функции-члены реализуют запись и считывание полей (проверка корректности),
расчет возраста студента
Создать список объектов.
Вывести:
a) список студентов заданного факультета;
d) список учебной группы.

"""


class Student:
    def __init__(self,  idS, SurnameS, NameStudentS, PatronymicS, BirthdayS, AdresS, NameFacultet, TelefonS, KursS, NumberGroup):
        self.__id = idS
        self.__SurSt = SurnameS
        self.__NameSt = NameStudentS
        self.__PatrSt = PatronymicS
        self.__BirtSt = BirthdayS
        self.__AdrSt = AdresS
        self.__TelSt = TelefonS
        self.__NameF = NameFacultet
        self.__KursSt = KursS
        self.__NumberGr = NumberGroup

    def get_id(self):
        return self.__id

    def setID(self, newId):
        if isinstance(newId, str):
            self.__Id = newId
        elif (newId <= 0):
            print("Id не может быть меньше 0 и ровняться нулю.")
        else:
            print("Неподходящий параметр!")

    def get_Surname(self):
        return self.__SurSt

    def set_Surname(self, newSur):
        if isinstance(newSur, str):
            self.__SurSt = newSur
        else:
            print("Неподходящий параметр!")

    def get_NameStudent(self):
        return self.__NameSt

    def set_NameStudent(self, NameStud):
        if isinstance(NameStud, str):
            self.__NameSt = NameStud
        else:
            print("Неподходящий параметр!")

    def get_Patronymic(self):
        return self.__PatrSt

    def set_Patronymic(self, PatrStus):
        if isinstance(PatrStus, str):
            self.__PatrSt = PatrStus
        else:
            print("Неподходящий параметр!")

    def get_Birthday(self):
        return self.__BirtSt

    def set_Birthday(self, BirthdayStud):
        if (BirthdayStud>= 1995 and BirthdayStud<=2010):
            self.__PatrSt = BirthdayStud
        else:
            print("Неподходящий параметр!")

    def get_Adres(self):
        return self.__AdrSt

    def set_Adres(self, AdresStud):
        if isinstance(AdresStud, str):
            self.__AdrSt = AdresStud
        else:
            print("Неподходящий параметр!")

    def get_Telefon(self):
        return self.__TelSt

    def set_Telefon(self, TelefonStud):
        if isinstance(TelefonStud, str):
            self.__TelSt = TelefonStud
        else:
            print("Неподходящий параметр!")

    def get_Kurs(self):
        return self.__KursSt

    def set_Kurs(self, KursStud):
        if (KursStud > 0 and KursStud < 5):
            self.__KursSt = KursStud
        else:
            print("Неподходящий параметр!")

    def get_Facultet(self):
        return self.__NameF

    def set_Facultet(self, FacultetStud):
        if isinstance(FacultetStud, str):
            self.__NameF = FacultetStud
        else:
            print("Неподходящий параметр!")

    def get_Group(self):
        return self.__NumberGr

    def set_Group(self, GroupStud):
        if isinstance(GroupStud, str):
            self.__NumberGr = GroupStud
        else:
            print("Неподходящий параметр!")


NameFacultet = input("Введите название факультета: \n")
NumberGroup = input("Введите номер группы: \n")


Students = []

Students.append(Student(1,'Иванов', 'Петр','Иванович',2004,'Минск','+375441234567',4,'ПОИТ','Т123'))
Students.append(Student(2,'Петров', 'Давид','Львович',2005,'Лида','+375441256732',4,'Экономика','Т124'))
Students.append(Student(3,'Орлова', 'Диана','Ивановна',2005,'Минск','+37544435267',4,'Право','Т123'))
Students.append(Student(4,'Демидов', 'Сергей','Петрович',2002,'Пинск','+37544112367',4,'ПОИТ','Т123'))

for item in Students:
    if (item.get_Facultet() == NameFacultet):
        print(item)


        ##  еще доделаю))