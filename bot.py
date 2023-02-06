from telegram.ext import ApplicationBuilder,CommandHandler, MessageHandler, filters
from voice import textToFile

"""If you don't have a TOKEN, check @BotFather on telegram and follow instruction.
Create file token.txt in Main directory and post your TOKEN there""" 

# Open file with telegram's token and copy to program.
f_token = open("token.txt", 'r')
TOKEN = f_token.read()
f_token.close()

# Comands
async def startHandler(update, context):
    await update.message.reply_text("For Start, text me pls!")


async def helpHandler(update, context):
    await update.message.reply_text("""
            All commands:
            /start
            /help
""")
          
          
# reply text from massages to voice.
async def replyTextToVoice(update, context):
    fileName = textToFile(update.message.text, update.message.message_id)   
    await update.message.reply_voice(voice=open(fileName, "rb"))
    
def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(TOKEN).build()
    
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", startHandler))
    application.add_handler(CommandHandler("help", helpHandler))

    # Reply your text to speech
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, replyTextToVoice))


    
    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
    
