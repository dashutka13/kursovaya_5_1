import requests


def connect_vacancy(id_company):
    """ подключение к hh и получение json """
    url = 'https://api.hh.ru/vacancies'
    params = {'employer_id': id_company,
              'per_page': '100'}
    headers = {
        "User-Agent": "50355527",  # User-Agent header из личного кабинета hh
    }
    response = requests.get(url, params=params, headers=headers)  # подключение к API hh
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Ошибка, код ответа{response.status_code}')
