from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""**مرحبا انا **{bn}** 🎵

بامكاني تشغيل الاغاني في المكالمات الجماعيه 
قم برفعي  مشرف في قناتك مع البوت المساعد [- Music Onfroy.](https://t.me/BAXBOT).

قم باضافتي الى مجموعتك لتبدأ الحفله 🎶**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 لطلب المساعده 🛠", url="https://t.me/Muamal")
                  ],[
                    InlineKeyboardButton(
                        "💬 قناة للشروحات", url="https://t.me/TR_RR"
                    ),
                    InlineKeyboardButton(
                        "🔊 قناتي", url="https://t.me/ZzZzBB"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕  اضفني الى مجموعتك ➕", url="https://t.me/BAXBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** تم تفعيل البوت بنجاح ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 قناتي الخاصه", url="https://t.me/ZzZzBB")
                ]
            ]
        )
   )


@Client.on_message(filters.command("panel") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** يمتاز هذا البوت بالبحث والتحميل ✨
اكتب معرف البوت مع اسم الاغنيه للبحث 🔊
مثال : 
@BAXBOT كاظم الساهر
تستطيع تحميل اي اغنيه ايضا 💞
بالاوامر التاليه :
- /ytp رابط الاغنيه من اليوتيوب
- /song رابط الاغنيه من اليوتيوب

للتحكم بالاغنية داخل المكالمه الجماعيه 🔊
- /play بالرد على الاغنيه او الرابط للتشغيل
- /pause لايقاف الاغنيه موقتا داخل المكالمه
- /resume لتكمله الاغنيه المتوقفه
- /stop لايقاف البوت عن تشغيل الاغنيه
- /skip لتخطي الاغنيه الحاليه والانتقال الى الاغنيه التاليه
#ملاحظه : تستطيع ان تقوم بتشغيل اغنيه اخرى فتضاف الى الدور بعد الاغنيه الحاليه فتتنقل بينها وبين الاغاني الباقيه باستخدام امر /skip 🔖 **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 قناتي الخاصه", url="https://t.me/ZzZzBB")
                ],[
                    InlineKeyboardButton(
                        "🎶 الحساب المساعد", url="https://t.me/BAXcalls"
                    )
                ]
            ]
        )
   )
