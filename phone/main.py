def ask_data():
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ") 
    phone = input("Введите номер телефона: ")
    contact = {
        'second_name': s_name,
        'first_name': f_name,
        'middle_name': m_name,
        'phone_number': phone
    }
    return contact

def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for key, value in contact.items():
            file.write(value, delimiter = ';')
        file.write('\n')

def open_phonebook():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t\t".join(line.split(";")))
            
def show_contact_lines():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines_with_contacts = [line.strip() for line in file if line.strip()]

    if not lines_with_contacts:
        print("Телефонная книга пуста.")
        return

    print("Контактная информация на следующих строках:")
    for i, line in enumerate(lines_with_contacts, start=1):
        print(f"{i}: {line}")            

def find_contact():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    s_name = input("Введите фамилию: ")
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            if s_name in line:
                print("\t\t".join(line.split(";")))


def export_contact_by_line():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines_with_contacts = [line.strip() for line in file if line.strip()]

    if not lines_with_contacts:
        print("Телефонная книга пуста.")
        return

    print("Контактная информация на следующих строках:")
    for i, line in enumerate(lines_with_contacts, start=1):
        print(f"{i}: {line}")

    choice = int(input("Введите номер строки с контактом для экспорта: ")) - 1

    if 0 <= choice < len(lines_with_contacts):
        export_file_name = input("Введите имя файла для экспорта: ")
        with open(export_file_name, 'w', encoding='utf-8') as export_file:
            export_file.write(lines_with_contacts[choice] + '\n')
        print("Контакт успешно экспортирован.")
    else:
        print("Некорректный номер строки.")
    

def main():
    isStop = 10
    while isStop != 0:
        print(f"Выберете что хотите сделать:\n1 найти\n2 добавить\n3 экспорт контакта\n4 открыть всю книгу\n5 строчка контакта\n0 выход")
        isStop = int(input(">"))
        if isStop == 1:
            find_contact()
        elif isStop == 3:
            export_contact_by_line()
        elif isStop == 2:
            add_new_contact()
        elif isStop == 4:
            add_new_contact()            
        elif isStop == 5:
            show_contact_lines()
        input("Нажмите Enter чтобы продолжить")

main()












































# def sort_phonebook():
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         contacts = [line.strip().split(';') for line in file]
#     sorted_contacts = sorted(contacts, key=lambda x: x[0])  # Сортировка по фамилии
#     with open('phonebook.txt', 'w', encoding='utf-8') as file:
#         for contact in sorted_contacts:
#             file.write(';'.join(contact) + '\n')

# def add_new_contact():
#     contact = ask_data()
#     with open('phonebook.txt', 'a', encoding='utf-8') as file:
#         for key, value in contact.items():
#             file.write(value + ';')
#         file.write('\n')
#     sort_phonebook()  # Добавление нового контакта и сортировка книги

# def find_contact():
#     title = ["Фамилия", "Имя", "Отчество", "Телефон"]
#     s_name = input("Введите фамилию: ")
#     found_contacts = []
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             fields = line.strip().split(';')
#             if s_name == fields[0]:
#                 found_contacts.append(fields)
#     if found_contacts:
#         # found_contacts_sorted = sorted(found_contacts, key=lambda x: x[1])  # Сортировка по имени
#         print("\t\t".join(title))
#         for contact in found_contacts:
#             print("\t\t".join(contact))
#     else:
#         print("Контакт не найден.")

# def delete_contact():
#     s_name = input("Введите фамилию контакта для удаления: ")
#     f_name = input("Введите имя контакта для удаления: ")
#     m_name = input("Введите отчество контакта для удаления: ")
#     found_contacts = []
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             fields = line.strip().split(';')
#             if s_name == fields[0] and f_name == fields[1] and m_name == fields[2]:
#                 found_contacts.append(fields)
#     if found_contacts:
#         found_contacts.sort(key=lambda x: x[0])  # Sort by surname
#         print("Найдены следующие контакты:")
#         for i, contact in enumerate(found_contacts):
#             print(f"{i + 1}. {contact[0]} {contact[1]} {contact[2]} - {contact[3]}")
#         choice = int(input("Введите номер контакта для удаления: ")) - 1
#         del found_contacts[choice]
#         with open('phonebook.txt', 'w', encoding='utf-8') as file:
#             for contact in found_contacts:
#                 file.write(';'.join(contact) + '\n')
#         sort_phonebook()  # Sort the phonebook after deleting a contact
#         print("Контакт успешно удален.")
#     else:
#         print("Контакт не найден.")


# def main():
#     isStop = 10
#     while isStop != 0:
#         print(f"Выберете что хотите сделать:\n1 найти\n2 добавить\n3 удалить\n4 открыть всю книгу\n5 копирование\n0 выход")
#         isStop = int(input(">"))
#         if isStop == 1:
#             find_contact()
#         elif isStop == 2:
#             add_new_contact()
#         elif isStop == 3:
#             delete_contact()
#         elif isStop == 4:
#             open_phonebook()
#         input("Нажмите Enter чтобы продолжить")

# # sort_phonebook()  # Не нужно вызывать здесь
# main()




# def ask_data():
#     s_name = input("Введите фамилию: ")
#     f_name = input("Введите имя: ")

#     m_name = input("Введите отчество: ") 
#     phone = input("Введите номер телефона: ")
#     contact = {
#         'second_name': s_name,
#         'first_name': f_name,
#         'middle_name': m_name,
#         'phone_number': phone
#     }
#     return contact

# def add_new_contact():
#     contact = ask_data()
#     with open('phonebook.txt', 'a', encoding='utf-8') as file:
#         for key, value in contact.items():
#             file.write(value + ';')
#         file.write('\n')

# def open_phonebook():
#     title = ["Фамилия", "Имя", "Отчество", "Телефон"]
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         print("\t\t".join(title))
#         for line in file:
#             print("\t\t".join(line.split(";")))

# def find_contact():
#     title = ["Фамилия", "Имя", "Отчество", "Телефон"]
#     s_name = input("Введите фамилию: ")
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         print("\t\t".join(title))
#         found = False
#         for line in file:
#             if s_name in line:
#                 found = True
#                 print("\t\t".join(line.split(";")))
#         if not found:
#             print("Контакт с такой фамилией не найден.")

# def export_phonebook():
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         data = file.read()
#     with open('exported_phonebook.txt', 'w', encoding='utf-8') as file:
#         file.write(data)
#     print("Телефонный справочник успешно экспортирован в файл exported_phonebook.txt")

# def import_phonebook():
#     file_name = input("Введите имя файла для импорта: ")
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             data = file.read()
#         with open('phonebook.txt', 'w', encoding='utf-8') as file:
#             file.write(data)
#         print("Телефонный справочник успешно импортирован из файла", file_name)
#     except FileNotFoundError:
#         print("Файл не найден.")

# def main():
#     while True:
#         print("\nМеню:")
#         print("1. Добавить новый контакт")
#         print("2. Открыть телефонный справочник")
#         print("3. Найти контакт по фамилии")
#         print("4. Экспортировать телефонный справочник")
#         print("5. Импортировать телефонный справочник")
#         print("0. Выйти из программы")
#         choice = input("Выберите действие: ")

#         if choice == "1":
#             add_new_contact()
#         elif choice == "2":
#             open_phonebook()
#         elif choice == "3":
#             find_contact()
#         elif choice == "4":
#             export_phonebook()
#         elif choice == "5":
#             import_phonebook()
#         elif choice == "0":
#             print("Программа завершена.")
#             break
#         else:
#             print("Неправильный выбор. Попробуйте снова.")

# if __name__ == "__main__":
#     main()
