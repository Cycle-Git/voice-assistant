import speech_recognition as sr
from os import system
from fuzzywuzzy import fuzz # для неточного сравнения
import functions 
import communication

# глобальные переменные
text = ''
r = sr.Recognizer() 
j = 0
adress = ''

ndel = ['бро', 'бр', 'бра', 'чувак','бот','ботяра']

commands = ['привет', 'здравствую', 'приветствую', 'дарова', 'пока', 'досвидания','как дела',
'как настроение', 'открой браузер', 'открой интернет', 'открой vk', 'включи vk', 'открой ютуб','вруби музыку', 'включи музон',
'выруби комп', 'покажи список команд', 'что планируется', 'планы', 'на будущее', 'переведи', 'Скажи',
'спасибо', 'время', 'сколько времени', 'как тебя зовут', 'имя', 'твоё имя', 'Чё как бро', 'температура на улице', 'какая погода',
'погода', 'переводчик', 'открой переводчик', 'новости']

def clear_task(): #удаляет ключевые слова
    global text,ndel
    for z in ndel:
        text = text.replace(z,'').strip()
        text = text.replace('  ',' ').strip()

def comparison(x): # неточное сравнение > 50%
    global commands,j
    ans = ''
    for i in range(len(commands)):
        k = fuzz.ratio(x,commands[i])
        if (k > 50) & (k > j):
            ans = commands[i]
            j = k
    return(str(ans))   

# распознавание голоса
def talk(): 
    global text, clear_task
    text = ''
    with sr.Microphone() as sourse:
        print('Я вас слушаю: ')
        r.adjust_for_ambient_noise(sourse)
        audio = r.listen(sourse, phrase_time_limit=3)
        try:
            text = (r.recognize_google(audio, language="ru-RU")).lower()    
        except(sr.UnknownValueError):
            pass
        except(TypeError):
            pass
        system('cls')
        clear_task()

# выполнение команд
def cmd_exe():
    global cmds, comparison, text, lb
    text = comparison(text)
    print(text)
    if (text in functions.cmds):
        functions.cmds[text]()
    elif (text in communication.cmds): 
        communication.cmds[text]()
    else:
        pass
 
# основная функция для запуска распознавание голоса, а потом выполнения команд
def main(): 
    global text, talk, cmd_exe, j
    try:
        talk()
        if text != '':
            cmd_exe()
            j = 0
    except(UnboundLocalError):
        pass
    except(TypeError):
        pass

communication.hello()
while True:
	main()