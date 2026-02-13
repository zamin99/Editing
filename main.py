import os
import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from urllib.parse import quote
import random

# =============================================
# 🔥 DEVELOPER CREDENTIALS - PRO WELCOME
# =============================================
DEVELOPER = "@SIGMAXZAMIN"
CHANNEL_USERNAME = "ZAMINTRICKS"
CHANNEL_LINK = "https://t.me/ZAMINTRICKS"
CHANNEL_NAME = "𝐙𝐀𝐌𝐈𝐍 𝐓𝐑𝐈𝐂𝐊𝐒"
BOT_VERSION = "𝐏𝐑𝐎 𝟐.𝟎.𝟎"
BOT_EMOJI = "🤖🔥"

# =============================================
# 🎬 EDITING APPS WITH DIRECT DOWNLOAD LINKS
# =============================================
DIRECT_APPS = {
    "capcut": {
        "name": "CapCut Pro",
        "url": "https://d.apkpure.com/b/APK/CapCut?version=latest",
        "direct": True
    },
    "capcut pro": {
        "name": "CapCut Pro",
        "url": "https://d.apkpure.com/b/APK/CapCut?version=latest",
        "direct": True
    },
    "picsart": {
        "name": "Picsart Pro",
        "url": "https://d.apkpure.com/b/APK/Picsart?version=latest",
        "direct": True
    },
    "picsart pro": {
        "name": "Picsart Pro",
        "url": "https://d.apkpure.com/b/APK/Picsart?version=latest",
        "direct": True
    },
    "pixelab": {
        "name": "PixelLab Pro",
        "url": "https://d.apkpure.com/b/APK/PixelLab?version=latest",
        "direct": True
    },
    "inshot": {
        "name": "InShot Pro",
        "url": "https://d.apkpure.com/b/APK/InShot?version=latest",
        "direct": True
    },
    "kinemaster": {
        "name": "KineMaster Pro",
        "url": "https://d.apkpure.com/b/APK/KineMaster?version=latest",
        "direct": True
    },
    "alight motion": {
        "name": "Alight Motion Pro",
        "url": "https://d.apkpure.com/b/APK/Alight%20Motion?version=latest",
        "direct": True
    },
    "lightroom": {
        "name": "Lightroom Pro",
        "url": "https://d.apkpure.com/b/APK/Lightroom?version=latest",
        "direct": True
    },
    "snapseed": {
        "name": "Snapseed Pro",
        "url": "https://d.apkpure.com/b/APK/Snapseed?version=latest",
        "direct": True
    },
    "canva": {
        "name": "Canva Pro",
        "url": "https://d.apkpure.com/b/APK/Canva?version=latest",
        "direct": True
    },
    "filmora": {
        "name": "Filmora Pro",
        "url": "https://d.apkpure.com/b/APK/Filmora?version=latest",
        "direct": True
    },
    "viva video": {
        "name": "VivaVideo Pro",
        "url": "https://d.apkpure.com/b/APK/VivaVideo?version=latest",
        "direct": True
    },
    "powerdirector": {
        "name": "PowerDirector Pro",
        "url": "https://d.apkpure.com/b/APK/PowerDirector?version=latest",
        "direct": True
    }
}

# =============================================
# 🚀 PRO WELCOME
# =============================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    first_name = user.first_name if user.first_name else "Bro"
    
    welcome = f"""
╔════════════════════════╗
║  {BOT_EMOJI} 𝐄𝐃𝐈𝐓𝐈𝐍𝐆 𝐏𝐑𝐎 {BOT_EMOJI}  ║
╚════════════════════════╝

Hello **{first_name}**! 👋

━━━━━━━━━━━━━━━━━━━━━
🔥 **DIRECT APK DOWNLOAD** 🔥
━━━━━━━━━━━━━━━━━━━━━

✅ **CapCut Pro** - Direct Link
✅ **Picsart Pro** - Direct Link  
✅ **PixelLab Pro** - Direct Link
✅ **InShot Pro** - Direct Link
✅ **KineMaster Pro** - Direct Link
✅ **Alight Motion Pro** - Direct Link
✅ **Lightroom Pro** - Direct Link
✅ **Snapseed Pro** - Direct Link

━━━━━━━━━━━━━━━━━━━━━
👑 **Developer**: `{DEVELOPER}`
📢 **Channel**: [{CHANNEL_NAME}]({CHANNEL_LINK})
━━━━━━━━━━━━━━━━━━━━━

💎 **App naam likho → Direct download start!**
`capcut pro`  `picsart`  `pixelab`  `inshot`
"""
    
    keyboard = [[InlineKeyboardButton("📢 JOIN CHANNEL", url=CHANNEL_LINK)]]
    await update.message.reply_text(welcome, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

# =============================================
# 🔍 DIRECT DOWNLOAD LINK BHEJO
# =============================================
async def direct_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower().strip()
    
    if len(query) < 2:
        await update.message.reply_text("❌ Kam se kam 2 letters likho!")
        return
    
    # Search in direct apps database
    found_app = None
    for key, app in DIRECT_APPS.items():
        if key in query:
            found_app = app
            break
    
    if found_app:
        # Direct download button - TAP KARTE HI DOWNLOAD SHURU!
        download_text = f"""
✅ **{found_app['name']}**

━━━━━━━━━━━━━━━━━━━━━
📥 **Neeche button tap karo**
📲 **APK Pure se direct download hoga**
━━━━━━━━━━━━━━━━━━━━━
👑 **Dev**: {DEVELOPER}
📢 **Channel**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━
        """
        
        keyboard = [[
            InlineKeyboardButton("📥 DIRECT DOWNLOAD NOW", url=found_app['url'])
        ]]
        
        await update.message.reply_text(
            download_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    else:
        # App not found - show available apps
        apps_list = "\n".join([f"• `{key}`" for key in DIRECT_APPS.keys()])
        
        not_found = f"""
❌ **App not found in database**

✅ **Available apps:**
{apps_list}

━━━━━━━━━━━━━━━━━━━━━
👨‍💻 **Dev**: {DEVELOPER}
📢 **Channel**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━

💡 **Type any app name from above list**
        """
        
        await update.message.reply_text(not_found, parse_mode='Markdown')

# =============================================
# 📢 ABOUT COMMAND
# =============================================
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = f"""
╔════════════════════════╗
║  🤖 BOT INFO 🤖       ║
╚════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━
👑 **Developer**: `{DEVELOPER}`
📢 **Channel**: @{CHANNEL_USERNAME}
🤖 **Version**: {BOT_VERSION}
━━━━━━━━━━━━━━━━━━━━━

✨ **Features**:
✅ Direct APK download links
✅ 15+ editing apps
✅ One tap download
✅ 100% working

━━━━━━━━━━━━━━━━━━━━━
⭐ Made by {DEVELOPER}
📢 Join @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━
    """
    
    keyboard = [[InlineKeyboardButton("📢 JOIN CHANNEL", url=CHANNEL_LINK)]]
    await update.message.reply_text(about_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

# =============================================
# 🚀 MAIN FUNCTION
# =============================================
def main():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not token:
        print("❌ Token not found!")
        return
    
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("developer", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, direct_download))
    
    print("✅ DIRECT DOWNLOAD BOT STARTED!")
    print(f"👑 Developer: {DEVELOPER}")
    print(f"📢 Channel: @{CHANNEL_USERNAME}")
    print("🔥 Direct APK links ready!")
    
    app.run_polling()

if __name__ == '__main__':
    main()
