import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot("введите ваш токен")

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.reply_to(message, "Привет! Я чат бот, который будет напоминать тебе тренироваться и правильно питаться!")
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=["help"])
def help_message(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Запустить бота и начать получать напоминания\n"
        "/help - Показать список команд\n"
        "/facttraining - Случайный факт о тренировках\n"
        "/facteat - Случайный факт о правильном питании\n"
    )
    bot.reply_to(message, help_text)


@bot.message_handler(commands=["facttraining"])
def facttraining_message(message):
    facts = ["** Регулярные тренировки и сбалансированное питание значительно повышают производительность и выносливость футболистов на поле.",
            "** Сильные и гибкие мышцы, развитые благодаря регулярным тренировкам, помогают стабилизировать суставы и предотвращают возникновение травм. Специальные упражнения на растяжку и укрепление мышц снижают риск мышечных растяжений и других травм.",
            "** Физическая активность способствует выделению эндорфинов, которые улучшают настроение и снижают уровень стресса. Регулярные тренировки также улучшают сон, что важно для психического восстановления и концентрации."]
    random_training = random.choice(facts)
    bot.reply_to(message, f"Посмотри факт о тренировках{random_training}")


@bot.message_handler(commands=["facteat"])
def facteat_message(message):
    facts = ["** Правильное питание обеспечивает организм необходимыми питательными веществами, такими как углеводы для энергии, белки для восстановления мышц и жиры для длительной энергии. Это помогает поддерживать высокий уровень энергии на протяжении всей игры и ускоряет восстановление после интенсивных физических нагрузок.",
            "** Питательные вещества, такие как кальций и витамин D, важны для здоровья костей, а белки и аминокислоты способствуют восстановлению тканей. Адекватное гидратация также предотвращает мышечные судороги и другие связанные с обезвоживанием травмы.",
            "** Определенные питательные вещества, такие как омега-3 жирные кислоты, антиоксиданты и витамины группы B, поддерживают здоровье мозга и когнитивные функции. Это помогает улучшить концентрацию, реакцию и принятие решений на поле."]
    random_eat = random.choice(facts)
    bot.reply_to(message, f"Посмотри факт о правильной еде{random_eat}")
def send_reminders (chat_id):
    first_rem = "02:30"
    second_rem = "14:00"
    third_rem = "16:30"
    end_rem = "18:42"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem:
            bot.send_message(chat_id, "Напоминание - пора завтракать ")
            time.sleep(61)
        elif now == second_rem:
            bot.send_message(chat_id, "Напоминание - пора обедать")
            time.sleep(61)
        elif now == third_rem:
            bot.send_message(chat_id, "Напоминание - пора тренироваться")
            time.sleep(61)
        elif now == end_rem:
            bot.send_message(chat_id, "Напоминание - прием ужинать")
            time.sleep(61)
        time.sleep(1)
bot.polling(none_stop=True)