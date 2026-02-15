from telegram.ext import Updater, CommandHandler

# Senin bot token
BOT_TOKEN = "8395556440:AAEifvx1_0Xr9aIdv7db6Bpagr74tnbxbHE"

# /start komutu
def start(update, context):
    update.message.reply_text(
        "💻 BORSA BUZZ borsa botuna hoş geldin!\n\n"
        "Kullanabileceğin komutlar:\n"
        "- /derinlik HISSE\n"
        "- /akd HISSE\n"
        "- /akd20 HISSE\n"
        "- /akdtarih HISSE\n"
        "- /kademe HISSE\n"
        "- /balina HISSE\n"
        "- /takas HISSE\n"
        "- /teorik HISSE\n"
        "- /pgc HISSE\n"
        "- /islem HISSE\n"
        "- /kurum\n"
        "- /bofa\n"
        "- /tera\n"
        "- /hacimtrend"
    )

# Örnek komutlar
def derinlik(update, context):
    hisse = context.args[0].upper() if context.args else "THYAO"
    update.message.reply_text(f"📈 {hisse} 25 Kademe Derinlik (Örnek veri)")

def akd(update, context):
    hisse = context.args[0].upper() if context.args else "THYAO"
    update.message.reply_text(f"📊 {hisse} Aracı Kurum Dağılımı (Örnek veri)")

def balina(update, context):
    hisse = context.args[0].upper() if context.args else "THYAO"
    update.message.reply_text(f"🐋 {hisse} Balina Avcısı (Örnek veri)")

def pgc(update, context):
    hisse = context.args[0].upper() if context.args else "THYAO"
    update.message.reply_text(f"💵 {hisse} Para Giriş/Çıkış (Örnek veri)")

# Updater ve handler ayarları
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

# Komutları ekle
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("derinlik", derinlik))
dp.add_handler(CommandHandler("akd", akd))
dp.add_handler(CommandHandler("balina", balina))
dp.add_handler(CommandHandler("pgc", pgc))

# Botu başlat
updater.start_polling()
updater.idle()
