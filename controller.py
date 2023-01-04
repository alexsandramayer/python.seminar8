import model
import view

def menu():
    choice = input('Выберите необходимый пункт: ')
    if choice == '1':
        surname = input('\nВведите фамилию сотрудника: ')
        model.search_employee(surname)
        view.show_menu()
    elif choice == '2':
        post= input('\nВведите должность сотрудника: ')
        model.post_selection(post)
        view.show_menu()
    elif choice == '3':
        view.level_salary()
    elif choice == '4':
        model.add_employee()
        view.show_menu()
    elif choice == '5':
        index = input('\nВведите индекс сотрудника, которого необходимо удалить: ')
        model.delete_employee(index)
        view.show_menu()
    elif choice == '6':
        index = input('\nВведите индекс сотрудника, чьи данные хотите обновить: ')
        model.update_employee(index)
        view.show_menu()
    elif choice == '7':
        model.export_data_json()
        view.show_menu()
    elif choice == '8':
        model.export_data_csv()
        view.show_menu()
    elif choice == '9':
        exit
    else:
        print('\nНевверный код.\n')
        view.show_menu()



def salary_menu():
    level = input('Выберите необходимый уровень: ')
    model.salary_selection(level)
    view.show_menu()