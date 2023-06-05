from aiogram import executor # Подключаем модуль библиотеки aiogramm, необходимый для запуска бота
import bot # импортируем бота


if __name__ == '__main__':
    executor.start_polling(bot.dp, skip_updates=True) #Запускаем бота, все сообщения, написанные боту до запуска, будут проигнорированы
