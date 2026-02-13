import os
import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from bs4 import BeautifulSoup
import random

# =============================================
# 🔥 DEVELOPER CREDENTIALS
# =============================================
DEVELOPER = "@SIGMAXZAMIN"
CHANNEL_USERNAME = "ZAMINTRICKS"
CHANNEL_LINK = "https://t.me/ZAMINTRICKS"

# =============================================
# 🎬 EDITING APPS KEYWORDS
# =============================================
EDITING_KEYWORDS = [
    "capcut", "picsart", "pixelab", "inshot", "kinemaster",
    "alight motion", "snapseed", "lightroom", "canva"
]

# =============================================
# 🔄 ROTATING USER AGENTS (BLOCKING SE BACHNE KE LIYE)
# =============================================
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36',
]

# =============================================
# 🔍 ALTERNATIVE APK SOURCE - HAPPYMOD (WORKING)
# =============================================
def search_happymod(query):
    """HappyMod se search - APKPure block hone par alternative"""
    results = []
    
    try:
        url = f"https://happymod.com/search/?q={query.replace(' ', '+')}"
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Accept': 'text/html,application/xhtml+xml',
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # App items find karo
        app_items = soup.select('.app-list-item, .search-item, .pd-list-li')
        
        for item in app_items[:5]:
            try:
                name_elem = item.select_one('.app-name, .media-heading, h3')
                app_name = name_elem.text.strip() if name_elem else "Unknown"
                
                link_elem = item.select_one('a')
                if link_elem and link_elem.get('href'):
                    download_url = link_elem['href']
                    if not download_url.startswith('http'):
                        download_url = 'https://happymod.com' + download_url
                    
                    # Check editing app
                    app_lower = app_name.lower()
                    is_editing = any(keyword in app_lower for keyword in EDITING_KEYWORDS)
                    
                    if is_editing:
                        results.append({
                            "name": app_name[:50],
                            "version": "Latest Mod",
                            "size": "N/A",
                            "download_url": download_url,
                            "source": "HappyMod"
                        })
            except:
                continue
                
    except Exception as e:
        logger.error(f"HappyMod error: {e}")
    
    return results

# =============================================
# 🔍 MAIN SEARCH FUNCTION (DONO SOURCES TRY KAREGA)
# =============================================
async def search_apps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    
    if len(query) < 2:
        return
    
    status = await update.message.reply_text(
        f"🔍 Searching for {query}...\n👨‍💻 Dev: {DEVELOPER}"
    )
    
    # Pehle APKPure try karo
    results = []
    
    # APKPure search
    try:
        url = f"https://apkpure.net/search?q={query.replace(' ', '%20')}"
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for item in soup.select('.search-result li')[:3]:
            name = item.text.strip()[:40] if item.text else "App"
            link = item.select_one('a')
            if link and link.get('href'):
                dl_url = link['href']
                if not dl_url.startswith('http'):
                    dl_url = 'https://apkpure.net' + dl_url
                results.append({
                    "name": name,
                    "url": dl_url,
                    "source": "APKPure"
                })
    except:
        pass
    
    # Agar APKPure se kuch nahi mila toh HappyMod try karo
    if not results:
        results = search_happymod(query)
    
    if not results:
        await status.edit_text(
            f"❌ No results found for '{query}'\n"
            f"Try: capcut pro, picsart, pixelab\n\n"
            f"👨‍💻 {DEVELOPER} | 📢 @{CHANNEL_USERNAME}"
        )
        return
    
    await status.delete()
    
    for app in results[:3]:
        keyboard = [[
            InlineKeyboardButton("⬇️ DOWNLOAD MOD", url=app['url'])
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"✅ {app['name']}\n"
            f"📦 Source: {app['source']}\n\n"
            f"👨‍💻 Dev: {DEVELOPER}\n"
            f"📢 @{CHANNEL_USERNAME}",
            reply_markup=reply_markup
        )

# =============================================
# 🚀 START COMMAND
# =============================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🎬 **EDITING MOD APK BOT**\n\n"
        f"✅ Working! Send app name:\n"
        f"• capcut pro\n• picsart\n• pixelab\n\n"
        f"👨‍💻 Developer: {DEVELOPER}\n"
        f"📢 Channel: @{CHANNEL_USERNAME}",
        parse_mode='Markdown'
    )

# =============================================
# 🎬 MAIN
# =============================================
def main():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not token:
        print("❌ Token not found!")
        return
    
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_apps))
    
    print("✅ Bot started with ALTERNATIVE SOURCE!")
    app.run_polling()

if __name__ == '__main__':
    main()
