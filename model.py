def add_employee():
    with open('seminar8\\base.txt', 'r', encoding='utf-8') as database:
        data = database.read()
        index = data.count('\n')

    with open('seminar8\\base.txt', "a", encoding="utf-8") as database:
        id = str(index+1)
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        post = input("Введите должность: ")
        salary = input("Введите заработанную плату: ")
        data = id + ',' + surname + ',' + name + ',' + post + ',' + salary
        database.write(data + '\n')
        print("Сотрудник добавлен\n")


def delete_employee(index: int):
    index = int(index)
    with open('seminar8\\base.txt', 'r', encoding='utf-8') as database:
        data = database.read()
        if index > data.count('\n'): 
            return print('Неверный индекс, такого сотрудника нет\n')

   
    with open('seminar8\\base.txt', 'r', encoding='utf-8') as database:
        result = ''
        flag = 0
        for line in database:
            data = line.split(',')
            if data[0] == str(index): 
                flag = 1
                print ('Сотрудник удален\n')
            if flag > 0 :
                if flag == 1 : flag = 2 
                else : result += str(int(data[0]) - 1) + ',' + data[1] + ',' + data[2] + ',' + data[3] + ',' + data[4]
            else : result += line
            
    with open('seminar8\\base.txt', 'w', encoding='utf-8') as database:
        database.write(result)


def search_employee(surname):
    surname = input('\nВведите id, фамилию или имя сотрудника: ')
    with open('seminar8\\base.txt', 'r', encoding='utf-8') as database:
        for line in database:
            if surname in line:
                print('Фамилия \t\t Имя \t\t Должность \t\t Зарплата')
                print('\t\t\t'.join(line.split(',')))
                count += 1
    if count == 0:
        print('Сотрудников с такой фамилией нет!\n')


def update_employee(index: int):
    index = int(index)
    with open('seminar8\\base.txt', 'r', encoding='utf-8') as database:
        data = database.read()
        if index > data.count('\n'): 
            return print('Неверный индекс, такого сотрудника нет\n')

    with open('seminar8\\base.txt', 'r', encoding='utf-8') as database:
        new_data = ''
        for line in database:
            data = line.split(',')
            if data[0] == str(index):
                update = int(input("Какие данные хотите обновить?'\n' 1. Фамилия'\n' 2. Имя'\n' 3. Должность'\n'4. Зарплата"))
                if update == 1:
                    surname = input("Введите новую фамилию: ")
                    data[1] = surname
                elif update == 2:
                    name = input("Введите новое имя: ")
                    data[2] = name
                elif update == 3:
                    post = input("Введите новую должность: ")
                    data[3] = post
                elif update == 4:
                    salary = input("Введите новую зарплату: ")
                    data[4] = salary
                print("данные сотрудника обновлены\n")
        new_data += data[0] + data[1] + data[2] + data[3] + data[4]
    
    with open('seminar8\\base.txt', 'w', encoding='utf-8') as database:
        database.write(new_data)


def post_selection(post: str):
    count = 0
    result = ''
    with open('seminar8\\base.txt', 'r', encoding='utf-8') as database :
        for line in database:
            data = line.split(',')
            if post.lower() == data[3].lower():
                for i in range(len(data)) :
                    if i == 5 :
                        result += data[i]
                    else :
                        result += data[i] + " " 
                count += 1
    if count == 0: print('Сотрудников с такой должностью нет\n') 
    else :
        print("\nИндекс" + "," + "Фамилия" + "," + "Имя" + "," + "Должность" + "," + "Зарплата")
        print(result)

def salary_selection(level: int):
    level = int(level)
    if level < 0 or level > 15 : return print('Неверный код.\n')
    salary = level * 10000
    count = 0
    result = ''
    with open('seminar8\\base.txt', 'r', encoding='utf-8') as database :
        for line in database:
            data = line.split(',')
            if salary <= int(data[4]) <= (salary + 10000):
                for i in range(len(data)) :
                    if i == 5 :
                        result += data[i]
                    else :
                        result += data[i] + " " 
                count += 1
    if count == 0: print('Сотрудников с такой зарплатой нету\n') 
    else :
        print("\nИндекс" + "," + "Фамилия" + "," + "Имя" + "," + "Должность" + "," + "Зарплата")
        print(result)



def export_data_json():
    import json
    with open("seminar8\\employees.json", "w", encoding = 'utf-8') as w_file:
        with open('seminar8\\base.txt', 'r', encoding = 'utf-8') as database :
            for line in database:
                data = line.replace('\n', '').split(',')
                result = {"Индекс": data[0], "Фамилия": data[1], "Имя": data[2], "Должность": data[3], "Зарплата": data[4]}
                json.dump(result, w_file, indent = 4)
    print ('Экспорт выполнен\n')
    


def export_data_csv():
    import csv
    with open("seminar8\\employees.csv", "w", encoding = 'utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator= "\r")
        file_writer.writerow(["Индекс", "Фамилия", "Имя", "Должность", "Зарплата"])
        with open('seminar8\\base.txt', 'r', encoding = 'utf-8') as database :
            for line in database:
                data = line.replace('\n', '').split(',')
                file_writer.writerow(data)
    print ('Экспорт выполнен\n')


