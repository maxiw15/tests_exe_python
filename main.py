from PIL import ImageTk, Image
import tkinter as tk

import random
from collections import OrderedDict

questionsandanswers = {
    'Кто является субъектами информационных отношений?': [[
        'a) Только пользователи информационных систем',
        'b) Только владельцы информации',
        'c) Люди или организации, взаимодействующие с информацией',
        'd) Правильный вариант ответа отсутствует'], 1],

    'В интересах субъектов информационных отношений лежит': [[
        'a) Только обеспечение конфиденциальности информации',
        'b) Обеспечение конфиденциальности, целостности и доступности информации',
        'c) Только обеспечение доступности информации',
        'd) Правильный вариант ответа отсутствует'], 2],

    'Что означает конфиденциальность информации?': [[
        'a) Защищенность от несанкционированного раскрытия или доступа третьих лиц',
        'b) Защищенность от несанкционированного изменения или уничтожения',
        'c) Доступность для авторизованных пользователей в нужное время и место',
        'd) Правильный вариант ответа отсутствует'], 1],

    'Что означает целостность информации?': [[
        'a) Защищенность от несанкционированного раскрытия или доступа третьих лиц',
        'b) Защищенность от несанкционированного изменения или уничтожения',
        'c) Доступность для авторизованных пользователей в нужное время и место',
        'd) Правильный вариант ответа отсутствует'], 2],

    'Что означает доступность информации?': [[
        'a) Защищенность от несанкционированного раскрытия или доступа третьих лиц',
        'b) Защищенность от несанкционированного изменения или уничтожения',
        'c) Доступность для авторизованных пользователей в нужное время и место',
        'd) Правильный вариант ответа отсутствует'], 3],

    'Какие источники угроз безопасности информации \n могут быть внутренними?': [[
        'a) Хакерские атаки',
        'b) Ошибки сотрудников',
        'c) Физические угрозы',
        'd) Спам и фишинг'], 2],

    'Какие меры защиты используются для противодействия \n угрозам безопасности информации?': [[
        'a) Организационные, технические и физические',
        'b) Политические, экономические и социальные',
        'c) Административные, финансовые и операционные',
        'd) Физические, технические и межличностные'], 1],

    'Какие меры включает в себя организационная защита информации?': [[
        'a) Разработка политики безопасности, проведение аудитов безопасности, обучение сотрудников',
        'b) Установление правил доступа и управление аутентификацией пользователей',
        'c) Использование фаерволлов и антивирусного ПО',
        'd) Физическая защита серверных помещений и системы видеонаблюдения'], 2],

    'Какие меры включает в себя техническая защита информации?': [[
        'a) Использование фаерволлов и антивирусного ПО',
        'b) Разработка политики безопасности и проведение аудитов безопасности',
        'c) Физическая защита серверных помещений и системы видеонаблюдения',
        'd) Обучение сотрудников и установление правил доступа'], 1],

    'Какие меры включает в себя физическая защита информации?': [[
        'a) Физическая защита серверных помещений, \n системы видеонаблюдения, контроль доступа и биометрическая идентификация',
        'b) Разработка политики безопасности и проведение аудитов безопасности',
        'c) Использование фаерволлов и антивирусного ПО',
        'd) Обучение сотрудников и установление правил доступа'], 1],

    'Какие достоинства организационных мерозащиты информации?': [[
        'a) Они формируют правильную культуру безопасности \n в организации и являются основой для обеспечения безопасности информации',
        'b) Они блокируют и обнаруживают атаки',
        'c) Они защищают от новых и неизвестных угроз',
        'd) Они предотвращают проникновение злоумышленников \n при использовании социальной инженерии'], 1],

    'Какой принцип предполагает предоставление доступа к системам \n и данным только необходимым пользователям \n с минимальными правами?': [
        [
            'a) Принцип наименьшего привилегирования',
            'b) Принцип защиты в глубину',
            'c) Принцип постоянного мониторинга и обновления',
            'd) Принцип обучения и осведомления пользователей'], 1],

    'Какой принцип предполагает использование различных уровней \n и слоев защиты для предотвращения или затруднения \n проникновения злоумышленников?': [
        [
            'a) Принцип наименьшего привилегирования',
            'b) Принцип защиты в глубину',
            'c) Принцип постоянного мониторинга и обновления',
            'd) Принцип обучения и осведомления пользователей.'], 2],

    'Какие требования устанавливает закон к качеству информации?': [[
        'a) Точность и достоверность',
        'b) Обязательность наличия электронных копий информации',
        'c) Применение новейших информационных технологий',
        'd) Правильный вариант ответа отсутствует'], 1],

    'Какие права гарантирует закон в отношении доступа к информации?': [[
        'a) Право на получение информации из открытых источников',
        'b) Право на получение информации только с разрешения обладателя информации',
        'c) Право на получение информации только для государственных органов',
        'd) Правильный вариант ответа отсутствует'], 1],

    'Какой приказ устанавливает основные положения и требования \n по безопасному использованию средств '
    'криптографической защиты \n информации с ограниченным доступом?': [
        [
            'a) Приказ ФАПСИ от 13.06.2001 № 152',
            'b) Приказ ФАПСИ от 13.06.2001 № 153',
            'c) Приказ ФАПСИ от 13.06.2001 № 154',
            'd) Приказ ФАПСИ от 13.06.2001 № 155'], 1],

    'Что рассматривается в инструкции по безопасному использованию \n средств криптографической защиты \n информации с '
    'ограниченным доступом?': [
        [
            'a) Риски использования электронной подписи (ЭП)',
            'b) Требования к процедурам создания и хранения резервных \n копий ключей',
            'c) Общие принципы и задачи безопасности при использовании \n средств криптографической защиты информации с ограниченным доступом',
        'd) Правильный вариант ответа отсутствует'], 3],

    'Какие действия регламентируются в инструкции \n по управлению своими сертификатами?': [[
        'a) Отзыв, приостановка и возобновление действия сертификатов',
        'b) Создание и хранение резервных копий ключей',
        'c) Требования к контролю доступа к сертификационным центрам',
        'd) Правильный вариант ответа отсутствует'], 1],

    'Что следует обеспечивать при работе с СКЗИ?': [[
        'a) Безопасное хранение ключевых носителей и кодов доступа',
        'b) Установку необходимых компонентов и настройку параметров работы СКЗИ',
        'c) Проверку срока действия сертификата ЭП',
        'd) Все варианты ответов подходят'], 4],

    'Что не рекомендуется делать при хранении \n ключевых носителей и кодов доступа?': [[
        'a) Хранить их вместе',
        'b) Хранить их в недостаточно защищенном месте',
        'c) Контролировать и учет использования СКЗИ',
        'd) Вести журналы использования и аудита'], 2],

    'Что такое квалифицированная электронная подпись?': [[
        'a) Электронная подпись, которая выполняет требования закона и \n использует квалифицированный сертификат ключа проверки электронной подписи.',
        'b) Электронная подпись, которая не соответствует требованиям закона.',
        'c) Электронная подпись, выполняющая усиленные криптографические алгоритмы.',
        'd) Правильный вариант ответа отсутствует'], 1],


    'Какое значение имеет \n квалифицированная электронная подпись в России?': [[
        'a) Она признается равноценной собственноручной подписи в письменных документах.',
        'b) Она не имеет особого значения по сравнению с другими видами электронных подписей.',
        'c) Она используется только для ограниченного числа документов.',
        'd) Правильный вариант ответа отсутствует'], 1],

}



#Мешаем словарь
# keys = list(questionsandanswers)
# random.shuffle(keys)
# questionsandanswers = OrderedDict(zip(keys, map(questionsandanswers.get, keys)))
#
#
total = 0
question_index = 0


def check_answer(choice):
    global total, question_index
    question = list(questionsandanswers.keys())[question_index]
    answer = questionsandanswers[question][1]
    if choice == answer:
        total += 1
    question_index += 1
    if question_index >= len(questionsandanswers):
        end_quiz()
    else:
        show_question()


def show_question():
    question = list(questionsandanswers.keys())[question_index]
    choices = questionsandanswers[question][0]
    question_label.config(text=question)
    for i, choice in enumerate(choices):
        choice_buttons[i].config(text=choice)


def end_quiz():
    if total > 0:
        succes = "сдали"
    else:
        succes = "не сдали"
    question_label.config(text=f"Ваше число баллов {total} \n"
                               f"Вы {succes} зачет")
    for button in choice_buttons:
        button.config(state=tk.DISABLED)


window = tk.Tk()
image = Image.open("./images.png")
width = 380
ratio = (width / float(image.size[0]))
height = int((float(image.size[1]) * float(ratio)))

image = ImageTk.PhotoImage(image)
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack(side="top", fill="both")
canvas.create_image(0, 0, anchor="nw", image=image)
canvas["background"] = "white"

window.title("Тест")
window.geometry("800x800")
window["background"] = "white"

question_label = tk.Label(window, text="", font='Arial 16 bold', bg='white')

question_label.pack()
choice_buttons = []

for _ in range(4):
    button = tk.Button(window, text="", font='Arial 12', command=lambda i=_: check_answer(i + 1), bg='white')
    choice_buttons.append(button)
    button.pack()

show_question()

window.mainloop()
