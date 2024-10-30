
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store the last message ID for each user
user_last_message = {}

def track_last_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    # Store the last message ID for the user
    user_last_message[user_id] = update.message.message_id

    # Reply with a quote of the user's message
    update.message.reply_text(
        f'You said: {update.message.text}',
        reply_to_message_id=update.message.message_id
    )

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    last_message_id = user_last_message.get(user_id)

    if last_message_id:
        # Quote the last message sent by the user
        update.message.reply_text(
            'Welcome back! Here is the message you sent before:',
            reply_to_message_id=last_message_id
        )
    else:
        # First interaction, so no message to quote
        update.message.reply_text(
            'Welcome! This is your first interaction. Please send me a message.'
        )

def main() -> None:
    updater = Updater("YOUR_TOKEN")

    # Handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, track_last_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
