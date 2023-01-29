from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import *

async def hi_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!\n'
        'My name is PythonBot!\nEnter: /help')
async def help_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/help\n/time\n/calc')
async def time_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data_today = datetime.now().strftime('%d-%m-%Y %H:%M')
    await update.message.reply_text(f'{data_today}')
async def calc_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = eval(update.message.text.split()[1])
    await update.message.reply_text(f'{result}')
    
