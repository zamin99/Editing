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
    "remini", "vsco", "pixlr", "touchretouch", "beautyplus",
    "capcut pro", "picsart pro", "pixelab pro", "inshot pro"
]

# =============================================
# 🚀 PRO WELCOME - FULL STYLE (SAME)
# =============================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    first_name = user.first_name if user.first_name else "𝐁𝐫𝐨"
    
    welcome = f"""
╔════════════════════════╗
║  {BOT_EMOJI} 𝐄𝐃𝐈𝐓𝐈𝐍𝐆 𝐏𝐑𝐎 {BOT_EMOJI}  ║
╚════════════════════════╝

𝐇𝐞𝐥𝐥𝐨 **{first_name}**! 👋

━━━━━━━━━━━━━━━━━━━━━
🔍 **𝐊𝐚𝐢𝐬𝐞 𝐊𝐚𝐦 𝐊𝐚𝐫𝐭𝐚 𝐇𝐚𝐢?**
━━━━━━━━━━━━━━━━━━━━━

➡️ 𝐀𝐚𝐩 𝐞𝐝𝐢𝐭𝐢𝐧𝐠 𝐚𝐩𝐩 𝐤𝐚 𝐧𝐚𝐚𝐦 𝐥𝐢𝐤𝐡𝐨
➡️ 𝐁𝐨𝐭 𝐚𝐩𝐤𝐨 𝐝𝐢𝐫𝐞𝐜𝐭 𝐥𝐢𝐧𝐤 𝐛𝐡𝐞𝐣𝐞𝐠𝐚
➡️ 𝐋𝐢𝐧𝐤 𝐭𝐚𝐩 𝐤𝐚𝐫𝐨 → 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐬𝐡𝐮𝐫𝐮

━━━━━━━━━━━━━━━━━━━━━
✅ **𝐒𝐢𝐫𝐟 𝐄𝐝𝐢𝐭𝐢𝐧𝐠 𝐀𝐩𝐩𝐬 𝐤𝐚 𝐥𝐢𝐧𝐤 𝐦𝐢𝐥𝐞𝐠𝐚**
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
# 🔎 EDITING APP CHECK (All Languages Allow)
# =============================================
def is_editing_app(query):
    """Check karo ki user ne editing app likha ya nahi - Sab languages allow"""
    query_lower = query.lower()
    for keyword in EDITING_KEYWORDS:
        if keyword in query_lower:
            return True
    return False

# =============================================
# 🔍 BAS LINK BHEJO - KOI NAAM NAHI
# =============================================
async def send_download_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    
    # Empty check
    if len(query) < 2:
        await update.message.reply_text("❌ Kam se kam 2 letters likho bhai!")
        return
    
    # SIRF EDITING APPS ALLOWED
    if not is_editing_app(query):
        editing_list = "\n".join([f"• `{k}`" for k in EDITING_KEYWORDS[:12]])
        not_editing = f"""
❌ **Yeh editing app nahi hai!**

✅ **Sirf yeh apps allow hain:**
{editing_list}

━━━━━━━━━━━━━━━━━━━━━
👨‍💻 **Dev**: {DEVELOPER}
📢 **Channel**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━

💡 **Koi editing app ka naam likho ↑**
        """
        await update.message.reply_text(not_editing, parse_mode='Markdown')
        return
    
    # ✅ EDITING APP HAI - BAS LINK BHEJO
    search_query = quote(query)
    download_url = f"https://apkpure.com/search?q={search_query}"
    
    # Simple result - Sirf link ka button
    result_text = f"""
✅ **{query.title()}**

⬇️ **Link tap karo → Download start**

━━━━━━━━━━━━━━━━━━━━━
👑 **Dev**: {DEVELOPER}
📢 **Channel**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━
    """
    
    keyboard = [[
        InlineKeyboardButton("📥 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 𝐍𝐎𝐖", url=download_url)
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
👑 **Dev**: `{DEVELOPER}`
📢 **Channel**: @{CHANNEL_USERNAME}
🤖 **Version**: {BOT_VERSION}
━━━━━━━━━━━━━━━━━━━━━

✨ **Features**:
✅ Sirf editing apps
✅ Direct download link
✅ Sab languages allow
✅ 100% working

━━━━━━━━━━━━━━━━━━━━━
⭐ Made by {DEVELOPER}
📢 Join @{CHANNEL_USERNAME}
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
        print("❌ Token nahi mila!")
        return
    
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("developer", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_download_link))
    
    print("✅ Editing Pro Bot Started!")
    print(f"👑 Developer: {DEVELOPER}")
    print(f"📢 Channel: @{CHANNEL_USERNAME}")
    
    app.run_polling()

if __name__ == '__main__':
    main()
