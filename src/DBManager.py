import psycopg2

from read_command_db import read_command


class DBManager:

    def __init__(self, params: dict):
        self.params = params

    def get_companies_and_vacancies_count(self):
        """ получение списка всех компаний и количество вакансий в компании """
        conn = psycopg2.connect(database='hh_db', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(2))
            rows = cur.fetchall()
            for row in rows:
                print(f'Компания - {row[0]}. Вакансий в компании - {row[1]}.')

    def get_all_vacancies(self):
        """ получение списка вакансий с названием компании, вакансии и зп, ссылка на вакансию """
        conn = psycopg2.connect(database='hh_db', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(3))
            rows = cur.fetchall()
            for row in rows:
                print(
                    f'Компания - {row[0]} *** Вакансия - {row[1]} *** ЗП от {row[2]} до {row[3]} *** Ссылка {row[4]}')

    def get_avg_salary(self):
        """ получение средней зп по вакансиям в компаниях """
        conn = psycopg2.connect(database='hh_db', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(4))
            rows = cur.fetchall()
            for row in rows:
                print(f'Компания - {row[0]} \ Средняя ЗП - {row[1]}')

    def get_vacancies_with_higher_salary(self):
        """ получение списка и ссылки всех вакансий,у которых зп выше средней """
        conn = psycopg2.connect(database='hh_db', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(5))
            rows = cur.fetchall()
            for row in rows:
                print(f'Вакансия - {row[0]} \ Ссылка- {row[1]}')

    def get_vacancies_with_keyword(self):
        """ получение списка и ссылок на вакансии, в названии которых содержатся переданные в метод слова """
        conn = psycopg2.connect(database='hh_db', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(6))
            rows = cur.fetchall()
            for row in rows:
                print(f'Вакансия - {row[0]} \ Ссылка- {row[1]}')
