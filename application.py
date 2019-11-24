#Assistent in site v.2.4
assistant = input('Здравствуйте, как вы хотели, чтоб меня звали?\n\n')
print('\nХорошо, теперь я, ' + assistant + ' - ваш ассистент')
answer = input('Что вы хотите? (Калькулятор, Шутка, Назвать, Время, Советы, Сайт, Погода)\n\n')
if answer == "Калькулятор" or answer == 'калькулятор':
    what = input("Что делаем? (+, -, *, /): ")

    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))

    if what == '+':
        c = a + b
        print("Результат: " + str(c))
    elif what =='-':
        c = a - b
        print("Результат: " + str(c))
    elif what =='*':
        c = a * b
        print('Результат: ' + str(c))
    elif what =='/':
        c = a / b
        print("Результат: " + str(c))
    else:
        print("Выбрана неверная операция!")

elif answer == "Шутка" or answer == 'шутка':
    import random  
    strings = ['\nМеня бесит, что я все время спокоен\n', '\nКолобок повесился\n', '\nDomestos - убивает все известные микробы! А неизвестные берет в плен,\nдля опытов...\n',
    '\nВстречаются два директора: \n- Ты своим зарплату платишь? \n- Нет. \n- И я нет. А они все равно на работу ходят? \n- Ходят. \n- И мои ходят. Может, вход платный сделаем?\n',
    '\n-Сынок, у базара остановишь?\n-Базара нет, бабуля\n-Как нет? Вчера же ещё был\n', '\n-Что купил?\n-Ничего\n-А кому?\n-Себе\n-Ничего себе!\n',
    '\n-Шеф, вызывали?\n-Да, я повышаю тебе зарплату в 0,5 раз\n', '\nМало кто знает, но 90-60-90 это скорость перед постом ГАИ\n',
    '\nЕсли свет на кухне включать-выключать каджые 5 секунд,\nТо тараканы умрут от челночного бега туда-обратно\n']
    print(random.choice(strings))

elif answer == "Назвать" or answer == 'назвать':
    name = input('Введите имя того, кого хотите назвать кем-то\n')
    rang = input('Какое звание должно быть у ' + name + "?\n")
    print('Официально заявляю, что ' + name + " - " + rang)

elif answer == 'Время' or answer == 'время':
    import time
    a = time.ctime(time.time())
    print(a)

elif answer == 'Советы' or answer == 'советы' or answer == 'совет' or answer == 'совет':
    import random  
    strings = ['\nКогда моете ложку, не забывайте о том, что её нужно держать вертикально\n', '\nСпи хоть примерно по графику, так будет намного проще\n',
    '\nМеньше говори о своимх планах\nПоверь мне...\n']
    print(random.choice(strings))

elif answer == 'Сайт' or answer == 'сайт' or answer == 'Сайты' or answer == 'сайты':
    qwe = input('Какой тип сайта вы хотите? (Математика, Ютуб, Gmail)\n')
    if qwe == 'Математика' or qwe == 'математика':
        print('Это сайт, где вы можете потренироваться в математике')
        sos = input('Напишите что-нибудь и сайт откроется\n')
        import webbrowser
        webbrowser.open('http://bekhruz-train-your-math.herokuapp.com/')
    elif qwe == 'Ютуб' or qwe == 'ютуб' or qwe == 'ютюб' or qwe == 'Ютюб':
        import webbrowser
        webbrowser.open('http://youtube.com/')
        
    elif qwe == 'Gmail' or qwe == 'gmail':
        import webbrowser
        webbrowser.open('http://gmail.com/')

    else:
        print('Я пока не могу открыть такой сайт')


elif answer == 'Погода' or answer == 'погода': 
    hao = input('\nВ каком месте вы хотите погоду? (Афины, Москва)\n')
    if hao == 'Афины' or hao == 'афины':
     import webbrowser
     webbrowser.open("https://openweathermap.org/city/264371")
    elif hao == 'Москва' or hao == 'москва':
     import webbrowser
     webbrowser.open("https://openweathermap.org/city/524901")	
    else:
     print('В таком месте я погоду сказать не могу')

else:
    print('такого я не умею')

das = input('Может еще раз или какое-нибудь другое действие?(Калькулятор, Шутка, Назвать, Время, Советы, Сайт, Погода)\n\n')
if das == "Калькулятор" or das == 'калькулятор':
    whatfd = input("Что делаем? (+, -, *, /): ")

    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))

    if whatfd == '+':
        c = a + b
        print("Результат: " + str(c))
    elif whatfd =='-':
        c = a - b
        print("Результат: " + str(c))
    elif whatfd =='*':
        c = a * b
        print('Результат: ' + str(c))
    elif whatfd =='/':
        c = a / b
        print("Результат: " + str(c))
    else:
        print("Выбрана неверная операция!")

elif das == "Шутка" or das == 'шутка':
    import random  
    strings = ['\nМеня бесит, что я все время спокоен\n', '\nКолобок повесился\n', '\nDomestos - убивает все известные микробы! А неизвестные берет в плен,\nдля опытов...\n',
    '\nВстречаются два директора: \n- Ты своим зарплату платишь? \n- Нет. \n- И я нет. А они все равно на работу ходят? \n- Ходят. \n- И мои ходят. Может, вход платный сделаем?\n',
    '\n-Сынок, у базара остановишь?\n-Базара нет, бабуля\n-Как нет? Вчера же ещё был\n', '\n-Что купил?\n-Ничего\n-А кому?\n-Себе\n-Ничего себе!\n',
    '\n-Шеф, вызывали?\n-Да, я повышаю тебе зарплату в 0,5 раз\n', '\nМало кто знает, но 90-60-90 это скорость перед постом ГАИ\n',
    '\nЕсли свет на кухне включать-выключать каджые 5 секунд,\nТо тараканы умрут от челночного бега туда-обратно\n']
    print(random.choice(strings))

elif das == "Назвать" or answer == 'назвать':
    name = input('Введите имя того, кого хотите назвать кем-то\n')
    rang = input('Какое звание должно быть у ' + name + "?\n")
    print('Официально заявляю, что ' + name + " - " + rang)

elif das == 'Время' or das == 'время':
    import time
    a = time.ctime(time.time())
    print(a) 
    
elif das == 'нет' or das == 'не' or das == 'не хочу' or das == 'Нет' or das == 'Не' or das == 'Не хочу':
    import random  
    strings = ['Ладно, пока!', 'Думаю на сегодня хватит', 'Хорошо пообщались']
    print(random.choice(strings))
    po = input()

elif das == 'Советы' or das == 'советы' or das == 'совет' or das == 'совет':
    import random  
    strings = ['\nКогда моете ложку, не забывайте о том, что её нужно держать вертикально\n', '\nСпи хоть примерно по графику, так будет намного проще\n',
    '\nМеньше говори о своимх планах\nПоверь мне...\n']
    print(random.choice(strings))

elif das == 'Сайт' or das == 'сайт' 'сайт' or das == 'Сайты' or das == 'сайты':
    qwq = input('Какой тип сайта вы хотите? (Математика, Ютуб, Gmail)\n')
    if qwq == 'Математика' or qwq == 'математика':
        print('Это сайт, где вы можете потренироваться в математике')
        sos = input('Напишите что-нибудь и сайт откроется\n')
        import webbrowser
        webbrowser.open('http://bekhruz-train-your-math.herokuapp.com/')
    elif qwq == 'Ютуб' or qwq == 'ютуб' or qwq == 'ютюб' or qwq == 'Ютюб':
        import webbrowser
        webbrowser.open('http://youtube.com/')
        
    elif qwq == 'Gmail' or qwq == 'gmail':
        import webbrowser
        webbrowser.open('http://gmail.com/')

    else:
        print('Я пока не могу открыть такой сайт')

elif das == 'Погода' or answer == 'погода': 
    hai = input('\nВ каком месте вы хотите погоду? (Афины, Москва)\n')
    if hai == 'Афины' or hai == 'афины':
     import webbrowser
     webbrowser.open("https://openweathermap.org/city/264371")
    elif hai == 'Москва' or hai == 'москва':
     import webbrowser
     webbrowser.open("https://openweathermap.org/city/524901")
    else:
     print('В таком месте я погоду сказать не могу')
        
else:
    print('Такого я не умею')

tot = input(assistant + ' спрашивает: продолжим?(Калькулятор, Шутка, Назвать, Время, Советы, Сайт, Погода)\n\n')

if tot == "Калькулятор" or tot == 'калькулятор':
    whatdf = input("Что делаем? (+, -, *, /): ")

    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))

    if whatdf == '+':
        c = a + b
        print("Результат: " + str(c))
    elif whatdf =='-':
        c = a - b
        print("Результат: " + str(c))
    elif whatdf =='*':
        c = a * b
        print('Результат: ' + str(c))
    elif whatdf =='/':
        c = a / b
        print("Результат: " + str(c))
    else:
        print("Выбрана неверная операция!")

elif tot == "Шутка" or tot == 'шутка':
    import random  
    strings = ['\nМеня бесит, что я все время спокоен\n', '\nКолобок повесился\n', '\nDomestos - убивает все известные микробы! А неизвестные берет в плен,\nдля опытов...\n',
    '\nВстречаются два директора: \n- Ты своим зарплату платишь? \n- Нет. \n- И я нет. А они все равно на работу ходят? \n- Ходят. \n- И мои ходят. Может, вход платный сделаем?\n',
    '\n-Сынок, у базара остановишь?\n-Базара нет, бабуля\n-Как нет? Вчера же ещё был\n', '\n-Что купил?\n-Ничего\n-А кому?\n-Себе\n-Ничего себе!\n',
    '\n-Шеф, вызывали?\n-Да, я повышаю тебе зарплату в 0,5 раз\n', '\nМало кто знает, но 90-60-90 это скорость перед постом ГАИ\n',
    '\nЕсли свет на кухне включать-выключать каджые 5 секунд,\nТо тараканы умрут от челночного бега туда-обратно\n']
    print(random.choice(strings))

elif tot == "Назвать" or tot == 'назвать':
    name = input('Введите имя того, кого хотите назвать кем-то\n')
    rang = input('Какое звание должно быть у ' + name + "?\n")
    print('Официально заявляю, что ' + name + " - " + rang)

elif tot == 'Время' or tot == 'время':
    import time
    a = time.ctime(time.time())
    print(a) 

elif tot == 'нет' or tot == 'не' or tot == 'не хочу' or tot == 'Нет' or tot == 'Не' or tot == 'Не хочу':
    import random  
    strings = ['Ладно, пока!', 'Думаю, на сегодня хватит', 'Хорошо пообщались']
    print(random.choice(strings))
    op = input()

elif tot == 'Советы' or tot == 'советы' or tot == 'совет' or tot == 'совет':
    import random  
    strings = ['\nКогда моете ложку, не забывайте о том, что её нужно держать вертикально\n', '\nСпи хоть примерно по графику, так будет намного проще\n',
    '\nМеньше говори о своимх планах\nПоверь мне...\n']
    print(random.choice(strings))

elif tot == 'Сайт' or tot == 'сайт' 'сайт' or tot == 'Сайты' or tot == 'сайты':
    qwew = input('Какой тип сайта вы хотите? (Математика, Ютуб, Gmail)\n')
    if qwew == 'Математика' or qwew == 'математика':
        print('Это сайт, где вы можете потренироваться в математике')
        sos = input('Напишите что-нибудь и сайт откроется\n')
        import webbrowser
        webbrowser.open('http://bekhruz-train-your-math.herokuapp.com/')
    elif qwew == 'Ютуб' or qwew == 'ютуб' or qwew == 'ютюб' or qwew == 'Ютюб':
        import webbrowser
        webbrowser.open('http://youtube.com/')
        
    elif qwew == 'Gmail' or qwew == 'gmail':
        import webbrowser
        webbrowser.open('http://gmail.com/')

    else:
        print('Я пока не могу открыть такой сайт')

elif tot == 'Погода' or answer == 'погода': 
    hau = input('\nВ каком месте вы хотите погоду? (Афины, Москва)\n')
    if hau == 'Афины' or hau == 'афины':
     import webbrowser
     webbrowser.open("https://openweathermap.org/city/264371")
    elif hau == 'Москва' or hau == 'москва':
     import webbrowser
     webbrowser.open("https://openweathermap.org/city/524901")
    else:
     print('В таком месте я погоду сказать не могу')

elif tot == 'Да' or tot == 'да':
    print('\nВыбирайте дальше\n')
    
else:
    print('Такого я не умею')

kik = input('\nХватит?\n\n')
if kik == 'да' or kik == 'хватит' or kik == 'Да' or kik == 'Хватит':
    import random  
    strings = ['Ладно, пока!', 'Думаю на сегодня хватит', 'Хорошо пообщались']
    print(random.choice(strings))
else:
    ut = input('\nМожете снова попробувать предыдущие функции(Калькулятор, Шутка, Назвать, Время, Советы, Сайт, Погода)\n\n')
    if ut == "Калькулятор" or ut == 'калькулятор':
        whatasd = input("Что делаем? (+, -, *, /): ")

        a = float(input("Введи первое число: "))
        b = float(input("Введи второе число: "))

        if whatasd == '+':
            c = a + b
            print("Результат: " + str(c))
        elif whatasd =='-':
            c = a - b
            print("Результат: " + str(c))
        elif whatasd =='*':
            c = a * b
            print('Результат: ' + str(c))
        elif whatasd =='/':
            c = a / b
            print("Результат: " + str(c))
        else:
            print("Выбрана неверная операция!")

    elif ut == "Шутка" or ut == 'шутка':
        import random  
        strings = ['\nМеня бесит, что я все время спокоен\n', '\nКолобок повесился\n', '\nDomestos - убивает все известные микробы! А неизвестные берет в плен,\nдля опытов...\n',
        '\nВстречаются два директора: \n- Ты своим зарплату платишь? \n- Нет. \n- И я нет. А они все равно на работу ходят? \n- Ходят. \n- И мои ходят. Может, вход платный сделаем?\n',
        '\n-Сынок, у базара остановишь?\n-Базара нет, бабуля\n-Как нет? Вчера же ещё был\n', '\n-Что купил?\n-Ничего\n-А кому?\n-Себе\n-Ничего себе!\n',
        '\n-Шеф, вызывали?\n-Да, я повышаю тебе зарплату в 0,5 раз\n', '\nМало кто знает, но 90-60-90 это скорость перед постом ГАИ\n',
        '\nЕсли свет на кухне включать-выключать каджые 5 секунд,\nТо тараканы умрут от челночного бега туда-обратно\n']
        print(random.choice(strings))

    elif ut == "Назвать" or ut == 'назвать':
        name = input('Введите имя того, кого хотите назвать кем-то\n')
        rang = input('Какое звание должно быть у ' + name + "?\n")
        print('Официально заявляю, что ' + name + " - " + rang)

    elif ut == 'Время' or ut == 'время':
        import time
        a = time.ctime(time.time())
        print(a)

    elif ut == 'Советы' or ut == 'советы' or ut == 'совет' or ut == 'совет':
        import random  
        strings = ['\nКогда моете ложку, не забывайте о том, что её нужно держать вертикально\n', '\nСпи хоть примерно по графику, так будет намного проще\n',
        '\nМеньше говори о своимх планах\nПоверь мне...\n']
        print(random.choice(strings))

    elif ut == 'Сайт' or ut == 'сайт' or ut == 'Сайты' or ut == 'сайты':
        qweq = input('Какой тип сайта вы хотите? (Математика, Ютуб, Gmail)\n')
        if qweq == 'Математика' or qweq == 'математика':
            print('Это сайт, где вы можете потренироваться в математике')
            sos = input('Напишите что-нибудь и сайт откроется\n')
            import webbrowser
            webbrowser.open('http://bekhruz-train-your-math.herokuapp.com/')
            
        elif qweq == 'Ютуб' or qweq == 'ютуб' or qweq == 'ютюб' or qweq == 'Ютюб':
            import webbrowser
            webbrowser.open('http://youtube.com/')
        
        elif qweq == 'Gmail' or qweq == 'gmail':
            import webbrowser
            webbrowser.open('http://gmail.com/')
            
        else:
            print('Я пока не могу открыть такой сайт')

    elif ut == 'Погода' or answer == 'погода': 
        hah = input('\nВ каком месте вы хотите погоду? (Афины, Москва)\n')
        if hah == 'Афины' or hah == 'афины':
         import webbrowser
         webbrowser.open("https://openweathermap.org/city/264371")
        elif hah == 'Москва' or hah == 'москва':
         import webbrowser
         webbrowser.open("https://openweathermap.org/city/524901")
        else:
            print('В таком месте я погоду сказать не могу')


pot = input('\n(Калькулятор, Шутка, Назвать, Время, Советы, Сайт, Погода)\n\n')
if pot == "Калькулятор" or answer == 'калькулятор':
    wham = input("Что делаем? (+, -, *, /): ")

    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))

    if wham == '+':
        c = a + b
        print("Результат: " + str(c))
    elif wham =='-':
        c = a - b
        print("Результат: " + str(c))
    elif wham =='*':
        c = a * b
        print('Результат: ' + str(c))
    elif wham =='/':
        c = a / b
        print("Результат: " + str(c))
    else:
        print("Выбрана неверная операция!")

elif pot == "Шутка" or pot == 'шутка':
    import random  
    strings = ['\nМеня бесит, что я все время спокоен\n', '\nКолобок повесился\n', '\nDomestos - убивает все известные микробы! А неизвестные берет в плен,\nдля опытов...\n',
    '\nВстречаются два директора: \n- Ты своим зарплату платишь? \n- Нет. \n- И я нет. А они все равно на работу ходят? \n- Ходят. \n- И мои ходят. Может, вход платный сделаем?\n',
    '\n-Сынок, у базара остановишь?\n-Базара нет, бабуля\n-Как нет? Вчера же ещё был\n', '\n-Что купил?\n-Ничего\n-А кому?\n-Себе\n-Ничего себе!\n',
    '\n-Шеф, вызывали?\n-Да, я повышаю тебе зарплату в 0,5 раз\n', '\nМало кто знает, но 90-60-90 это скорость перед постом ГАИ\n',
    '\nЕсли свет на кухне включать-выключать каджые 5 секунд,\nТо тараканы умрут от челночного бега туда-обратно\n']
    print(random.choice(strings))

elif pot == "Назвать" or pot == 'назвать':
    name = input('Введите имя того, кого хотите назвать кем-то\n')
    rang = input('Какое звание должно быть у ' + name + "?\n")
    print('Официально заявляю, что ' + name + " - " + rang)

elif pot == 'Время' or pot == 'время':
    import time
    a = time.ctime(time.time())
    print(a)

elif pot == 'Советы' or pot == 'советы' or pot == 'совет' or pot == 'совет':
    import random  
    strings = ['\nКогда моете ложку, не забывайте о том, что её нужно держать вертикально\n', '\nСпи хоть примерно по графику, так будет намного проще\n',
    '\nМеньше говори о своимх планах\nПоверь мне...\n']
    print(random.choice(strings))

elif pot == 'Сайт' or pot == 'сайт' 'сайт' or pot == 'Сайты' or pot == 'сайты':
    qweqwe = input('Какой тип сайта вы хотите? (Математика, Ютуб, Gmail)\n')
    if qweqwe == 'Математика' or qweqwe == 'математика':
        print('Это сайт, где вы можете потренироваться в математике')
        sos = input('Напишите что-нибудь и сайт откроется\n')
        import webbrowser
        webbrowser.open('http://bekhruz-train-your-math.herokuapp.com/')
    elif qweqwe == 'Ютуб' or qweqwe == 'ютуб' or qweqwe == 'ютюб' or qweqwe == 'Ютюб':
        import webbrowser
        webbrowser.open('http://youtube.com/')
        
    elif qweqwe == 'Gmail' or qweqwe == 'gmail':
        import webbrowser
        webbrowser.open('http://gmail.com/')

    else:
        print('Я пока не могу открыть такой сайт')


elif pot == 'Погода' or pot == 'погода': 
    haoha = input('\nВ каком месте вы хотите погоду? (Афины, Москва)\n')
    if haoha == 'Афины' or haoha == 'афины':
     import webbrowser
     webbrowser.open("https://openweathermap.org/city/264371")		
    elif haoha == 'Москва' or haoha == 'москва':
     import webbrowser
     webbrowser.open("https://openweathermap.org/city/524901")		
    else:
     print('В таком месте я погоду сказать не могу')

else:
    print('такого я не умею')
        
   
all = input('\nК сожалению у меня закончились фразы((\nНо вы можете перезагрузить сраницу, если хотите возобновить диалог))\n')


