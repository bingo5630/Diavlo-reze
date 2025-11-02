from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')],
                [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.edit_text(
            text=f"""<b>✨ Get Premium Membership of <a href=https://t.me/Cultured_Aodox>@Cultured_Aodox</a> Network and enjoy exclusive benefits!</b>

<blockquote><b><i>💰 Pricing:
━━━━━━━━━━━━━━
⏳ ₹79 / $1.5 : 1 Week
💎 ₹249 / $5 : 1 Month
💠 ₹349 / $7 : 2 Months
🔥 ₹449 / $9 : 3 Months (Most Bought)
⚡ ₹599 / $12 : 6 Months
🚀 ₹899 / $18 : 9 Months
👑 ₹1199 / $22 : 12 Months
━━━━━━━━━━━━━━</i></b></blockquote>

<blockquote><b><i>🚀 Premium Benefits:
━━━━━━━━━━━━━━
➡️ No Link Shortener – Direct links, No ads
➡️ Premium Requests – Request any content
➡️ Fast Uploads & Priority Support
━━━━━━━━━━━━━━</i></b></blockquote>

<b>📩 DM Here:</b> <a href=https://t.me/Diablovolfir0>@Diablovolfir0</a>
<b>We Have Limited Seats For Premium Users!</b>

<b>🧾 Premium Proof:</b> <a href=https://t.me/Aodox_premium_proof>@Aodox_premium_proof</a>""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Diablovolfir0"),
                        InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Cultured_Aodox")
                    ],
                    [
                        InlineKeyboardButton("Anime", url="https://t.me/anime_Aodox"),
                        InlineKeyboardButton("Hemtai Channel", url="https://t.me/Cultured_Aodox")
                    ],
                    [
                        InlineKeyboardButton("Powered By", url="https://t.me/Cultured_Aodox"),
                        InlineKeyboardButton("🔒ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass