import json
#--------------Больница-----------
class Hospital:
def __init__(self, name : str , addres : str , chief_medical : str , mail : str,patient_dict : dict):
    self.name = name
    self.addres = addres
    self.chief_medical = chief_medical
    self.mail = mail
    self.patient_dict = patient_dict # ИФО - id
  
def hocpital_info(self):
  return f"Название: {self.name}\nАдрес: {self.addres}\nГлавный врач: {self.chief_medical}\nПочта: {self.mail}"
  
def withdrawal_of_patients(self,patient_dict : dict):#вывод инфы о пациентах
  count = 0
  for key in self.patient_dict.keys():
    count+=1
    return (f"{count} - {key}")
    
def to_dict(self):
    return {
      'Название' : self.name,
      'Адресс': self.addres,
      'Главный врач': self.chief_medical,
      'Mail.ru': self.mail,
    }

#--------------Пациент-----------
class Patient:
    def __init__(self, id : int , name : str, gender : str , age : str):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        
    def checking_the_attachment(patient_dict: dict, value) -> bool:#проверка прикрепления
        return value in patient_dict.values()
        
    def to_dict(self):
        return {
          'ID': self.id,
          'ФИО' : self.name,
          'Пол': self.gender,
          'Возраст': self.age,
        }
#--------------Прикрепление-----------
class Attachment:


    
