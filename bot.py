import os
import logging
import asyncio
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
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
    
    keyboard = [
        [InlineKeyboardButton("📚 Learn More", callback_data='learn_more')],
        [InlineKeyboardButton("🌐 Visit Website", url='https://example.com')],
        [InlineKeyboardButton("📱 Join Channel", url='https://t.me/example')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        message_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'learn_more':
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
        
        keyboard = [
            [InlineKeyboardButton("🚀 Join Waitlist", callback_data='waitlist')],
            [InlineKeyboardButton("📢 Updates", url='https://t.me/example_updates')],
            [InlineKeyboardButton("← Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text=learn_more_text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'waitlist':
        waitlist_text = (
            "🎉 *Join Our Exclusive Waitlist!*\n\n"
            "Be among the first to experience our Super AI when it launches.\n\n"
            "Early access members will get:\n"
            "• Priority access to new features\n"
            "• Special launch bonuses\n"
            "• Direct support from our team\n\n"
            "Please send your email to: *waitlist@example.com*\n"
            "or visit our website to register!"
        )
        
        keyboard = [
            [InlineKeyboardButton("🌐 Register Online", url='https://example.com/waitlist')],
            [InlineKeyboardButton("← Back", callback_data='learn_more')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text=waitlist_text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'back':
        message_text = (
            "🚀 *We are launching our Super AI Intelligence!*\n\n"
            "This AI is as advanced as ChatGPT, Gemini, and DeepSeek, "
            "designed to assist people with various tasks.\n\n"
            "Join the future of AI learning and experience next-generation "
            "artificial intelligence at your fingertips!"
        )
        
        keyboard = [
            [InlineKeyboardButton("📚 Learn More", callback_data='learn_more')],
            [InlineKeyboardButton("🌐 Visit Website", url='https://example.com')],
            [InlineKeyboardButton("📱 Join Channel", url='https://t.me/example')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text=message_text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors."""
    logger.error(f"Exception while handling an update: {context.error}")

def main() -> None:
    """Start the bot."""
    # Check token
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set!")
        return
    
    # Create Application
    application = Application.builder().token(TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_error_handler(error_handler)
    
    # Start the Bot
    logger.info("Starting bot... Press Ctrl+C to stop.")
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
