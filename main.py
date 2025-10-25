import json
import random

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
    def __init__(self, polic : int , name : str, gender : str , age : str):
        self.polic = polic
        self.name = name
        self.gender = gender
        self.age = age

    # Пациент - чел, у которого есть полис 
    def checking_policy(self, hospital : "Hospital"): #проверка наличия полиса
        if self.polic is None:
            print("Полис отсутсвует! Нужно создать ?")
            request = input("Да/Нет")

            if request=="Да":
                self.polic = Polis.create_polic()
                hospital.add_patient(self.polic)
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
          'Policy': self.polic,
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
    
#-------------Создание объектов----------------
