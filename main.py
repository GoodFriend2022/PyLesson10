from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from comand_bot import *
from datetime import *

TOKEN = "5923800644:AAHGyd3Bwtb0YR1eXoBjjRkXuTyoH4711fg"
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hi", hi_comand))
app.add_handler(CommandHandler("help", help_comand))
app.add_handler(CommandHandler("time", time_comand))
app.add_handler(CommandHandler("calc", calc_comand))
app.add_handler(CommandHandler("newyear", days_under_new_year))




app.add_handler(MessageHandler(filters.Command(False), unknow))

app.run_polling()
