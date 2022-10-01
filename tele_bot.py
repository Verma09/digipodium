from telegram.ext import 

token = "5662185208:AAF53nFWZeTohp5KEcGJIiIBLbwvfFKbjUg"

updater = telegram.ext.updater("5662185208:AAF53nFWZeTohp5KEcGJIiIBLbwvfFKbjUg", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    upadate.massage.reply_text("Hello! Welcome To My Telegram Bot")

def help(update, context):
    update.massage.reply-text(
        """
        /start -> Welcome to the channel
        /help -> this particuler massage
        /content -> About various playlist of Simplilearn
        /Python -> The first video from Python  playlist
        /SQl -> The first video from SQL playlist
        /java -> The firs video from java playlist
        /contact -> contact information 
        """
    )
def contant(update, context):
    update.massage.reply_text("We have various playlist of articals avilable")

def Python(update, context):
    update.massage.reply_text("tutorial link : https://youtu.be/Tm5u97I7OrM")

def SQL(update, context):
    update.massage.reply_text("https://youtu.be/AA7i2GcTGwU")

def Java(update, context):
    update.massage.reply_text("https://youtu.be/i6AZdFxTK9I")

def Contact(update, context):
    update.massage.reply_text("You can contact registered mail id provided on the website")

dispatcher.add.handler(telegram.ext.CommandHandler('start',start))
dispatcher.add.handler(telegram.ext.CommandHandler('start',Python))
dispatcher.add.handler(telegram.ext.CommandHandler('start',SQL))
dispatcher.add.handler(telegram.ext.CommandHandler('start',Java))
dispatcher.add.handler(telegram.ext.CommandHandler('start',contact))
dispatcher.add.handler(telegram.ext.CommandHandler('start',help))



updater.start_polling()
updater.idle()











    

