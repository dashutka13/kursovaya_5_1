def read_command(command):
    """ функция обращается к файлу с sql запросами и возвращает нужную команду по индексу"""
    with open('queries.sql', 'r') as file:
        queries = file.readlines()
    queries = [query.strip() for query in queries]
    return queries[command]
