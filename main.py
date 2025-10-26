import random
import string

doctor_dict = {
    'Терапевт' : {
        'Тимошева Наталья Викторовна' : 'M001', # имя - информация
        'Сомов Павел Игоревич' : 'T002',
    },
    'Хирург' : {
        'Спасская Анна Валерьевна' : 'T001',
        'Марков Андрей Ильич' : 'X002',
    },
    'Стоматолог' : {
        'Власов Дмитрий Александрович' : 'K001',
        'Цыпуля Сергей Васильевич' : 'S002',
    }
    }
patient_dict = {
        'Волков Александр Петрович' : '0125',
        'Соколова Мария Игоревна' : '3223', 
        'Хомин Николай Сергеевич' : '7777'
    }

class Generate():
    _lst_polis = ['0125', '3223', '7777']
    _lst_ids = ['M001','T002','T001','X002','K001','S002']
    
    @staticmethod
    def get_polis():
        while True:
            polis = str(random.randint(1000, 9999))
            if polis not in Generate._lst_polis:
                Generate._lst_polis.append(polis)
                return polis

    @staticmethod
    def get_code():
        while True:
            code = random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=4))
            if code not in Generate._lst_ids:
                Generate._lst_ids.append(code)
                return code
            
#--------------Запись------------

#--------------Приём------------
#Проверка на запись 

class record:
    def __init__(self,doctor_name , ):
        ...    

#--------------Диагноз-------------
# сущетсвует только после приема 
class Diagnosis:
    def __init__(self , name : str , date_create : str , comment : str):
        self.name = name 
        self.date_create = date_create
        self.comment = comment
        self.medical = []

    #def write_medcard(self):
    #    return self.medical.append(self.name,self.date_create,self.comment)
    
    def to_dict(self):
        return {
          'Название диагноза': self.name,
          'Дата' : self.date_create,
          'Комментарий': self.comment,
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

    def add_diagnosis(self, diagnos : Diagnosis):
        self.name = diagnos.name
        self.date_create = diagnos.date_create
        self.comment = diagnos.comment

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

#--------------Пациент-----------
class Patient:
    def __init__(self, polis : int , name : str, gender : str , age : str):
        self.polis = polis
        self.name = name
        self.gender = gender
        self.age = age

    # Пациент - чел, у которого есть полис 
    #проверка наличия полиса

    def checking_policy(self, hospital : "Hospital"): 
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
            
    def show_medcard(self,):
        ...
            
    def to_dict(self):
        return {
          'Policy': self.polis,
          'ФИО' : self.name,
          'Пол': self.gender,
          'Возраст': self.age,
        }
#--------------Больница-----------
class Hospital:
    def __init__(self, name : str , addres : str , chief_medical : str , mail : str,doctor_dict: dict, patient_dict: dict):
        self.name = name
        self.addres = addres
        self.chief_medical = chief_medical
        self.mail = mail
        self.patient = doctor_dict
        self.doctor = patient_dict

    def watch_patient(self):
        print("Список пациентов:")
        for name, number in Hospital.patient.items():
            print(f"ФИО: {name} - ID: {number}")

    def add_patient(self):
        self.polic = Generate.get_polis()
        self.name = input("Введите ФИО: ").capitalize().strip()
        Hospital.patient[self.name] = self.polic
        print("Пациент создан! ")
    
    def watch_doctor(self):
        print("\nСписок врачей:")
        for spec, doctors in Hospital.doctor.items():
            print(f"\nСпециальность : {spec}")
            for name in doctors.keys():
                print(f" - {name} ")

    def add_doctor(self):
        print("Добавление нового врача: ")
        specialty = input("Введите специальность врача: ").capitalize().strip()
        name = input("Введите ФИО врача: ").strip()
        new_id = Generate.get_code()

        # если специальности нет — создаём новую
        if specialty not in Hospital.doctor:
            Hospital.doctor[specialty] = {}

        Hospital.doctor[specialty][name] = new_id
        print(f"Врач '{name}' ({specialty}) добавлен с ID {new_id}")

    def Work(self):#Нужно ли вам узнать о врачах или добавится в поликлинику
        print("Выберите что хотите сделать: \n")
        while True:
            if input("\nПросмотр существующих пациентов. Требуются права администратора! Введите код: ").strip().lower() == '1111':
                self.watch_patient()
                if input('\nНужно ли сделать еще что-то? (да/нет) : ').strip().lower()=='да':
                    continue
                else:
                    break 
            else:
                if input("\nДобавить пациента (да/нет): ").strip().lower() == 'да':
                    self.add_patient()
                    if input('\nНужно ли сделать еще что-то? (да/нет) : ').strip().lower()=='да':
                        continue
                    else:
                        break 
                else:
                    if input("\nПосмотреть список врачей (да/нет): ").strip().lower() == 'да':
                        self.watch_doctor()
                        if input('\nНужно ли сделать еще что-то? (да/нет) : ').strip().lower()=='да':
                            continue
                        else:
                            break 
                    else:
                        if input("\nДобавить врача : Требуются права администратора! Введите код: ").strip() == '1111':
                            self.add_doctor()
                            if input('\nНужно ли сделать еще что-то? (да/нет) : ').strip().lower()=='да':
                                continue
                            else:
                                break 
                        else:
                            print("\nВведен неверный запрос! Попробуйте снова.\n")
                            return self.Work()  

    #-------------------------------------
    def choose_patient(self):#выбор чела для работы
        print("Выбирете пациента из списка: ")
        print("Список пациентов:")
        for name, number in Hospital.patient.items():
            print(f"ФИО: {name} - ID: {number}")

        object = input("\nВведите ID пациента: ")

        for name, number in Hospital.patient.items():
            if number == object:
                print(f"Вы выбрали пациента: {name} (ID: {number})")
                return name, number

        print("Пациент не найден. Повторите попытку снова")
        self.choose_patient(self)
        return None

    def show_hocpital(self):#выведи инфу про поликлинику
        print(f"\nНазвание: {self.name}\nАдрес: {self.addres}\nГлавный врач: {self.chief_medical}\nПочта: {self.mail}")
        return True
    
    def to_dict(self):
        return {
        'Название' : self.name,
        'Адресс': self.addres,
        'Главный врач': self.chief_medical,
        'Mail.ru': self.mail,
        }
    
#-------------Создание объектов----------------
