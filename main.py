import asyncio
import re
from io import BytesIO
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

# BotFather'dan olgan tokeningizni shu yerga yozing
TOKEN = "BOT_token_here"

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'i uchun handler
@dp.message(CommandStart())
async def start_cmd(message: Message):
    text = (
        "Salom! Menga ichida havolalar (http/https) bor bo'lgan .txt fayl yuboring.\n"
        "Men uni ochib, har bir havolani sizga alohida xabar qilib tashlab beraman."
    )
    await message.answer(text)

# Hujjat (fayl) qabul qilish handleri
@dp.message(F.document)
async def handle_document(message: Message):
    document = message.document
    
    # Faqat .txt fayllarni qabul qilish
    if not document.file_name.endswith('.txt'):
        await message.answer("Iltimos, faqat .txt formatidagi fayl yuboring.")
        return

    # Fayl haqida ma'lumot olish
    file_info = await bot.get_file(document.file_id)
    
    # Faylni xotiraga (RAM) yuklab olish
    downloaded_file = BytesIO()
    await bot.download_file(file_info.file_path, downloaded_file)
    
    # Fayl tarkibini o'qish (UTF-8 formatida)
    try:
        content = downloaded_file.getvalue().decode('utf-8')
    except UnicodeDecodeError:
        await message.answer("Faylni o'qishda xatolik yuz berdi. U to'g'ri matn formatidaligiga ishonch hosil qiling.")
        return

    # Muntazam ifoda (Regex) orqali barcha http/https havolalarni qidirish
    urls = re.findall(r'https?://[^\s]+', content)

    # Agar havola topilmasa
    if not urls:
        await message.answer("Fayl ichidan hech qanday havola topilmadi 😔")
        return

    await message.answer(f"🔍 Fayldan {len(urls)} ta havola topildi. Yuborishni boshlayman...")

    # Har bir havolani alohida yuborish
    for url in urls:
        await message.answer(url)
        # Telegram botni "spam" deb o'ylab bloklamasligi uchun kichik pauza beramiz
        await asyncio.sleep(0.3) 
        
    await message.answer("✅ Barcha havolalar yuborildi!")

# Botni ishga tushirish funksiyasi
async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    # Asinxron siklni boshlash
    asyncio.run(main())
