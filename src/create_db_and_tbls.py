import psycopg2
from read_command_db import read_command


def create_database():
    """создание БД"""
    conn = psycopg2.connect(host='localhost', user='postgres', password='root', port=5432)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS hh_db")
    cur.execute(f'CREATE DATABASE hh_db')

    conn.commit()
    conn.close()


def create_tables():
    """создание таблиц"""
    conn = psycopg2.connect(host='localhost', user='postgres', password='root', port=5432)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS hh_db")
    cur.execute(f'CREATE DATABASE hh_db')
    conn.close()
    conn = psycopg2.connect(host='localhost', database='hh_db', user='postgres', password='root', port=5432)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers (
            employer_id int PRIMARY KEY,
            emp_title varchar(255),
            vacancy_count int
        )""")

    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE vacancies (
        vac_title varchar(100),
        employer_id int REFERENCES employers(employer_id),
        salary_from int,
        salary_to int,
        url varchar(100))""")

    conn.commit()
    conn.close()


def fill_tables(data_list, employer_id):
    """функция заполнения таблиц данными"""
    conn = psycopg2.connect(host='localhost', database='hh_db', user='postgres', password='root', port=5432)
    cur = conn.cursor()

    data_to_employers_tbl = (employer_id, data_list['items'][0]['employer']['name'], data_list['found'])
    cur.execute(read_command(0), data_to_employers_tbl)

    for data in data_list['items']:
        title = data['name']

        if data['salary'] is None:
            salary_from = 0
            salary_to = 0
        else:
            if data['salary']['from'] is None:
                salary_from = 0
            else:
                salary_from = data['salary']['from']

            if data['salary']['to'] is None:
                salary_to = 0
            else:
                salary_to = data['salary']['to']

        url = data['alternate_url']

        data_to_vacancy_tbl = (title, employer_id, salary_from, salary_to, url)
        cur.execute(read_command(1), data_to_vacancy_tbl)
    conn.commit()
    cur.close()
