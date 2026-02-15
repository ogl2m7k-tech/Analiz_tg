from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Senin verdiğin token
BOT_TOKEN = "8395556440:AAEifvx1_0Xr9aIdv7db6Bpagr74tnbxbHE"

# /start komutu
def start(update: Update, context: CallbackContext):
    update.message.reply_text("💻 BORSA BUZZ borsa botuna hoş geldin!")

# /derinlik komutu örnek
def derinlik(update: Update, context: CallbackContext):
    if context.args:
        hisse = context.args[0].upper()
    else:
        hisse = "THYAO"
    update.message.reply_text(f"📈 {hisse} 25 Kademe Derinlik (Örnek veri)")

# Telegram updater ve handler ayarları
updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("derinlik", derinlik))

# Botu başlat
updater.start_polling()
updater.idle()
