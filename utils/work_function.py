import json

from utils.hhru_class import HHJobPlatform
from utils.sj_class import SuperJobPlatform
from utils.vacancy_class import Vacancy


def hh_function(keyword, count_vacancy):
    """Функция вызова класса для работы с хх ру, выводит вакансии по параметрам"""
    get_list = HHJobPlatform(keyword, count_vacancy)  # Создаем экземпляр класса с параметрами пользователя
    list_job = get_list.get_jobs()  # Получаем список вакансий из класса
    print(f'Нашлось {len(list_job)} вакансий.')
    Vacancy.all_class_vacancy = []
    Vacancy.class_vacancy_ex(list_job)
    for item in Vacancy.all_class_vacancy:  # Перебираем и выводим список
        print(str(item))
    print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически')


def sj_function(keyword, count_vacancy):
    """Функция вызова класса для работы с суперджоб, выводит вакансии по параметрам"""
    get_list = SuperJobPlatform(keyword, count_vacancy)  # Создаем экземпляр класса с параметрами пользователя
    list_job = get_list.get_jobs()  # Получаем список вакансий из класса
    print(f'Нашлось {len(list_job)} вакансий!')
    Vacancy.all_class_vacancy = []
    Vacancy.class_vacancy_ex(list_job)
    for item in Vacancy.all_class_vacancy:  # Перебираем и выводим список
        print(str(item))
    print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически')
    # Даём возможность вывести данные в уменьшенном варианте, т.к. в суперджоб длинное описание
    answer_baby = input('Хочешь выведу только наименование вакансии, зарплату и ссылку? да/нет\n')
    if answer_baby.lower() == 'да' or answer_baby.lower() == 'lf':
        with open('vacancy_list_sjru.json', 'r', encoding='utf-8') as file:  # Получаем список из файла
            data = json.load(file)
            for i in data:  # Перебираем список и выводим нужные параметры
                print('Вакансия:', i['title'])
                print('Ссылка:', i['link'])
                print('Зарплата: от', i['salary_min'], ' до', i['salary_max'], '\n')
                print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически')