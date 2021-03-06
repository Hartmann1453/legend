import random
import time

import pyautogui

import defs
import fight
import finder
import puzzle


def start(resourse):
    while True:
        # Проверяем в бою мы или нет. Если в бою - переходим к процедуре боя.
        # После боя возвращаемся в начало цикла.
        if defs.check_fight() != 'Я не в бою':
            fight.start()
            continue

        # Проверяем пазл
        if puzzle.check_puzzle():
            puzzle.start_puzzle()
            continue

        # Проверяем заполненность инвентаря
        if check_inv():
            click_close()
            continue

        # Отлавлиаем ошибку "Добыча не удалась"
        if check_mine_fail():
            click_close()
            continue
        # Отлавлиаем ошибку "Ошибка профессии"
        if check_prof_error():
            click_close()
            continue
        # Отлавлиаем ошибку "Цель не восстановилась"
        if check_target_error():
            click_close()
            continue
        # Отлавлиаем ошибку "Нет инструмента"
        if check_instrument_error():
            click_close()
            continue

        # Ищем вкладку охоты и переходим в неё.
        if defs.click_hunt() == 'Вкладка Охота не найдена': # Переходим к Охоте
            continue

        for i in range(30):
            print(f'Пошла {i} итерация.')
            # Ищем ресурс в локации и нажимаем на него.
            if click_res(resourse) == 'Ресурс не найден':
                continue

            # Проверяем верный ли мы выделили ресурс.
            # Если ошибка - возвращаемся в начало цикла.
            if check_res(resourse) == 'Ресурс не подтвержден': # Проверяем нужный ли моб выбран
                continue

            # Повторно ищем ресурс и начинаем добычу.
            if click_harvest() == 'Иконка не найдена':
                continue


def click_close():
    # Ищем кнопку закрыть
    res_x, res_y = finder.element('img/default/close.png', 30)
    print(f'Элемент найден [Кнопка Выход]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        res_x, res_y = finder.element('img/default/close2.png', 30)
        if res_x == 'Элемент не найден.':
            res_x, res_y = finder.element('img/default/close3.png', 30)
            if res_x == 'Элемент не найден.':
                return

    # Выделяем область клика
    x = random.randint(res_x, res_x + 100)
    y = random.randint(res_y, res_y + 18)

    # Кликаем
    pyautogui.click(x, y)
    print('Нажали на элемент [Кнопка Закрыть]')

def check_inv():
    res_x, res_y = finder.element('img/default/full_inv.png', 3)
    print(f'Элемент найден [Инвентарь полон]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return False
    else:
        return True
def check_mine_fail():
    res_x, res_y = finder.element('img/default/mine_fail.png', 3)
    print(f'Элемент найден [Добыча не удалась]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return False
    else:
        return True

def check_prof_error():
    res_x, res_y = finder.element('img/default/prof_error.png', 3)
    print(f'Элемент найден [Ошибка профессии]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return False
    else:
        return True
def check_target_error():
    res_x, res_y = finder.element('img/default/target_error.png', 3)
    print(f'Элемент найден [Цель не восстановилась]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return False
    else:
        return True
def check_instrument_error():
    res_x, res_y = finder.element('img/default/instrument_error.png', 3)
    print(f'Элемент найден [Нет инструмента]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return False
    else:
        return True

def click_res(resourse):
    # Ищем моба
    crd = finder.pixel_coord(resourse, 3)
    if crd[0] == -1:
        return 'Ресурс не найден'

    # Выделяем область клика
    x = random.randint(crd[1], crd[1] + 4)
    y = random.randint(crd[0], crd[0] + 4)

    # Кликаем
    pyautogui.click(x, y) # Клик на моба
    time.sleep(1)
    print(f'Нажали на элемент [Ресурс {resourse}]')
def check_res(resourse):
    # Ищем иконку моба
    res_x, res_y = finder.element(f'img/resourse/{resourse}/ico_res.png', 3)
    print(f'Элемент найден [Иконка {resourse}]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return 'Ресурс не подтвержден'
def click_harvest():
    # Ищем иконку добычи
    res_x, res_y = finder.element(f'img/default/ico_mine.png', 3)
    print(f'Элемент найден [Иконка]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        res_x, res_y = finder.element(f'img/default/ico_harvest.png', 3)
        if res_x == 'Элемент не найден.':
            return 'Иконка не найдена'

    # Выделяем область клика
    x = random.randint(res_x, res_x + 10)
    y = random.randint(res_y, res_y + 10)

    # Кликаем
    pyautogui.click(x, y) # Клик на моба
    time.sleep(1)
    print(f'Нажали на элемент [Иконка добычи]')

#def click_harvest(resourse):
    # Ищем моба
    #crd = finder.pixel_coord(resourse, 3)
    #if crd[0] == -1:
    #    return 'Ресурс не найден'
#
    #print(f'Элемент найден [Ресурс {resourse}]. x: {crd[1]} | y: {crd[0]}')
    ## Выделяем область клика
    #x = random.randint(crd[1], crd[1] + 4)
    #y = random.randint(crd[0], crd[0] + 4)
#
    ## Кликаем
    #pyautogui.click(x, y)
    #time.sleep(0.3)
    #pyautogui.click(x, y)
#
    #print(f'Нажали на элемент [Ресурс {resourse}]')
#
    ## Пауза для добычи
    #time.sleep(25)
