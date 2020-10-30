
import discord
import config
from discord.ext import commands
import numexpr as ne


bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def calc(self, nam1):  # Ввод переменных

    # логика калькулятора
    try:
        rep = '÷'
        for item in rep:
            if item in nam1:
                nam1 = nam1.replace(item, '/')
        rep1 = '×'
        for item in rep1:
            if item in nam1:
                nam1 = nam1.replace(item, '*')
        rep2 = ' '
        for item in rep2:
            if item in nam1:
                nam1 = nam1.replace(item, '')

        c = ne.evaluate(nam1)

        await self.send(nam1 + ' = ' + str(c))  # отправляем обратно аргумент

        await self.send('\nЯ полезный!!!')
    except ZeroDivisionError:
        await self.send("Я тебя сейчас сам на 0 поделю!!! >_<'")
    except ValueError:
        await self.send("А можно я цифры считать буду? T_T")
    except KeyError:
        await self.send("Моя не понимать что значит " + num1 + "! Ты точно все правильно ввел?")


@bot.command()
async def time(self, uname):
    whu = '{0.author}'.format(self)
    import time # Импорт библиотеки Time
    import config

    named_tuple = time.localtime() # получить struct_time
    time_string = time.strftime("_%d_%m_%Y", named_tuple)

    # Timezine
    msk = time.ctime(time.time())
    yak = time.ctime(time.mktime(time.localtime()) + (3600 * 6))
    buh = time.ctime(time.mktime(time.localtime()) - 3600)

    # пулл участников

    try:
        with open('data/заявки_от' + time_string + '.txt', 'a') as f:
            f.write ('Запрос от пользователя: '+ whu + ' ' + msk + '. Запрос на: ' + uname + '\n')

    except UnicodeEncodeError:
        with open('data/заявки_от' + time_string + '.txt', 'a') as f:
            f.write ('Запрос от пользователя: '+ 'Soda по ходу' + ' ' + msk + '. Запрос на: ' + uname + '\n')
    # Определение Timezone
    try:
        if config.tz[uname] == 'UTC +3 // Moscow':
            await self.send("Часовой пояс " + uname + ' ' + config.tz[uname] + '!\n' + msk)
        elif config.tz[uname] == 'UTC +3 // Minsk':
            await self.send("Часовой пояс " + uname + ' ' + config.tz[uname] + '!\n' + msk)
        elif config.tz[uname] == 'UTC +9 // Yakutsk':
            await self.send("Часовой пояс " + uname + ' ' + config.tz[uname] + '!\n' + yak)
        elif config.tz[uname] == 'UTC +2 // Румыния, Бухарест':
            await self.send("Часовой пояс " + uname + ' ' + config.tz[uname] + '!\n' + buh)
    except KeyError:
        await self.send("Часовой пояс " + uname + ' не внесен в базу.\nВы можете отправить запрос на внесение в базу командой !add "Ник и ваш часовой пояс". Желательно указывать UTC\nПример: !add Vasya/UTC+4.\nИли обратитесь в ЛС к Reinkor_Lor за помощью!')
    except UnicodeEncodeError:
        await self.send("Я не могу осознать Ваш никнейм или в нем есть не знакомые мне символы! Но я стараюсь.")


@bot.command()
async def add(self, *fuck):
    import config as con
    import time
    whu = '{0.author}'.format(self)

    msk = time.ctime(time.time())
    named_tuple = time.localtime() # получить struct_time
    time_string = time.strftime("_%d_%m_%Y", named_tuple)

    zv = str(fuck)

    with open('data/заявки_от' + time_string + '.txt', 'a') as f:
        f.write ('Запрос на добавление пользователя: '+ zv + ' // ' + msk + '. От: ' + whu + '\n')

    await self.send("Запрос на добавление отправлен!!!\nАдминистрация уже спешит на проверку!")



bot.run(config.REIN)
