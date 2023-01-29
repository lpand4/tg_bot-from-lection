from bot_commands import *


app = ApplicationBuilder().token("5786635957:AAGVAyxWtno9CyfUNFFau6Cp0wNKerXJDC4").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))


# app.add_handler(CommandHandler("candy", candy()))





print('server rabotaet')
app.run_polling()

