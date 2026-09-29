import asyncio
import logging
import os
from telegram import Bot

# تنظیمات لاگ برای مشاهده بهتر در GitHub Actions
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

MESSAGE = """درود 👋
شاه‌ بت؛ پادشاهی در دنیای پیش‌بینی و کازینو 👑

آیا به دنبال تجربه‌ای متفاوت، سریع و بی‌دغدغه در دنیای شرط‌بندی هستید؟ به «شاه‌بت» خوش آمدید، جایی که حرفه‌ای‌ها بازی می‌کنند.

✅ کازینوی آنلاین بی‌نظیر: بیش از ۶۱۴ بازی اسلات متنوع و ۶۴ میز کازینوی زنده با دیلرهای واقعی. هیجان واقعی کازینو را در خانه تجربه کنید.

⚽ بخش ورزشی کامل: از فوتبال و بسکتبال تا بیسبال، مسابقات اسب‌دوانی و دنیای هیجان‌انگیز ای‌اسپورت (کانتر). تمامی ضرایب با بالاترین کیفیت و به‌روزترین رقابت‌ها برای شماست.

💰 واریز و برداشت آسان: پشتیبانی کامل از روش‌های پرداخت ریالی و ارزهای دیجیتال (کریپتو). بدون معطلی واریز کنید و آنی برداشت کنید.

🚀 بدون محدودیت: ورود آسان با تلگرام یا ایمیل؛ بدون نیاز به فیلترشکن و بدون اتلاف وقت.

🎁 دعوت از دوستان: با سیستم کمیسیون‌دهی شاه‌بت، از فعالیت دوستانتان هم سود کسب کنید!

شاه‌بت؛ یک پکیج کامل برای بت‌بازان حرفه‌ای.

همین حالا وارد شوید و پادشاهی خود را آغاز کنید:

https://shah.bet/fa?aff=b2c1012-1109526_0
"""

# Chat ID شما
TARGET_CHAT_ID = -1002670424462

async def send_promo_message():
    # خواندن توکن از GitHub Secrets (بسیار مهم)
    token = os.environ.get("BOT_TOKEN")
    
    if not token:
        logging.error("خطا: BOT_TOKEN یافت نشد! حتماً در GitHub Secrets مقدار BOT_TOKEN را تنظیم کنید.")
        return

    # ایجاد شیء Bot با توکن خوانده شده از محیط
    bot = Bot(token=token)
    
    try:
        logging.info("در حال ارسال پیام به چت آیدی: %s", TARGET_CHAT_ID)
        # استفاده از context manager برای مدیریت صحیح اتصال
        async with bot:
            await bot.send_message(
                chat_id=TARGET_CHAT_ID,
                text=MESSAGE,
                disable_web_page_preview=True
            )
        logging.info("پیام با موفقیت ارسال شد.")
    except Exception as e:
        logging.error(f"خطا در ارسال پیام: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(send_promo_message())
    except KeyboardInterrupt:
        logging.info("عملیات توسط کاربر متوقف شد.")
    except Exception as e:
        logging.error(f"خطای غیرمنتظره: {e}")
