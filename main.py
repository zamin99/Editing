import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from urllib.parse import quote

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
# 🎬 SIRF EDITING APPS KEYWORDS
# =============================================
EDITING_KEYWORDS = [
    "capcut", "picsart", "pixelab", "inshot", "kinemaster",
    "alight motion", "viva video", "powerdirector", "filmora",
    "snapseed", "lightroom", "canva", "photofox", "videoleap",
    "remini", "vsco", "pixlr", "touchretouch", "beautyplus"
]

# =============================================
# 🚀 PRO WELCOME - FULL STYLE
# =============================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    first_name = user.first_name if user.first_name else "𝐁𝐫𝐨"
    
    welcome = f"""
╔════════════════════════╗
║  {BOT_EMOJI} 𝐄𝐃𝐈𝐓𝐈𝐍𝐆 𝐏𝐑𝐎 {BOT_EMOJI}  ║
╚════════════════════════╝

𝐇𝐞𝐥𝐥𝐨 **{first_name}**! 👋

✨ 𝐀𝐏𝐊𝐏𝐮𝐫𝐞 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭 ✨

━━━━━━━━━━━━━━━━━━━━━
🔍 **𝐊𝐚𝐢𝐬𝐞 𝐊𝐚𝐦 𝐊𝐚𝐫𝐭𝐚 𝐇𝐚𝐢?**
━━━━━━━━━━━━━━━━━━━━━

1️⃣ 𝐀𝐚𝐩 𝐞𝐝𝐢𝐭𝐢𝐧𝐠 𝐚𝐩𝐩 𝐤𝐚 𝐧𝐚𝐚𝐦 𝐥𝐢𝐤𝐡𝐨
2️⃣ 𝐁𝐨𝐭 𝐀𝐏𝐊𝐏𝐮𝐫𝐞 𝐤𝐚 𝐥𝐢𝐧𝐤 𝐛𝐚𝐧𝐚𝐞𝐠𝐚
3️⃣ 𝐀𝐚𝐩 𝐭𝐚𝐩 𝐤𝐚𝐫𝐨 → 𝐀𝐏𝐊𝐏𝐮𝐫𝐞 𝐤𝐡𝐮𝐥𝐞𝐠𝐚
4️⃣ 𝐕𝐡𝐚𝐚𝐧 𝐬𝐞 𝐝𝐢𝐫𝐞𝐜𝐭 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐤𝐚𝐫𝐨

━━━━━━━━━━━━━━━━━━━━━
✅ **𝐒𝐢𝐫𝐟 𝐄𝐝𝐢𝐭𝐢𝐧𝐠 𝐀𝐩𝐩𝐬 𝐤𝐚 𝐬𝐞𝐚𝐫𝐜𝐡 𝐡𝐨𝐠𝐚**
━━━━━━━━━━━━━━━━━━━━━

👑 **𝐃𝐄𝐕**: `{DEVELOPER}`
📢 **𝐂𝐇𝐀𝐍𝐍𝐄𝐋**: [{CHANNEL_NAME}]({CHANNEL_LINK})
🤖 **𝐕𝐄𝐑𝐒𝐈𝐎𝐍**: {BOT_VERSION}
━━━━━━━━━━━━━━━━━━━━━

💎 **𝐀𝐩𝐩 𝐧𝐚𝐚𝐦 𝐥𝐢𝐤𝐡𝐨 👇**
`capcut pro`  `picsart`  `pixelab`  `inshot`
    """
    
    keyboard = [[InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=CHANNEL_LINK)]]
    await update.message.reply_text(welcome, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

# =============================================
# 🔎 EDITING APP CHECK KARO
# =============================================
def is_editing_app(query):
    """Check karo ki user ne editing app likha ya nahi"""
    query_lower = query.lower()
    for keyword in EDITING_KEYWORDS:
        if keyword in query_lower:
            return True
    return False

# =============================================
# 🔍 APKPURE SEARCH LINK BANAO
# =============================================
async def search_apkpure(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    
    # Check for empty query
    if len(query) < 2:
        await update.message.reply_text("❌ **Kam se kam 2 letters likho!**", parse_mode='Markdown')
        return
    
    # SIRF EDITING APPS ALLOWED
    if not is_editing_app(query):
        editing_list = "\n".join([f"• `{k}`" for k in EDITING_KEYWORDS[:15]])
        not_editing = f"""
❌ **𝐘𝐞𝐡 𝐞𝐝𝐢𝐭𝐢𝐧𝐠 𝐚𝐩𝐩 𝐧𝐚𝐡𝐢 𝐡𝐚𝐢!**

━━━━━━━━━━━━━━━━━━━━━
✅ **𝐒𝐢𝐫𝐟 𝐲𝐞𝐡 𝐚𝐩𝐩𝐬 𝐚𝐥𝐥𝐨𝐰𝐞𝐝 𝐡𝐚𝐢𝐧:**

{editing_list}
━━━━━━━━━━━━━━━━━━━━━
👨‍💻 **𝐃𝐄𝐕**: {DEVELOPER}
📢 **𝐂𝐇𝐀𝐍𝐍𝐄𝐋**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━

💡 **𝐊𝐨𝐢 𝐞𝐝𝐢𝐭𝐢𝐧𝐠 𝐚𝐩𝐩 𝐤𝐚 𝐧𝐚𝐚𝐦 𝐥𝐢𝐤𝐡𝐨**
        """
        await update.message.reply_text(not_editing, parse_mode='Markdown')
        return
    
    # ✅ EDITING APP HAI - APKPURE SEARCH LINK BANAO
    search_query = quote(query)
    apkpure_url = f"https://apkpure.com/search?q={search_query}"
    
    # PRO RESULT CARD
    result_text = f"""
╔════════════════════════╗
║  🔍 𝐀𝐏𝐊𝐏𝐮𝐫𝐞 𝐒𝐄𝐀𝐑𝐂𝐇  ║
╚════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━
📱 **𝐀𝐩𝐩**: `{query}`
🌐 **𝐒𝐨𝐮𝐫𝐜𝐞**: `APKPure.com`
━━━━━━━━━━━━━━━━━━━━━

✅ **𝐘𝐞𝐡 𝐞𝐝𝐢𝐭𝐢𝐧𝐠 𝐚𝐩𝐩 𝐡𝐚𝐢!**
⬇️ **𝐍𝐢𝐜𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧 𝐭𝐚𝐩 𝐤𝐚𝐫𝐨**

━━━━━━━━━━━━━━━━━━━━━
👑 **𝐃𝐄𝐕**: {DEVELOPER}
📢 **𝐂𝐇𝐀𝐍𝐍𝐄𝐋**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━
    """
    
    keyboard = [[
        InlineKeyboardButton("🔍 𝐀𝐏𝐊𝐏𝐮𝐫𝐞 𝐩𝐞 𝐬𝐞𝐚𝐫𝐜𝐡 𝐤𝐚𝐫𝐨", url=apkpure_url)
    ]]
    
    await update.message.reply_text(
        result_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

# =============================================
# 📢 ABOUT COMMAND
# =============================================
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = f"""
╔════════════════════════╗
║  🤖 𝐁𝐎𝐓 𝐈𝐍𝐅𝐎 🤖      ║
╚════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━
👑 **𝐃𝐄𝐕**: `{DEVELOPER}`
📢 **𝐂𝐇𝐀𝐍𝐍𝐄𝐋**: @{CHANNEL_USERNAME}
🤖 **𝐕𝐄𝐑𝐒𝐈𝐎𝐍**: {BOT_VERSION}
━━━━━━━━━━━━━━━━━━━━━

✨ **𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒**:
✅ 𝐒𝐢𝐫𝐟 𝐞𝐝𝐢𝐭𝐢𝐧𝐠 𝐚𝐩𝐩𝐬
✅ 𝐀𝐏𝐊𝐏𝐮𝐫𝐞 𝐬𝐞𝐚𝐫𝐜𝐡 𝐥𝐢𝐧𝐤
✅ 𝟏𝟎𝟎% 𝐰𝐨𝐫𝐤𝐢𝐧𝐠
✅ 𝐍𝐨 𝐬𝐜𝐫𝐚𝐩𝐢𝐧𝐠

━━━━━━━━━━━━━━━━━━━━━
⭐ 𝐌𝐚𝐝𝐞 𝐰𝐢𝐭𝐡 ❤️ 𝐛𝐲 {DEVELOPER}
📢 𝐉𝐨𝐢𝐧 @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━
    """
    
    keyboard = [[InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=CHANNEL_LINK)]]
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
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_apkpure))
    
    print("✅ 𝐀𝐏𝐊𝐏𝐮𝐫𝐞 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝!")
    print(f"👑 Developer: {DEVELOPER}")
    print(f"📢 Channel: @{CHANNEL_USERNAME}")
    
    app.run_polling()

if __name__ == '__main__':
    main()
