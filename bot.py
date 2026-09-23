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
https://share.google/0uMmiN8yYXeMdrlqx
__
(این یک ربات تبلیغاتیه و ربطی به شرکت امایا ندارد.)
__
فوتبال و بیسبال و بسکتبال و .... مسابقات اسب سواری هم داره
با کلی اسلات
👇 سایت بت 100% معتبر کریپتویی که ربات تلگرام هم داره

https://shah.bet/fa?aff=b2c1012-1109526_0


فوکس پول 
یه سایت کسب درآمد پیشنهاد شده از طرف یه کانال قدیمیه
من تست نکردم اما کد رفرالمو میزارم براتون تشخیصتونو بفرستین برام
یا اگر از قدیم اسکم بود اطلاع بدید 👇
https://t.me/FoxPoolbot?start=rMLTTAZ8X3a7

جای فوکس پول میتونه تبلیغات شما باشه ، اگر حق تبلیغ بدین
__
پانزی باز ها 100 تا تتر bep20  بزنن به این آدرس و تراکنش و لینک رفرال و توضیحاتشونو بفرستن تو گروه تا تبلیغاتشونو وارد ربات کنم
- من هش تراکنشی که برام واریز بشه  رو تو گروه سرچ میکنم و پیامتونو پیدا میکنم -

0x7C818dcdF64a265F4D9519b2aC016eE6aA1231ab
__

Hello 👋
Let's get rid of these scam sites
An Iranian site has come and introduced a wallet that you register in
And it introduces sites that can be used to earn money with small activities
Site address 👇
https://share.google/0uMmiN8yYXeMdrlqx
__
(This is an advertising robot and has nothing to do with the Amaya company.)
__
It also has football, baseball, basketball, and .... horse racing
With a lot of slots
👇 100% reliable crypto betting site that also has a telegram robot

https://shah.bet/fa?aff=b2c1012-1109526_0

Focus Money
A suggested income-generating site from an old channel
I haven't tested it, but I'll give you my referral code. Send me your diagnosis
Or let me know if it's been a scam for a long time 👇
https://t.me/FoxPoolbot?start=rMLTTAZ8X3a7

Instead of FoxPool, your ads can be your ads, if you give them the right to advertise

__
Ponzi players, deposit 100 bep20 Tether to this address and send the transaction, referral link, and their description to the group so that I can enter their ads into the robot
- I will search the transaction hash that is deposited to me in the group and find your message -

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
