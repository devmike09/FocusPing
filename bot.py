import os
import asyncio
import logging
from telegram import Bot
from telegram.ext import Application

# --- CONFIGURATION ---
# Replace 'YOUR_USER_ID' with your actual Telegram User ID (numeric)
# Or set it as an environment variable named USER_ID on Render
USER_ID = os.getenv("USER_ID")
TOKEN = os.getenv("TELEGRAM_TOKEN")
INTERVAL = 3600  # 1 hour in seconds

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def send_reminders(bot: Bot):
    """Loop that sends a reminder every hour."""
    if not USER_ID:
        logger.error("USER_ID environment variable is missing!")
        return

    while True:
        try:
            message = "🚀 **Don't procrastinate! Don't be lazy!** \nFocus on your goals right now."
            await bot.send_message(chat_id=USER_ID, text=message, parse_mode="Markdown")
            logger.info("Reminder sent successfully.")
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
        
        # Wait for 1 hour
        await asyncio.sleep(INTERVAL)

async def main():
    """Start the bot."""
    if not TOKEN:
        logger.error("TELEGRAM_TOKEN environment variable is missing!")
        return

    # Initialize the Application (required to keep the event loop happy)
    application = Application.builder().token(TOKEN).build()
    bot = application.bot

    print(f"Bot started. Sending reminders to {USER_ID} every hour...")
    
    # Run the reminder loop
    await send_reminders(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
