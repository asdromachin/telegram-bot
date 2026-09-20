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
بیاین از دست این سایت های اسکم خلاص بشیم 
یه سایت ایرانی اومده یه کیف پول معرفی کرده که داخلش ثبت نام میکنید
و سایت هایی رو معرفی میکنه که میشه با فعالیت های کوچیک ازشون کسب درامد کرد
آدرس سایت 👇
https://faucet.ir/
__
(این یک ربات تبلیغاتیه و ربطی به شرکت امایا ندارد.)
__

👇 سایت بت 100% معتبر کریپتویی که ربات تلگرام هم داره

https://telegram.me/shahbetvip_bot?start=aff_b2c1012-1109526_0

__
پانزی باز ها 500 تا تتر bep20  بزنن به این آدرس و تراکنش و لینک رفرال و توضیحاتشونو بفرستن تو گروه تا تبلیغاتشونو وارد ربات کنم

0x7C818dcdF64a265F4D9519b2aC016eE6aA1231ab
__


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
