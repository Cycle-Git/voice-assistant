import pyttsx3
from os import system
import random
import time
import webbrowser
from pyowm import OWM

import requests 
from bs4 import BeautifulSoup
import lxml.html

#иницилизируем голос бро
bro = pyttsx3.init()
voices = bro.getProperty('voices')
bro.setProperty('voice', 'ru') 

bro.setProperty("rate", 165)
bro.setProperty("volume", 3)

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Artemiy':
        bro.setProperty('voice', voice.id)

def brows(): # открывает браузер
    webbrowser.open('https://google.ru')
    x = ['Открываю', 'Уже открываю', 'Гугл к вашим услугам', 'Есть сэр']
    bro.say(random.choice(x))
    bro.runAndWait()

def news(): #последние новости
    url = 'https://stopgame.ru/news'

    query = requests.get(url)
    soup = BeautifulSoup(query.content, "html.parser")

    latest_news = soup.findAll('div' ,class_="caption caption-bold")
    for news in latest_news:
        bro.say(f"{news.get_text(strip=True)} \n")
        bro.runAndWait()

def translate(): # осуществляет поиск в интернете по запросу (adress)
    webbrowser.open('https://translate.google.ru/?hl=ru')
    x = ['Открываю', 'Уже открываю', 'Переводчик к вашим услугам', 'Есть сэр']
    bro.say(random.choice(x))
    bro.runAndWait()

def check_searching(): # проверяет нужно-ли искать в интернете
    pass
 
def vk(): # открывает вк
    webbrowser.open('https://vk.com/feed')

def musik(): # включает музыку
	webbrowser.open('https://vk.com/audios263610075')
 
def youtube(): # открывает ютюб
    webbrowser.open('https://www.youtube.com')
 
def os_off(): # выключает комп
    system('shutdown /s /f /t 10') 

def restart_os():
        oswald.say(random.choice(answers))
        oswald.runAndWait()
        system("shutdown /r /t 10")
        quit()

def show_cmds(): # выводит на экран список доступных комманд
    my_com = ['привет', 'здравствую', 'приветствую', 'дарова', 'пока', 'досвидания','как дела',
    'как настроение', 'открой браузер', 'открой интернет', 'открой vk', 'включи vk', 'открой ютуб','вруби музыку', 'включи музон',
    'выруби комп', 'выключи компютер', 'покажи список команд', 'что планируется', 'планы', 'на будущее', 'переведи', 'Скажи',
    'спасибо']
    for i in my_com:
        print(i) 

def clock(): # тут ещё буду многое менять
    chasov = time.strftime("%H")
    minutes = time.strftime("%M")
    mas_1 = ['00','01','02','03','04','05','06','07','08','09']
    mas_2 = [x for x in range(10,60)]
    sravnenie_1 = [mas_1[2:5], mas_2[12:15], mas_2[22:25], mas_2[32:35], mas_2[42:45]]
    sravnenie_2 = [mas_2[0:11],mas_2[16:21], mas_2[26:31], mas_2[36:41], mas_2[46:50]]

    if chasov in str([mas_1[0:2],mas_2[1::10]]):
        chasov = 'час'
    elif chasov in str(sravnenie_1):
        chasov = 'часа'
    elif chasov in str(sravnenie_2):
        chasov = 'часов'

    if minutes in str([mas_1[0:2],mas_2[1::10]]):
        minutes = 'минута'
    elif minutes in str(sravnenie_1):
        minutes = 'минуты'
    elif minutes in str(sravnenie_2):
        minutes = 'минут'

    bro.say(time.strftime(f"Сейчас %H {chasov} %M {minutes}"))
    bro.runAndWait()

def weather(): # погода
    owm = OWM('78fc9cb466b4aa6945d253a266eec9b5')
    manager = owm.weather_manager()
    place = manager.weather_at_place("Красное")
    res = place.weather
    value = int(res.temperature('celsius')['temp'])
    bro.say(f"В селе красное сейчас {value} градусов по Цельсию")

    if value >= 25 and value < 35:
        bro.say('Господин на улице сейчас тепло.')
    elif value < 25 and value >= 10:
        bro.say('На улице прохладно. Пожалуста одентесь теплее.')
    elif value < 10 and value >= -5:
        bro.say('На улице прохладно. Господин одевайтесь теплее')
    elif value <= -6:
        bro.say('Стоит холодно, Господин Одевай всё что есть')
    else:
        bro.say("Выходим за диапозон значений, фиг его знает, какая погода Господин")
    bro.runAndWait()


cmds = {
    'открой браузер' : brows,
    'открой интернет' : brows,

    'открой vk' : vk,		
    'включи vk' : vk,

    'открой ютуб' : youtube,

    'вруби музыку' : musik,	
    'включи музон' : musik,	

    'найди' : check_searching, 

    'погода' : weather,
    'какая погода' : weather,
    'температура на улице' : weather,

    'переводчик' : translate,
    'переведи' : translate,
    'открой переводчик' : translate,
    
    'новости' : news,

    'выруби комп' : os_off,
    'перезагрузка' : restart_os,
    'перезагрузи комп' : restart_os,
    
    'покажи список команд' : show_cmds,
    'время' : clock,
    'сколько времени' : clock,
}