import asyncio
import logging
import os
from telegram import Bot

# تنظیمات لاگ
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

MESSAGE = """درود 👋
بیاین از دست این سایت های اسکم خلاص بشیم 
یه سایت ایرانی اومده یه کیف پول معرفی کرده که داخلش ثبت نام میکنید
و سایت هایی رو معرفی میکنه که میشه با فعالیت های کوچیک ازشون کسب درامد کرد
آدرس سایت 👇
https://faucet.ir/
__
(این یک ربات تبلیغاتیه و ربطی به شرکت امایا ندارد.)
__
"""

# دقت کنید: Chat ID باید عدد باشد (بدون کوتیشن اگر integer است)
TARGET_CHAT_ID = -1002670424462

async def send_promo_message():
    # خواندن توکن از Secrets گیت‌هاب
    TOKEN = os.environ.get("BOT_TOKEN")
    
    if not TOKEN:
        logging.error("خطا: BOT_TOKEN یافت نشد! مطمئن شوید در GitHub Secrets تعریف شده است.")
        return

    # ایجاد شیء Bot
    bot = Bot(token=TOKEN)
    
    try:
        logging.info("در حال ارسال پیام...")
        # استفاده از context manager یا اطمینان از بستن اتصال
        async with bot:
            await bot.send_message(
                chat_id=TARGET_CHAT_ID,
                text=MESSAGE,
                disable_web_page_preview=True
            )
        logging.info("پیام با موفقیت ارسال شد.")
    except Exception as e:
        logging.error(f"خطا در ارسال: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(send_promo_message())
    except KeyboardInterrupt:
        pass
