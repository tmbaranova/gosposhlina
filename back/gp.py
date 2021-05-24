from docxtpl import DocxTemplate #для создания док-та на основе вордовского шаблона
import datetime
import json
import subprocess #для открытия файла программой по-умолчанию

import webbrowser

courts_dict = {
    'Алтайского края': 'altai-krai',
    'Амурской области': 'amuras',
    'Архангельской области': 'arhangelsk',
    'Астраханской области': 'astrahan',
    'Белгородской области': 'belgorod',
    'Брянской области': 'bryansk',
    'Вологодской области': 'vologda',
    'Москвы': 'msk',
    'Санкт-Петербурга и Ленинградской области': 'spb',
    'Забайкальского края': 'chita',
    'Кемеровской области': 'kemerovo',
    'Костромской области': 'kostroma',
    'Красноярского края': 'krasnoyarsk',
    'Московской области': 'asmo',
    'Пермского края': 'perm',
    'Приморского края': 'primkray',
    'Псковской области': 'pskov',
    'Республики Алтай': 'altai',
    'Республики Башкортостан': 'ufa',
    'Республики Бурятия': 'buryatia',
    'Саратовской области': 'saratov',
    'Тульской области': 'tula',
    'Хабаровского края': 'khabarovsk',
    'Ярославской области': 'yaroslavl',
    'Свердловской области': 'ekaterinburg',
}


def gosposhlina(summa_iska):  # аргумент - строка
    """Функция расчета госпошлины по сумме иска"""
    summa_iska = float(summa_iska)
    if summa_iska <= 100000:
        gp = summa_iska/100*4
        if gp < 2000:
            gp = 2000

    elif summa_iska <= 200000:
        gp = 4000 + (summa_iska-100000)/100*3

    elif summa_iska <= 1000000:
        gp = 7000 + (summa_iska-200000)/100*2

    elif summa_iska <= 2000000:
        gp = 23000 + (summa_iska-1000000)/100*1

    elif summa_iska > 2000000:
        gp = 33000 + (summa_iska-2000000)/100*0.5
        if gp > 200000:
            gp = 200000
    return round(gp)


def url(court):
    """Функция, определяющая ссылку на страницу с реквизитами по наименованию суда"""
    url = ''
    for court_name in courts_dict:
        if court_name in court:
            court_link = courts_dict[court_name]
            url = f'http://{court_link}.arbitr.ru/process/duty/commission'
            return url

    if url == '':
        return f'Добавьте суд в справочник'


def open_url(court):
    if court == '':
        return f'Заполните графу "суд"'
    link = url(court)
    webbrowser.open(link, new=2)


def zayava_for_event(summa_iska, sud, otvetchik):
    """Запуск функции создания заявки по событию нажатие на кнопку"""
    if summa_iska == '' or summa_iska == 0:
        return
    elif sud == '' and otvetchik == '':
        gp = gosposhlina(summa_iska)
        sud = 'АС г. Москвы'
        otvetchik = 'ОАО"РЖД"'
        zayava_word(summa_iska, gp, sud, otvetchik)
        lst = [gp, sud, otvetchik]
        return lst

    elif sud == '' or otvetchik == '':
        return
    else:
        gp = gosposhlina(summa_iska)
        zayava_word(summa_iska, gp, sud, otvetchik)
        lst = [gp, sud, otvetchik]
        return lst



def zayava_word(summa, gp, sud, otvetchik):
    """Создание заявки на основе вордовского шаблона"""
    doc = DocxTemplate("шаблон.docx")
    now = datetime.datetime.today()
    now = now.strftime("%d.%m.%Y")
    context = {'otvetchik': otvetchik, 'sud': sud, 'gp': gp, 'summa_iska': summa, 'data': now}
    doc.render(context)
    doc.save("шаблон-final.docx")
    subprocess.Popen("шаблон-final.docx", shell=True)  # открыть файл программой по-умолчанию

