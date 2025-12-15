  import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Message text
    message_text = (
        "🚀 *We are launching our Super AI Intelligence!*\n\n"
        "This AI is as advanced as ChatGPT, Gemini, and DeepSeek, "
        "designed to assist people with various tasks.\n\n"
        "Join the future of AI learning and experience next-generation "
        "artificial intelligence at your fingertips!\n\n"
        "✨ *Features:*\n"
        "• Advanced natural language understanding\n"
        "• Multi-task assistance\n"
        "• Continuous learning capabilities\n"
        "• 24/7 availability"
    )
    
    # Create inline keyboard
    keyboard = [
        [InlineKeyboardButton("📚 Learn More", callback_data='learn_more')],
        [InlineKeyboardButton("🌐 Visit Website", url='https://your-website.com')],
        [InlineKeyboardButton("📱 Join Channel", url='https://t.me/your_channel')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        message_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Learn More callback handler
async def learn_more(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    learn_more_text = (
        "🤖 *About Our Super AI*\n\n"
        "Our AI system combines the best features of leading AI models:\n\n"
        "🔹 *Advanced Capabilities:*\n"
        "• Natural conversations\n"
        "• Problem solving\n"
        "• Creative writing\n"
        "• Code generation\n"
        "• Research assistance\n\n"
        "🔹 *Coming Soon:*\n"
        "• Image generation\n"
        "• Voice interactions\n"
        "• File processing\n"
        "• Custom AI agents\n\n"
        "*Stay tuned for our official launch!*"
    )
    
    # Additional buttons
    keyboard = [
        [InlineKeyboardButton("🚀 Join Waitlist", callback_data='waitlist')],
        [InlineKeyboardButton("📢 Updates", url='https://t.me/your_updates_channel')],
        [InlineKeyboardButton("← Back", callback_data='back_to_start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text=learn_more_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Waitlist callback
async def waitlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    waitlist_text = (
        "🎉 *Join Our Exclusive Waitlist!*\n\n"
        "Be among the first to experience our Super AI when it launches.\n\n"
        "Early access members will get:\n"
        "• Priority access to new features\n"
        "• Special launch bonuses\n"
        "• Direct support from our team\n\n"
        "Please send your email to: *waitlist@yourai.com*\n"
        "or visit our website to register!"
    )
    
    keyboard = [
        [InlineKeyboardButton("🌐 Register Online", url='https://your-website.com/waitlist')],
        [InlineKeyboardButton("← Back", callback_data='learn_more')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text=waitlist_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Back to start callback
async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    message_text = (
        "🚀 *We are launching our Super AI Intelligence!*\n\n"
        "This AI is as advanced as ChatGPT, Gemini, and DeepSeek, "
        "designed to assist people with various tasks.\n\n"
        "Join the future of AI learning and experience next-generation "
        "artificial intelligence at your fingertips!"
    )
    
    keyboard = [
        [InlineKeyboardButton("📚 Learn More", callback_data='learn_more')],
        [InlineKeyboardButton("🌐 Visit Website", url='https://your-website.com')],
        [InlineKeyboardButton("📱 Join Channel", url='https://t.me/your_channel')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text=message_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Error handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Exception while handling an update: {context.error}")

def main():
    """Start the bot."""
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set!")
        return
    
    # Create application
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(learn_more, pattern='^learn_more$'))
    application.add_handler(CallbackQueryHandler(waitlist, pattern='^waitlist$'))
    application.add_handler(CallbackQueryHandler(back_to_start, pattern='^back_to_start$'))
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
