from DBManager import DBManager
from config import config
from hh_get_company import connect_vacancy
from create_db_and_tbls import create_database, create_tables, fill_tables

COMPANIES_IDS = [3529, 816144, 3458, 4880, 23427, 7172, 2748, 3127, 30751, 370]
params = config()
DB_class = DBManager(params)

input(f'\nЧтобы показать вакансии {len(COMPANIES_IDS)} компаний - нажмите "Enter"')

print("\nОжидайте...")
create_database()
create_tables()
print("\nГотово!")


for id in COMPANIES_IDS:
    vacancy_list = connect_vacancy(id)
    fill_tables(vacancy_list, id)
    count_vacancy = vacancy_list['found']

    print('\n***', vacancy_list["items"][0]["employer"]["name"], '***',\
    f'Всего ваканcий {count_vacancy}, до 100 вакансий добавлено в базу данных.')


while True:
    print('\nВыберите действие и введите команду:\n'
                      '1 - показать список всех компаний и количество вакансий\n'
                      '2 - показать список вакансий, название компании, зп, ссылка на вакансию\n'
                      '3 - показать среднюю зп\n'
                      '4 - показать вакансии с зп выше среднего по всем вакансиям\n'
                      '5 - показать вакансии со словом python\n'
                      'Выход - завершить работу программы\n')

    user_input = input()

    if user_input == '1':
        DB_class.get_companies_and_vacancies_count()

    elif user_input == '2':
        DB_class.get_all_vacancies()

    elif user_input == '3':
        DB_class.get_avg_salary()

    elif user_input == '4':
        DB_class.get_vacancies_with_higher_salary()

    elif user_input == '5':
        DB_class.get_vacancies_with_keyword()

    elif user_input.lower() == 'выход' or user_input.lower() == 'ds[jl':
        break

    else:
        print("Не знаю такую команду!")
        input('Чтобы вернуться в начало, нажми enter')
