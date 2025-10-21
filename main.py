import json
import random

class Generator_ID:
    def get_id():
        pass

class Polis(Generator_ID):
    _lst_ids = []
    def get_id():
        while (id := random.randint(10 ** 3, 10 ** 4 - 1)) not in Polis._lst_ids:
            return id


#--------------Пациент-----------
class Patient:
    def __init__(self, name : str, gender : str , age : str):
        self.name = name
        self.gender = gender
        self.age = age
        
    def to_dict(self):
        return {
          'ID': self.id,
          'ФИО' : self.name,
          'Пол': self.gender,
          'Возраст': self.age,
        }
    
#--------------Больница-----------
class Hospital:
    def __init__(self, name : str , addres : str , chief_medical : str , mail : str, patient_dict : dict[Patient, Polis]):
        self.name = name
        self.addres = addres
        self.chief_medical = chief_medical
        self.mail = mail
        self.patient_dict = patient_dict # ИФО - id
    
    def hocpital_info(self):
        return f"Название: {self.name}\nАдрес: {self.addres}\nГлавный врач: {self.chief_medical}\nПочта: {self.mail}"
    
    def withdrawal_of_patients(self):#вывод инфы о пациентах
        count = 0
        for key in self.patient_dict.keys():
            count+=1
            print (f"{count} - {key}")
        
    def to_dict(self):
        return {
        'Название' : self.name,
        'Адресс': self.addres,
        'Главный врач': self.chief_medical,
        'Mail.ru': self.mail,
        }
    
hospital1 = Hospital("Bolnica", "addres0", "afasf", "ilyaer@dgf", {Patient("sdg", "m", 18) : Polis.get_id(),
                                                                   Patient("sdgd", "m", 19) : Polis.get_id(),
                                                                   Patient("sdget", "m", 20) : Polis.get_id()})
    
#--------------Прикрепление----------- пациент - прикрепление(агрегация)
class Attachment:
    def __init__(self, date, status, patient: Patient):
        self.date = date 
        self.status = status
        self.patient = patient 
        
    def checking_the_attachment(self, patient_dict: dict, value : str):#проверка прикрепления
        if value in patient_dict.values():
            print('Пациент прикреплен')
            return True
        else:
            patient_dict[self.patient] = Polis.get_id()



    '''
                new_id = ''.join(random.choice('0123456789') for _ in range(4))
            
            # Если передан объект пациента, обновляем его ID
            if patient_info and hasattr(patient_info, 'id'):
                patient_info.id = new_id
                print(f'Сгенерирован новый ID для пациента: {new_id}')
            
            # Добавляем в словарь patient_dict
            patient_dict[patient_name] = new_id
            print(f'Пациент {patient_name} прикреплен с ID: {new_id}')
            return False
    '''
            
    def to_dict(self):
        return {
          'ID': self.date,
          'Статус' : self.status,
        }