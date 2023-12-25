
HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрпашивается у пользователя)
show - напечатать все добавленные задачи."""

today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Сегодня")
        print(today)
        print("Завтра")
        print(tomorrow)
        print("Другое")
        print(other)
    elif command == "add":
        task = input("Введите название задачи: ")
        data = input("Введите дату: ")
        if data == "сегодня":
            today.append(task)
        elif data == "завтра":
            tomorrow.append(task)
        else: 
            other.append(task)
        print(f"Задача {task} добавлена.")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
    else:
        print("Неизвестная команда")
        break
print("До свидания!")

# print(data, today)
# print(data, tomorrow)
# print(data, other)fdg