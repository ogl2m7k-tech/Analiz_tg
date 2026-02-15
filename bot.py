
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8395556440:AAEifvx1_0Xr9aIdv7db6Bpagr74tnbxbHE"

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💻 BORSA BUZZ borsa botuna hoş geldin!\n\n"
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
                                    "- /hacimtrend\n")

# Örnek komut: /derinlik THYAO
async def derinlik(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hisse = context.args[0].upper() if context.args else "THYAO"
    await update.message.reply_text(f"📈 {hisse} 25 Kademe Derinlik (Örnek veri)")

# Diğer örnek komutlar (şimdilik örnek mesaj)
async def akd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hisse = context.args[0].upper() if context.args else "THYAO"
    await update.message.reply_text(f"📊 {hisse} Aracı Kurum Dağılımı (Örnek veri)")

async def balina(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hisse = context.args[0].upper() if context.args else "THYAO"
    await update.message.reply_text(f"🐋 {hisse} Balina Avcısı (Örnek veri)")

async def pgc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hisse = context.args[0].upper() if context.args else "THYAO"
    await update.message.reply_text(f"💵 {hisse} Para Giriş/Çıkış (Örnek veri)")

# Telegram bot uygulaması
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Komutları ekle
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("derinlik", derinlik))
app.add_handler(CommandHandler("akd", akd))
app.add_handler(CommandHandler("balina", balina))
app.add_handler(CommandHandler("pgc", pgc))

# Botu başlat (polling ile)
app.run_polling()
