import json
import random


#--------------Генерация полиса----------
class Generate():
    _lst_ids = []
    def get_polis():
        while (polis := random.randint(10 ** 3, 10 ** 4 - 1)) not in Generate._lst_ids:
            return polis

#--------------ПОЛИС-------------
class Polis:
    all_polis = []
    def __init__(self,data : str , status : str ):
        self.data = data
        self.status = status
        self.polic = Generate.get_polis()
    
    def show_polic(self):
        return self.polic

    def to_dict(self):
        return {
          'Дата создания полиса : ': self.data,
        }
#--------------Пациент-----------
class Patient:
    def __init__(self, polis : int , name : str, gender : str , age : str):
        self.polis = polis
        self.name = name
        self.gender = gender
        self.age = age

    # Пациент - чел, у которого есть полис 
    def checking_policy(self, hospital : "Hospital"): #проверка наличия полиса
        if self.polis is None:
            print("Полис отсутсвует! Нужно создать ?")
            request = input("Да/Нет")

            if request=="Да":
                self.polis = Polis.show_polic()
                hospital.add_patient(self.polis)
                return "Полис создан! Пациент добавлен"
            
            if request=="Нет":
                s = f"Объект {self.patient} удален :(((( "
                hospital.remove_patient(self.patient)
                return s
            
            else:
                print("Информация не распознана!")
                return self.checking_policy(hospital)

            
    def to_dict(self):
        return {
          'Policy': self.polis,
          'ФИО' : self.name,
          'Пол': self.gender,
          'Возраст': self.age,
        }
#--------------Больница-----------
class Hospital:
    def __init__(self, name : str , addres : str , chief_medical : str , mail : str):
        self.name = name
        self.addres = addres
        self.chief_medical = chief_medical
        self.mail = mail
        self.hospital_patient : list[Patient] = [] # Список пациентов в больнице

    def add_patient(self, patient : Patient):
            self.hospital_patient.append(patient)

    def remove_patient(self, patient : Patient):
            self.hospital_patient.remove(patient)

    def hocpital_info(self):
        return f"Название: {self.name}\nАдрес: {self.addres}\nГлавный врач: {self.chief_medical}\nПочта: {self.mail}"
        
    def to_dict(self):
        return {
        'Название' : self.name,
        'Адресс': self.addres,
        'Главный врач': self.chief_medical,
        'Mail.ru': self.mail,
        }
    
#--------------Медицинская карта----------
class Medical_card:
    def __init__(self,number , health_group , date_of_creation, diagnosis , patient : Patient):
        self.number = number
        self.health_group = health_group
        self.date_of_creation = date_of_creation
        self.diagnosis = diagnosis
        self.name = patient.name
        self.addres = patient.addres
        self.chief_medical = patient.chief_medical
        self.mail = patient.mail

    def show_info(self):
        return {
            'Полис' : self.name,
            'Адресс' : self.addres,
            'Главный врач' : self.chief_medical,
            'Mail.ru' : self.mail,
            'Полис': self.polic,
            'ФИО' : self.name,
            'Пол': self.gender,
            'Возраст': self.age,
        }
    def to_dict(self):
        return {
          'Полис': self.polic,
          'ФИО' : self.name,
          'Пол': self.gender,
          'Возраст': self.age,
        }
    
#-------------Создание объектов----------------
