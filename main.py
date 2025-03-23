import shelve

import shelve
import re

# Крок 1: Створення класу Conference
class Conference:
    def __init__(self, name, location, participants):
        if not name.strip():
            raise ValueError("Назва конференції не може бути порожньою")
        if not location.strip():
            raise ValueError("Місце проведення не може бути порожнім")
        if participants < 0:
            raise ValueError("Кількість учасників не може бути від'ємною")
        self.name = name
        self.location = location
        self.participants = participants
    
    def __str__(self):
        return f"Конференція: {self.name}, Локація: {self.location}, Учасників: {self.participants}"
    
    def add_participants(self, number):
        if number < 0:
            return "Кількість учасників не може бути від'ємною"
        self.participants += number
        return f"Кількість учасників оновлена: {self.participants}"
    
    def __add__(self, other):
        return Conference(self.name + " & " + other.name, self.location, self.participants + other.participants)

# Крок 4: Створення підкласів
class ScienceConference(Conference):
    def __init__(self, name, location, participants, topic):
        super().__init__(name, location, participants)
        if not topic.strip():
            raise ValueError("Тема конференції не може бути порожньою")
        self.topic = topic
    
    def __str__(self):
        return f"Наукова конференція: {self.name}, Тема: {self.topic}, Локація: {self.location}, Учасників: {self.participants}"
    
    def get_details(self):
        return f"Наукова конференція {self.name}, Тема: {self.topic}, Локація: {self.location}, Учасників: {self.participants}"

class BusinessConference(Conference):
    def __init__(self, name, location, participants, industry):
        super().__init__(name, location, participants)
        if not industry.strip():
            raise ValueError("Галузь не може бути порожньою")
        self.industry = industry
    
    def __str__(self):
        return f"Комерційна конференція: {self.name}, Галузь: {self.industry}, Локація: {self.location}, Учасників: {self.participants}"

    def get_details(self):
        return f"Комерційна конференція {self.name}, Галузь: {self.industry}, Локація: {self.location}, Учасників: {self.participants}"

class DevelopmentConference(Conference):
    def __init__(self, name, location, participants, focus_area):
        super().__init__(name, location, participants)
        if not focus_area.strip():
            raise ValueError("Сфера розвитку не може бути порожньою")
        self.focus_area = focus_area
    
    def __str__(self):
        return f"Конференція з розвитку: {self.name}, Сфера: {self.focus_area}, Локація: {self.location}, Учасників: {self.participants}"

    def get_details(self):
        return f"Конференція з розвитку {self.name}, Сфера: {self.focus_area}, Локація: {self.location}, Учасників: {self.participants}"

# Функція для перегляду списку всіх конференцій
def view_all_conferences():
    with shelve.open("conferences_db") as db:
        if not db:
            print("Записи відсутні в базі даних.")
            return False
        else:
            # Виводимо всі конференції з їх порядковими номерами
            print("\nСписок конференцій:")
            for idx, key in enumerate(db, 1):
                conference = db[key]
                print(f"{idx}. {conference.name}")
            return True

# Функція для перегляду деталей конференції за її номером
def view_conference_details(conference_number):
    with shelve.open("conferences_db") as db:
        if not db:
            print("Записи відсутні в базі даних.")
        else:
            conference_list = list(db.values())
            if 0 < conference_number <= len(conference_list):
                conference = conference_list[conference_number - 1]
                print("\nДеталі конференції:")
                print(conference.get_details())  # Викликаємо метод get_details
            else:
                print("Невірний номер конференції.")

# Функція для взаємодії з користувачем
def main():
    while True:
        print("\n1. Переглянути всі конференції")
        print("2. Додати конференцію")
        print("3. Вийти")
        choice = input("Оберіть опцію: ")
        is_not_empty = view_all_conferences()

        if choice == "1" :
            while True and is_not_empty: # Викликаємо функцію для перегляду списку конференцій
                try:
                    conference_number = int(input("\nВведіть номер конференції для перегляду деталей (0 для повернення): "))
                    if conference_number == 0:
                        break
                    view_conference_details(conference_number)  # Викликаємо функцію для перегляду деталей конференції
                except ValueError:
                    print("Будь ласка, введіть коректний номер.")
        elif choice == "2":
            while True: 
                print("\nОберіть тип конференції:")
                print("1. Наукова")
                print("2. Бізнесова")
                print("3. З розвитку")
    
                try:
                    conf_type = int(input("Введіть номер типу: "))
                    if conf_type > 3 or conf_type < 1:
                        print("Номер конференції повинен бути між 1 і 3.")
                    else:
                        break
                except ValueError:
                    print("Будь ласка, введіть число.")


            while True:
                name = input("Введіть назву конференції: ").strip()
                if name:
                    break
                print("Назва конференції не може бути порожньою.")
        
            while True:
                location = input("Введіть місце проведення: ").strip()
                if location and re.match("^[A-Za-zА-Яа-яІіЄєЇїҐґ\s]+$", location):
                    break
                print("Місце проведення не може бути порожнім і повинно містити тільки букви та пробіли.")

            
            while True:
                try:
                    participants = int(input("Введіть кількість учасників: "))
                    if participants <= 0:
                        print("Кількість учасників не може бути від'ємною або дорівнювати нулю.")
                        continue
                    break
                except ValueError:
                    print("Будь ласка, введіть коректне число.")
            
            if conf_type == 1:
                while True:
                    topic = input("Введіть тему наукової конференції: ").strip()
                    if topic:
                        break
                    print("Тема конференції не може бути порожньою.")
                conference = ScienceConference(name, location, participants, topic)
            elif conf_type == 2:
                while True:
                    industry = input("Введіть галузь бізнесової конференції: ").strip()
                    if industry:
                        break
                    print("Галузь не може бути порожньою.")
                conference = BusinessConference(name, location, participants, industry)
            elif conf_type == 3:
                while True:
                    focus_area = input("Введіть сферу розвитку конференції: ").strip()
                    if focus_area:
                        break
                    print("Сфера розвитку не може бути порожньою.")
                conference = DevelopmentConference(name, location, participants, focus_area)
            else:
                print("Некоректний вибір типу конференції!")
                continue
            
            with shelve.open("conferences_db") as db:
                db[name] = conference
            print("Конференція успішно додана!")
        elif choice == "3":
            print("Вихід...")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()