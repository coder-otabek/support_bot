from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.btn import buttons
from loader import dp


# 🔘 Inline keyboard (support uchun)
support_kb = InlineKeyboardMarkup(row_width=1)
support_kb.add(
    InlineKeyboardButton("🟢 UzCard", callback_data="uzcard"),
    InlineKeyboardButton("🔵 Humo", callback_data="humo"),
    InlineKeyboardButton("🌍 Visa", callback_data="visa"),
    InlineKeyboardButton("🧑‍💻 Admin bilan bog‘lanish", url="https://t.me/abdumalikovotabek2006")
)


# 🚀 START
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"""👋 <b>Assalomu alaykum, {message.from_user.full_name}!</b>

💙 Bizni tanlaganingiz uchun rahmat!
Sizning ishonchingiz — biz uchun juda muhim 🙌

Quyidagi menyudan foydalanishingiz mumkin 👇
""",
        parse_mode="HTML",
        reply_markup=buttons
    )


# 💙 SUPPORT
@dp.message_handler(text="Qo'llab-quvvatlash")
async def support(message: types.Message):
    await message.answer(
        """💙 <b>Qo‘llab-quvvatlash</b>

Agar loyiha sizga foydali bo‘layotgan bo‘lsa,
uni qo‘llab-quvvatlashingiz mumkin 🙌

☕ Har bir kichik yordam — katta motivatsiya!

👇 Kartani tanlang:""",
        parse_mode="HTML",
        reply_markup=support_kb
    )


# 🟢 UzCard
@dp.callback_query_handler(text="uzcard")
async def uzcard_handler(call: types.CallbackQuery):
    await call.message.answer(
        """🟢 <b>UzCard</b>

<code>6262 5700 4946 3427</code>
👤 Otabek Abdimalikov

💙 Rahmat sizga!""",
        parse_mode="HTML",reply_markup=buttons
    )
    await call.answer()


# 🔵 Humo
@dp.callback_query_handler(text="humo")
async def humo_handler(call: types.CallbackQuery):
    await call.message.answer(
        """🔵 <b>Humo</b>

<code>9860 3501 4362 0507</code>
👤 Otabek Abdimalikov

💙 Rahmat sizga!""",
        parse_mode="HTML",reply_markup=buttons
    )
    await call.answer()


# 🌍 Visa
@dp.callback_query_handler(text="visa")
async def visa_handler(call: types.CallbackQuery):
    await call.message.answer(
        """🌍 <b>Visa</b>

<code>4448 8444 1917 4787</code>
👤 Otabek Abdimalikov

🚀 Siz kabi foydalanuvchilar sabab loyiha rivojlanadi!""",
        parse_mode="HTML",reply_markup=buttons
    )
    await call.answer()


# 🧑‍💻 ADMIN
@dp.message_handler(text="🧑‍💻 Admin bilan bog'lanish")
async def admin_start(message: types.Message):
    await message.answer(
        """🧑‍💻 <b>Admin bilan bog‘lanish</b>

Savol yoki muammo bormi? 👇
To‘g‘ridan-to‘g‘ri yozishingiz mumkin:

👉 https://t.me/abdumalikovotabek2006

⏳ Tez orada javob beramiz!""",
        parse_mode="HTML",reply_markup=buttons
    )