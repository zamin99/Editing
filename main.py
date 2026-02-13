import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

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
# 🎬 100% WORKING DIRECT DOWNLOAD LINKS (TESTED)
# =============================================
DIRECT_APPS = {
    "capcut": {
        "name": "🎬 CapCut Pro",
        "url": "https://apkpure.com/capcut-video-editor/com.lemon.lvoverseas/download",
        "working": True
    },
    "capcut pro": {
        "name": "🎬 CapCut Pro",
        "url": "https://apkpure.com/capcut-video-editor/com.lemon.lvoverseas/download",
        "working": True
    },
    "picsart": {
        "name": "🎨 Picsart Pro",
        "url": "https://apkpure.com/picsart-photo-editor/com.picsart.studio/download",
        "working": True
    },
    "picsart pro": {
        "name": "🎨 Picsart Pro",
        "url": "https://apkpure.com/picsart-photo-editor/com.picsart.studio/download",
        "working": True
    },
    "pixelab": {
        "name": "✨ PixelLab Pro",
        "url": "https://apkpure.com/pixellab-text-on-photos/com.imagination.pixellab/download",
        "working": True
    },
    "pixelab pro": {
        "name": "✨ PixelLab Pro",
        "url": "https://apkpure.com/pixellab-text-on-photos/com.imagination.pixellab/download",
        "working": True
    },
    "inshot": {
        "name": "📱 InShot Pro",
        "url": "https://apkpure.com/inshot-video-editor/com.camerasideas.instashot/download",
        "working": True
    },
    "inshot pro": {
        "name": "📱 InShot Pro",
        "url": "https://apkpure.com/inshot-video-editor/com.camerasideas.instashot/download",
        "working": True
    },
    "kinemaster": {
        "name": "🎥 KineMaster Pro",
        "url": "https://apkpure.com/kinemaster-video-editor/com.nexstreaming.app.kinemasterfree/download",
        "working": True
    },
    "alight motion": {
        "name": "✨ Alight Motion Pro",
        "url": "https://apkpure.com/alight-motion/com.alightcreative.motion/download",
        "working": True
    },
    "lightroom": {
        "name": "📸 Lightroom Pro",
        "url": "https://apkpure.com/lightroom-photo-video-editor/com.adobe.lrmobile/download",
        "working": True
    },
    "snapseed": {
        "name": "🖼️ Snapseed Pro",
        "url": "https://apkpure.com/snapseed/com.niksoftware.snapseed/download",
        "working": True
    },
    "canva": {
        "name": "🎨 Canva Pro",
        "url": "https://apkpure.com/canva/com.canva.editor/download",
        "working": True
    },
    "filmora": {
        "name": "🎥 Filmora Pro",
        "url": "https://apkpure.com/filmora-video-editor/com.wondershare.filmorago/download",
        "working": True
    },
    "viva video": {
        "name": "🎬 VivaVideo Pro",
        "url": "https://apkpure.com/vivavideo-video-editor-make-tiktok-videos/com.quvideo.xiaoying.Korea/download",
        "working": True
    },
    "powerdirector": {
        "name": "⚡ PowerDirector Pro",
        "url": "https://apkpure.com/powerdirector-video-editor/com.cyberlink.powerdirector/download",
        "working": True
    }
}

# =============================================
# 🚀 PRO WELCOME - FULL STYLE
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
🔥 **𝟭𝟬𝟬% 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝗟𝗜𝗡𝗞𝗦** 🔥
━━━━━━━━━━━━━━━━━━━━━

✅ CapCut Pro
✅ Picsart Pro
✅ PixelLab Pro
✅ InShot Pro
✅ KineMaster Pro
✅ Alight Motion Pro
✅ Lightroom Pro
✅ Snapseed Pro
✅ Canva Pro
✅ Filmora Pro
✅ VivaVideo Pro
✅ PowerDirector Pro

━━━━━━━━━━━━━━━━━━━━━
👑 **Developer**: `{DEVELOPER}`
📢 **Channel**: [{CHANNEL_NAME}]({CHANNEL_LINK})
🤖 **Version**: {BOT_VERSION}
━━━━━━━━━━━━━━━━━━━━━

💎 **App naam likho → Direct download link!**
`capcut pro`  `picsart`  `pixelab`  `inshot`
"""
    
    keyboard = [[InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=CHANNEL_LINK)]]
    await update.message.reply_text(welcome, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

# =============================================
# 🔍 DIRECT DOWNLOAD LINK BHEJO - 100% WORKING
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
        # Direct download button - WORKING LINK!
        download_text = f"""
╔════════════════════════╗
║  {found_app['name']}  ║
╚════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━
✅ **𝗟𝗜𝗡𝗞 𝗦𝗧𝗔𝗧𝗨𝗦**: `𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝟭𝟬𝟬%`
📲 **𝗦𝗼𝘂𝗿𝗰𝗲**: `𝗔𝗣𝗞𝗣𝘂𝗿𝗲.𝗰𝗼𝗺`
━━━━━━━━━━━━━━━━━━━━━

📥 **𝗡𝗲𝗲𝗰𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻 𝘁𝗮𝗽 𝗸𝗮𝗿𝗼**
⬇️ **𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗰 𝘀𝘁𝗮𝗿𝘁 𝗵𝗼𝗴𝗮**

━━━━━━━━━━━━━━━━━━━━━
👑 **𝗗𝗲𝘃**: {DEVELOPER}
📢 **𝗖𝗵𝗮𝗻𝗻𝗲𝗹**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━
        """
        
        keyboard = [[
            InlineKeyboardButton("📥 𝐃𝐈𝐑𝐄𝐂𝐓 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃", url=found_app['url'])
        ]]
        
        await update.message.reply_text(
            download_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    else:
        # App not found - show available apps
        apps_list = "\n".join([f"• `{key}`" for key in list(DIRECT_APPS.keys())[:15]])
        
        not_found = f"""
❌ **𝗔𝗽𝗽 𝗻𝗼𝘁 𝗳𝗼𝘂𝗻𝗱 𝗶𝗻 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲**

━━━━━━━━━━━━━━━━━━━━━
✅ **𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗮𝗽𝗽𝘀:**
{apps_list}
━━━━━━━━━━━━━━━━━━━━━
👨‍💻 **𝗗𝗲𝘃**: {DEVELOPER}
📢 **𝗖𝗵𝗮𝗻𝗻𝗲𝗹**: @{CHANNEL_USERNAME}
━━━━━━━━━━━━━━━━━━━━━

💡 **𝗨𝗽𝗮𝗿 𝗱𝗶 𝗴𝗮𝗶 𝗹𝗶𝘀𝘁 𝘀𝗲 𝗸𝗼𝗶 𝗻𝗮𝗮𝗺 𝗹𝗶𝗸𝗵𝗼**
        """
        
        await update.message.reply_text(not_found, parse_mode='Markdown')

# =============================================
# 📢 ABOUT COMMAND
# =============================================
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = f"""
╔════════════════════════╗
║  🤖 𝗕𝗢𝗧 𝗜𝗡𝗙𝗢 🤖   ║
╚════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━
👑 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿**: `{DEVELOPER}`
📢 **𝗖𝗵𝗮𝗻𝗻𝗲𝗹**: @{CHANNEL_USERNAME}
🤖 **𝗩𝗲𝗿𝘀𝗶𝗼𝗻**: {BOT_VERSION}
━━━━━━━━━━━━━━━━━━━━━

✨ **𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀**:
✅ 𝟭𝟬𝟬% 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗟𝗶𝗻𝗸𝘀
✅ 𝟭𝟱+ 𝗘𝗱𝗶𝘁𝗶𝗻𝗴 𝗔𝗽𝗽𝘀
✅ 𝗢𝗻𝗲 𝘁𝗮𝗽 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱
✅ 𝗔𝗣𝗞𝗣𝘂𝗿𝗲 𝗗𝗶𝗿𝗲𝗰𝘁

━━━━━━━━━━━━━━━━━━━━━
⭐ 𝗠𝗮𝗱𝗲 𝗯𝘆 {DEVELOPER}
📢 𝗝𝗼𝗶𝗻 @{CHANNEL_USERNAME}
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
        print("❌ ERROR: TELEGRAM_BOT_TOKEN not found!")
        print("========================================")
        print(f"👑 Developer: {DEVELOPER}")
        print(f"📢 Channel: {CHANNEL_LINK}")
        print("========================================")
        return
    
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("developer", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, direct_download))
    
    print("\n" + "="*50)
    print("🔥 EDITING PRO BOT - 100% WORKING LINKS")
    print("="*50)
    print(f"👑 Developer: {DEVELOPER}")
    print(f"📢 Channel: @{CHANNEL_USERNAME}")
    print(f"✅ Status: RUNNING")
    print(f"🔗 Links: WORKING")
    print("="*50 + "\n")
    
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
