from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import *

comands = '/hi\n/help\n/time\n/calc\n/newyear'
async def hi_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!\n'
        'My name is PythonBot!\nEnter: /help')
async def help_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(comands)
async def time_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data_today = datetime.now().strftime('%d-%m-%Y %H:%M')
    await update.message.reply_text(f'{data_today}')
async def calc_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = eval(update.message.text.split()[1])
    await update.message.reply_text(f'{result}')
async def unknow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Простите, но я пока не знаю такой команды')
    await update.message.reply_text(f'Попробуйте одну из этих:\n{comands}')
async def days_under_new_year(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.now()
    new_year = datetime(2024,1,1)
    delta_days = new_year - today
    if delta_days.days % 10 == 1:
        word = 'день'
    elif delta_days.days % 10 > 1 and delta_days < 5:
        word = 'дня'
    else: word = 'дней'
    await update.message.reply_text(f'До нового года {delta_days.days} {word}!')

    
