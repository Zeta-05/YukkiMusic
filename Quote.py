from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store user states
user_last_message = {}

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    last_message_id = user_last_message.get(user_id)

    if last_message_id:
        # Reply to the last message sent by the user
        update.message.reply_text(
            'Welcome back! Here is the message you sent before:',
            reply_to_message_id=last_message_id
        )
    else:
        # If no last message exists, just send a welcome message
        update.message.reply_text('Welcome! This is your first message.')

def track_last_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    # Store the last message ID for the user
    user_last_message[user_id] = update.message.message_id

    # Echo back the message (you can customize this as needed)
    update.message.reply_text(f'You said: {update.message.text}')

def main() -> None:
    updater = Updater("7642320220:AAEDsTucFRB95md7L_eSUx_Pr7NvDapHwmA")

    # Handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, track_last_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
