import random
import telebot
from db import show_notes_from_db, save_data, delete_note_from_db

API_TOKEN = "6815886462:AAEDGZykTdcchF7gwp6qWEzJJT0xBY-4YTQ"
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start", "help"])
def start_help(message: telebot.types.Message):
    text = "Привет! Я бот для заметок!\n\n" \
           f"Список команд:\n\n" \
           f"/show_note - показать заметки (показывает случайную заметку из таблицы)\n\n" \
           f"/delete_note - удалить заметки (удаляет заметку, если ее номер превышает 15)\n\n"\
           "/ - чтобы сохранить заметку, напиши номер и саму заметку через запятую между ними\n"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show_note"])
def show_note(message: telebot.types.Message):
    notes = show_notes_from_db()
    note = random.choice(notes)
    bot.send_message(message.chat.id, text=f"Номер заметки: {note[1]}, заметка: {note[2]}")


@bot.message_handler(commands=["delete_note"])
def delete_note(message: telebot.types.Message, note_id=None):
    delete_note_from_db(note_id)
    bot.send_message(message.chat.id, text=f"Заметка удалена")


@bot.message_handler()
def add_note(message: telebot.types.Message):
    note_id_note = message.text.split(",")

    if len(note_id_note) == 2:
        note_id = note_id_note[0]
        note = note_id_note[1]
        bot.send_message(message.chat.id, f"Номер заметки: {note_id}, Заметка: {note}")
        save_data(note_id=note_id, note=note)
        bot.send_message(message.chat.id, "Заметка сохранена")
    else:
        bot.send_message(message.chat.id, "Неправильное оформление заметки")


print("Бот запущен")
bot.infinity_polling()