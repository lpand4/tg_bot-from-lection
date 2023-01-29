from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import spy as s
import random as r


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await s.log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await s.log(update, context)
    await update.message.reply_text(f'Time now is {datetime.datetime.now().time()}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await s.log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await s.log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])

    print(msg)
    await update.message.reply_text(f'{x} + {y} = {x + y}')
