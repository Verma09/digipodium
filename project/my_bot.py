from telegram.ext import *
import keys 

from news_bot_api import get_news

print('starting up bot...')


def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. Nice to meet you!')
    

def help_command(update, context):
    update.message.reply_text('Available Commands :-/start /help /hello /Howareyou /news Youtube Link =>https://www.youtube.com/ LinkedIn URL => \https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/ GeeksforGeeks URL => https://www.geeksforgeeks.org/ Your gmail link here (I am not\ giving mine one for security reasons)')
    
def gmail_url(Update, context):
    update.message.reply_text("Your gmail link here (I am not\ giving mine one for security reasons)")
          
def youtube_url(Update, context):
    update.message.reply_text("Youtube Link =>\https://www.youtube.com/")

def linkedIn_url(Update, context):
    update.message.reply_text("LinkedIn URL => \https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")
    
def geeks_url(Update, context):
    update.message.reply_text("GeeksforGeeks URL => https://www.geeksforgeeks.org/")
   
    
def custom_command(update, context):
    update.message.reply_text('This is custom command!')
    
def handle_response(text: str) -> str:
    if 'hello' in text.lower().strip():
        return 'Hey there!'
        
    if 'how are you' in text.lower().strip():
        return 'I am good, thanks!'
    
    if 'hi' in text.lower().strip():
        return 'Hey there!'
    
    
    if 'news' in text.lower().strip():
        return '📰 '+'\n📰 '.join(get_news())
    
   
   
    
    
    return 'Idk, try other query!'

def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''
    
    print(f'user ({update.message.chat.id}) says: "{text}" in: {message_type}')
    
    if message_type == 'group':
        if '@fun_03_bot' in text:
            new_text = text.replace('@fun_03_bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)
        
    update.message.reply_text(response)
    
def error(update, context):
    print(f'Update {update} caused error: {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    dp.add_handler(CommandHandler('youtube', youtube_url))
    dp.add_handler(CommandHandler('linkedin', linkedIn_url))
    dp.add_handler(CommandHandler('gmail', gmail_url))
    dp.add_handler(CommandHandler('geeks', geeks_url))

    

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
    
