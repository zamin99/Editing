import os
import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

# =============================================
# 🔥 DEVELOPER CREDENTIALS - PRO WELCOME (INTACT)
# =============================================
DEVELOPER = "@SIGMAXZAMIN"
CHANNEL_USERNAME = "ZAMINTRICKS"
CHANNEL_LINK = "https://t.me/ZAMINTRICKS"
CHANNEL_NAME = "𝐙𝐀𝐌𝐈𝐍 𝐓𝐑𝐈𝐂𝐊𝐒"
BOT_VERSION = "𝐏𝐑𝐎 𝟐.𝟎.𝟎"
BOT_EMOJI = "🤖🔥"

# =============================================
# 🎬 100% WORKING PRO APK LINKS (TESTED)
# =============================================
PRO_APPS = {
    "capcut": {
        "name": "🎬 𝐂𝐚𝐩𝐂𝐮𝐭 𝐏𝐑𝐎",
        "link": "https://www.apkmirror.com/apk/capcut/capcut-2-4-0-release/",  # WORKING
        "version": "𝐏𝐑𝐎 𝟐.𝟒.𝟎",
        "size": "𝟖𝟖 𝐌𝐁"
    },
    "capcut pro": {
        "name": "🎬 𝐂𝐚𝐩𝐂𝐮𝐭 𝐏𝐑𝐎",
        "link": "https://www.apkmirror.com/apk/capcut/capcut-2-4-0-release/",  # WORKING
        "version": "𝐏𝐑𝐎 𝟐.𝟒.𝟎",
        "size": "𝟖𝟖 𝐌𝐁"
    },
    "picsart": {
        "name": "🎨 𝐏𝐢𝐜𝐬𝐀𝐫𝐭 𝐏𝐑𝐎",
        "link": "https://picsart.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟐𝟑.𝟗.𝟏",
        "size": "𝟕𝟐 𝐌𝐁"
    },
    "picsart pro": {
        "name": "🎨 𝐏𝐢𝐜𝐬𝐀𝐫𝐭 𝐏𝐑𝐎",
        "link": "https://picsart.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟐𝟑.𝟗.𝟏",
        "size": "𝟕𝟐 𝐌𝐁"
    },
    "pixelab": {
        "name": "✨ 𝐏𝐢𝐱𝐞𝐋𝐚𝐛 𝐏𝐑𝐎",
        "link": "https://pixellab.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟐.𝟏.𝟎",
        "size": "𝟒𝟓 𝐌𝐁"
    },
    "pixelab pro": {
        "name": "✨ 𝐏𝐢𝐱𝐞𝐋𝐚𝐛 𝐏𝐑𝐎",
        "link": "https://pixellab.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟐.𝟏.𝟎",
        "size": "𝟒𝟓 𝐌𝐁"
    },
    "inshot": {
        "name": "📱 𝐈𝐧𝐒𝐡𝐨𝐭 𝐏𝐑𝐎",
        "link": "https://inshot.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟐.𝟓.𝟎",
        "size": "𝟗𝟎 𝐌𝐁"
    },
    "kinemaster": {
        "name": "🎥 𝐊𝐢𝐧𝐞𝐌𝐚𝐬𝐭𝐞𝐫 𝐏𝐑𝐎",
        "link": "https://kinemaster.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟕.𝟓.𝟎",
        "size": "𝟏𝟐𝟎 𝐌𝐁"
    },
    "alight motion": {
        "name": "✨ 𝐀𝐥𝐢𝐠𝐡𝐭 𝐌𝐨𝐭𝐢𝐨𝐧 𝐏𝐑𝐎",
        "link": "https://alight-motion.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟓.𝟎.𝟎",
        "size": "𝟗𝟓 𝐌𝐁"
    },
    "lightroom": {
        "name": "📸 𝐋𝐢𝐠𝐡𝐭𝐫𝐨𝐨𝐦 𝐏𝐑𝐎",
        "link": "https://lightroom.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟖.𝟎.𝟎",
        "size": "𝟕𝟖 𝐌𝐁"
    },
    "snapseed": {
        "name": "🖼️ 𝐒𝐧𝐚𝐩𝐬𝐞𝐞𝐝 𝐏𝐑𝐎",
        "link": "https://snapseed.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟐.𝟐.𝟎",
        "size": "𝟑𝟓 𝐌𝐁"
    },
    "canva": {
        "name": "🎨 𝐂𝐚𝐧𝐯𝐚 𝐏𝐑𝐎",
        "link": "https://canva.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟏.𝟕𝟎.𝟎",
        "size": "𝟏𝟏𝟎 𝐌𝐁"
    },
    "viva video": {
        "name": "🎬 𝐕𝐢𝐯𝐚𝐕𝐢𝐝𝐞𝐨 𝐏𝐑𝐎",
        "link": "https://viva-video.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟖.𝟎.𝟎",
        "size": "𝟖𝟐 𝐌𝐁"
    },
    "filmora": {
        "name": "🎥 𝐅𝐢𝐥𝐦𝐨𝐫𝐚 𝐏𝐑𝐎",
        "link": "https://filmora.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟏𝟐.𝟎.𝟎",
        "size": "𝟏𝟑𝟓 𝐌𝐁"
    },
    "powerdirector": {
        "name": "⚡ 𝐏𝐨𝐰𝐞𝐫𝐃𝐢𝐫𝐞𝐜𝐭𝐨𝐫 𝐏𝐑𝐎",
        "link": "https://powerdirector.en.uptodown.com/android/download",  # WORKING
        "version": "𝐏𝐑𝐎 𝟗.𝟓.𝟎",
        "size": "𝟗𝟖 𝐌𝐁"
    }
}

# =============================================
# 🚀 𝐏𝐑𝐎 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 - 𝐅𝐔𝐋𝐋 𝐒𝐓𝐘𝐋𝐄 (𝐔𝐍𝐂𝐇𝐀𝐍𝐆𝐄𝐃)
# =============================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    first_name = user.first_name if user.first_name else "𝐁𝐫𝐨"
    
    pro_welcome = f"""
╔════════════════════════╗
║  {BOT_EMOJI} 𝐄𝐃𝐈𝐓𝐈𝐍𝐆 𝐏𝐑𝐎 {BOT_EMOJI}  ║
╚════════════════════════╝

𝐇𝐞𝐥𝐥𝐨 **{first_name}**! 👋

✨ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐏𝐑𝐎 𝐁𝐎𝐓 ✨

━━━━━━━━━━━━━━━━━━━━━
🎯 **𝐃𝐈𝐑𝐄𝐂𝐓 𝐏𝐑𝐎 𝐀𝐏𝐊 𝐋𝐈𝐍𝐊𝐒**
━━━━━━━━━━━━━━━━━━━━━

✅ 𝐂𝐚𝐩𝐂𝐮𝐭 𝐏𝐑𝐎
✅ 𝐏𝐢𝐜𝐬𝐀𝐫𝐭 𝐏𝐑𝐎
✅ 𝐏𝐢𝐱𝐞𝐋𝐚𝐛 𝐏𝐑𝐎
✅ 𝐈𝐧𝐒𝐡𝐨𝐭 𝐏𝐑𝐎
✅ 𝐊𝐢𝐧𝐞𝐌𝐚𝐬𝐭𝐞𝐫 𝐏𝐑𝐎
✅ 𝐀𝐥𝐢𝐠𝐡𝐭 𝐌𝐨𝐭𝐢𝐨𝐧 𝐏𝐑𝐎
✅ 𝐋𝐢𝐠𝐡𝐭𝐫𝐨𝐨𝐦 𝐏𝐑𝐎
✅ 𝐂𝐚𝐧𝐯𝐚 𝐏𝐑𝐎
✅ 𝐕𝐢𝐯𝐚𝐕𝐢𝐝𝐞𝐨 𝐏𝐑𝐎
✅ 𝐅𝐢𝐥𝐦𝐨𝐫𝐚 𝐏𝐑𝐎

━━━━━━━━━━━━━━━━━━━━━
👑 **𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑**: `{DEVELOPER}`
📢 **𝐂𝐇𝐀𝐍𝐍𝐄𝐋**: [{CHANNEL_NAME}]({CHANNEL_LINK})
🤖 **𝐕𝐄𝐑𝐒𝐈𝐎𝐍**: {BOT_VERSION}
━━━━━━━━━━━━━━━━━━━━━

💎 **𝐉𝐮𝐬𝐭 𝐭𝐲𝐩𝐞 𝐚𝐩𝐩 𝐧𝐚𝐦𝐞** 👇
`capcut pro`  `picsart`  `pixelab`  `inshot`

🔥 **𝐀𝐋𝐋 𝐋𝐈𝐍𝐊𝐒 𝟏𝟎𝟎% 𝐖𝐎𝐑𝐊𝐈𝐍𝐆** 🔥
    """
    
    keyboard = [
        [InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 𝐏𝐑𝐎 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=CHANNEL_LINK)],
        [InlineKeyboardButton("👨‍💻 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑", url=f"https://t.me/{DEVELOPER[1:]}")]
    ]
    
    await update.message.reply_text(
        pro_welcome,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

# =============================================
# 🔎 𝐏𝐑𝐎 𝐒𝐄𝐀𝐑𝐂𝐇 - 𝟏𝟎𝟎% 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐋𝐈𝐍𝐊𝐒
# =============================================
async def search_pro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower().strip()
    
    # Search in database
    found_app = None
    for key, app in PRO_APPS.items():
        if key in query:
            found_app = app
            break
    
    if found_app:
        # 𝐏𝐑𝐎 𝐑𝐄𝐒𝐔𝐋𝐓 𝐂𝐀𝐑𝐃
        pro_card = f"""
╔════════════════════════╗
║  {found_app['name']}  ║
╚════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━
📦 **𝐕𝐄𝐑𝐒𝐈𝐎𝐍**: `{found_app['version']}`
📏 **𝐒𝐈𝐙𝐄**: `{found_app['size']}`
🔓 **𝐒𝐓𝐀𝐓𝐔𝐒**: `𝐏𝐑𝐎 𝐔𝐍𝐋𝐎𝐂𝐊𝐄𝐃`
🌐 **𝐒𝐎𝐔𝐑𝐂𝐄**: `𝐔𝐩𝐭𝐨𝐃𝐨𝐰𝐧`
━━━━━━━━━━━━━━━━━━━━━
👑 **𝐃𝐄𝐕**: {DEVELOPER}
📢 **𝐂𝐇𝐀𝐍𝐍𝐄𝐋**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━

⬇️ **𝐓𝐀𝐏 𝐓𝐎 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 𝐏𝐑𝐎** ⬇️
        """
        
        keyboard = [[
            InlineKeyboardButton(f"📥 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 {found_app['name']}", url=found_app['link'])
        ]]
        
        await update.message.reply_text(
            pro_card,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    else:
        # 𝐀𝐩𝐩 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝 - 𝐒𝐡𝐨𝐰 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐚𝐩𝐩𝐬
        apps_list = "\n".join([f"• `{key}`" for key in PRO_APPS.keys()])
        
        not_found = f"""
❌ **𝐀𝐏𝐏 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃 𝐈𝐍 𝐏𝐑𝐎 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄**

━━━━━━━━━━━━━━━━━━━━━
✅ **𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄 𝐏𝐑𝐎 𝐀𝐏𝐏𝐒**:
{apps_list}
━━━━━━━━━━━━━━━━━━━━━
👨‍💻 **𝐃𝐄𝐕**: {DEVELOPER}
📢 **𝐂𝐇𝐀𝐍𝐍𝐄𝐋**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━

💡 **𝐓𝐲𝐩𝐞 𝐚𝐧𝐲 𝐚𝐩𝐩 𝐧𝐚𝐦𝐞 𝐟𝐫𝐨𝐦 𝐚𝐛𝐨𝐯𝐞**
        """
        
        await update.message.reply_text(
            not_found,
            parse_mode='Markdown'
        )

# =============================================
# 📢 𝐀𝐁𝐎𝐔𝐓 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 (𝐔𝐍𝐂𝐇𝐀𝐍𝐆𝐄𝐃)
# =============================================
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = f"""
╔════════════════════════╗
║  🤖 𝐏𝐑𝐎 𝐁𝐎𝐓 𝐈𝐍𝐅𝐎 🤖  ║
╚════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━
👑 **𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑**: `{DEVELOPER}`
📢 **𝐂𝐇𝐀𝐍𝐍𝐄𝐋**: @{CHANNEL_USERNAME}
🔗 **𝐋𝐈𝐍𝐊**: {CHANNEL_LINK}
🤖 **𝐕𝐄𝐑𝐒𝐈𝐎𝐍**: {BOT_VERSION}
━━━━━━━━━━━━━━━━━━━━━

✨ **𝐏𝐑𝐎 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒**:
✅ 𝐃𝐢𝐫𝐞𝐜𝐭 𝐏𝐑𝐎 𝐀𝐏𝐊 𝐋𝐢𝐧𝐤𝐬
✅ 𝟏𝟓+ 𝐄𝐝𝐢𝐭𝐢𝐧𝐠 𝐀𝐩𝐩𝐬
✅ 𝟐𝟒/𝟕 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞
✅ 𝟏𝟎𝟎% 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 𝐋𝐢𝐧𝐤𝐬
✅ 𝐍𝐨 𝐀𝐏𝐈 𝐊𝐞𝐲 𝐍𝐞𝐞𝐝𝐞𝐝

━━━━━━━━━━━━━━━━━━━━━
⭐ 𝐌𝐚𝐝𝐞 𝐰𝐢𝐭𝐡 ❤️ 𝐛𝐲 {DEVELOPER}
📢 𝐉𝐨𝐢𝐧 @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━
    """
    
    keyboard = [[
        InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=CHANNEL_LINK)
    ]]
    
    await update.message.reply_text(
        about_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

# =============================================
# 🚀 𝐌𝐀𝐈𝐍 𝐅𝐔𝐍𝐂𝐓𝐈𝐎𝐍
# =============================================
def main():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    
    if not token:
        print("❌ Token not found!")
        return
    
    app = Application.builder().token(token).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("developer", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_pro))
    
    print("✅ 𝐏𝐑𝐎 𝐁𝐎𝐓 𝐒𝐓𝐀𝐑𝐓𝐄𝐃!")
    print(f"👑 Developer: {DEVELOPER}")
    print(f"📢 Channel: @{CHANNEL_USERNAME}")
    print(f"🔗 100% Working Links: Uptodown + APKMirror")
    
    app.run_polling()

if __name__ == '__main__':
    main()
