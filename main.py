import random

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список.
show - напечатать все добавленные задачи.
random - добавлять случайную задачу на дату "Сегодня". 
exit - выход из программы."""


RANDOM_TASKS = ["Повысить уровень знаний", "Подготовить резюме", "Написать сопроводительное письмо", "Откликнуться на вакансию"]

tasks = {

}

run = True

def add_todo(date, task):
    if date in tasks:
        # если дата есть в словаре
        # добавить в список задачу
        tasks[date].append(task)
    else:
        # если даты нет
        # создать запись с ключом date
        tasks[date] = []
        tasks[date].append(task)
    print("Задача", task, "добавлена на дату", date)

while run: 
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print("Такой даты нет")
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    elif command == "exit":
        print("Спасибо за использование!")
        break
    else:
        print("Неизвестная команда")
        break
print("До свидания!")

