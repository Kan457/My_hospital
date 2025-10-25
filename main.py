import json
import random

Hospital_patient = [] # Список пациентов в больнице
class Generator_ID:
    def get_id():
        pass

class Polis(Generator_ID):
    _lst_ids = []
    def get_id():
        while (id := random.randint(10 ** 3, 10 ** 4 - 1)) not in Polis._lst_ids:
            return id


#--------------Пациент-----------
# Пациент - чел, у которого есть полис 
class Patient:
    def __init__(self, polic : int , name : str, gender : str , age : str):
        self.polic = polic
        self.name = name
        self.gender = gender
        self.age = age
        
    def checking_policy(self, polic : int , object : "Patient"):
        if polic=="":
            print("Полис отсутсвует! Нужно создать ?")
            request = input("Да/Нет")
            if request=="Да":
                #create_policy - создание полиса
                ...
            else:
                s = f"Объект {self.object} удален :(((( "
                del object
                return s
            
    def to_dict(self):
        return {
          'Policy': self.polic,
          'ФИО' : self.name,
          'Пол': self.gender,
          'Возраст': self.age,
        }
    
#--------------Больница-----------
class Hospital:
    def __init__(self, name : str , addres : str , chief_medical : str , mail : str, 
                 patient_dict : dict[Patient, Polis]):
        self.name = name
        self.addres = addres
        self.chief_medical = chief_medical
        self.mail = mail
        self.patient_dict = patient_dict # ИФО - id
    
    def hocpital_info(self):
        return f"Название: {self.name}\nАдрес: {self.addres}\nГлавный врач: {self.chief_medical}\nПочта: {self.mail}"
        
    def to_dict(self):
        return {
        'Название' : self.name,
        'Адресс': self.addres,
        'Главный врач': self.chief_medical,
        'Mail.ru': self.mail,
        }
    
#--------------------------------
    
hospital1 = Hospital("Bolnica", "addres0", "afasf", "ilyaer@dgf", {Patient("sdg", "m", 18) : Polis.get_id(),
                                                                   Patient("sdgd", "m", 19) : Polis.get_id(),
                                                                   Patient("sdget", "m", 20) : Polis.get_id()})
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
