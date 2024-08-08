import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Sabit kod listesi
codes = [
    "BIKE-0PZ-7DPC-05ED-PD4",
    "BIKE-0PF-4DYD-0NEN-KCP",
    # Daha fazla kod ekleyebilirsiniz
]

# Kullanılan kodları saklamak için bir liste
used_codes = []

# /start komutu için işlev
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Reklamı İzle", callback_data='watch_ad')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Kod almak için reklamı izleyin.', reply_markup=reply_markup)

# CallbackQuery işleyicisi
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'watch_ad':
        if codes:
            code = codes.pop(0)  # İlk kodu alın
            used_codes.append(code)  # Kullanılan kodları sakla
            query.edit_message_text(text=f"Reklam izlediğiniz için teşekkürler! İşte kodunuz: {code}")
        else:
            query.edit_message_text(text="Üzgünüz, tüm kodlar tükendi.")

def main():
    # Bot tokenınızı çevresel değişkenden alın
    updater = Updater(os.getenv("TELEGRAM_BOT_TOKEN"), use_context=True)
    dispatcher = updater.dispatcher

    # Komut işleyicileri
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Botu başlatma
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
          
