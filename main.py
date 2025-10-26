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

#--------------Больница-----------
class Hospital:
    def __init__(self, name : str , addres : str , chief_medical : str , mail : str,doctor_dict: dict, patient_dict: dict):
        self.name = name
        self.addres = addres
        self.chief_medical = chief_medical
        self.mail = mail
        self.doctor = doctor_dict     
        self.patient = patient_dict 

    def watch_patient(self):
        print("Список пациентов:")
        for name, number in self.patient.items():
            print(f"ФИО: {name} - ID: {number}")

    def add_patient(self):
        polis = Generate.get_polis()
        name_patient = input("Введите ФИО: ").capitalize().strip()
        self.patient[name_patient] = polis
        print(f"Пациент '{name_patient}' создан! (Полис: {polis})")
    
    def watch_doctor(self):
        print("\nСписок врачей:")
        for spec, doctors in self.doctor.items():
            print(f"\nСпециальность : {spec}")
            for name in doctors.keys():
                print(f" - {name} ")

    def add_doctor(self):
        print("Добавление нового врача: ")
        specialty = input("Введите специальность врача: ").capitalize().strip()
        name = input("Введите ФИО врача: ").strip()
        new_id = Generate.get_code()

        # если специальности нет — создаём новую
        if specialty not in self.doctor:
            self.doctor[specialty] = {}

        self.doctor[specialty][name] = new_id
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
        for name, number in self.patient.items():
            print(f"ФИО: {name} - ID: {number}")

        object = input("\nВведите ID пациента: ")

        for name, number in self.patient.items():
            if number == object:
                print(f"Вы выбрали пациента: {name} (ID: {number})")
                return name, number

        print("Пациент не найден. Повторите попытку снова")
        return self.choose_patient()   # исправлено: раньше было self.choose_patient(self)

    def show_hocpital(self):#выведи инфу про поликлинику
        print(f"\nНазвание: {self.name}\nАдрес: {self.addres}\nГлавный врач: {self.chief_medical}\nПочта: {self.mail}")
        return True
#--------------Пациент-----------
class Patient:
    def __init__(self,hospital : Hospital):
        self.name = hospital.choose_patient[0]
        self.polis = hospital.choose_patient[1]
    
    #если попросит показать - покажем 
    def show_medical_card(self, medical_card : dict):
        print(f"Медицинская карта пациента {self.name} :")
        Medical_card.show_medical_card(self.polis)
    
        

    #пойти на прием - сравнить с записью и вписать направление или диагноз
    def go_to_an_appointment(self):
        ...
    
    def sign_up(self):
        ...

    def base_patient(self):
        print("База пациентов:")
        for polis, data in Patient.info_patient.items():
            print(f"{polis} : {data}")
#--------------Медицинская карта----------
class Medical_card:
    medical_cards = {
        '0125': {
            'ФИО' : 'Волков Александр Петрович', 
            'Пол': 'мужской', 
            'Дата рождения':'01.01.1988',
            'Номер телефона' : '+7-987-456-01-02',
            'Диагноз' : {
                'Диагноз1' : 'Гастрит',
            }
        },
        '3223': {
            'ФИО' : 'Соколова Мария Игоревна', 
            'Пол': 'женский', 
            'Дата рождения':'27.03.2005',
            'Номер телефона' : '+7-285-111-86-00',
            'Диагноз' : {
                'Диагноз1' : 'Перелом ноги',
            }
        },
        '7777' : {
            'ФИО' : 'Хомин Николай Сергеевич',
            'Пол' : 'мужской',
            'Дата' : '04.04.2004',
            'Номер телефона' : '+7-444-400-00-78',
            'Диагноз' : {
                'Диагноз1' : 'Гастрит'
            }
        },
    }
    def __init__(self, number, gender , age, diagnosis , patient : Patient):
        self.polis = patient.polis
        self.name = patient.name
        self.gender = gender
        self.age = age
        self.number = number
        self.diagnosis = diagnosis

    def create_medical_card(self,medical_cards):#name-id
        for k in self.medical_cards.keys():
            if self.polis==k:
                print("Медицинская карта уже существует!:)")
                return 
            else: 
                gender=input("Введите пол: (женский/мужской): ")
                data = input("Введите дату рождения (02.04.2000): ")
                phone = input("Введите номер телефона (+7-777-777-70-70): ")
                diagnos = {}
                medical_cards[self.polis] = {
                    'ФИО' : self.name,
                    'Пол' : gender,
                    'Дата' : data,
                    'Номер телефона' : phone,
                    'Диагноз' : diagnos,
                }

    def add_diagnosis(self, patient : Patient ,diagnos : Diagnosis,medical_cards : dict):
        self.all_keys = []
        self.polis = patient.polis
        self.name = diagnos.name
        self.comment = diagnos.comment
        for k in medical_cards.keys():
            self.all_keys.append(k)
        if self.name in self.all_keys:
            print("Поименяйте название диагноза! ")
        else:
            medical_cards[self.polis][self.name] = self.comment
            print("Диагноз записан в медкижку ")
        return


    def show_medical_card(self, polis: str, medical_cards: dict):
        if polis not in medical_cards:
            print(f"Карта с полисом {polis} не найдена.")
            return

        card = medical_cards[polis]
        print(f"\nМедицинская карта пациента (полис {polis}):")
        for key, value in card.items():
            if isinstance(value, dict):  
                print(f"  {key}:")
                for sub_key, sub_value in value.items():
                    print(f"    {sub_key}: {sub_value}")
        else:
            print(f"  {key}: {value}")

    def to_dict(self):
        return {
          'Полис': self.polis,
          'ФИО' : self.name,
          'Пол': self.gender,
          'Возраст': self.age,
          'Телефон' : self.number,
          'Диагноз' : self.diagnosis

        }

#-------------Создание объектов----------------
if __name__ == "main":
    pass