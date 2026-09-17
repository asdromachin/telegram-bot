import asyncio
import logging
import os
from telegram.ext import Application

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

TARGET_CHAT_ID = -1002670424462

async def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    if not TOKEN:
        logging.error("توکن پیدا نشد!")
        return

    app = Application.builder().token(TOKEN).build()
    await app.initialize()
    
    try:
        await app.bot.send_message(
            chat_id=TARGET_CHAT_ID,
            text=MESSAGE,
            disable_web_page_preview=True
        )
        logging.info("پیام با موفقیت ارسال شد")
    except Exception as e:
        logging.error(f"خطا در ارسال: {e}")
    
    await app.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
