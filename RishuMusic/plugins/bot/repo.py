from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ sɪʟᴇɴᴛʜʀᴀx ʀᴇᴘᴏ
 
● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʙᴇsᴛɪᴇ ꭙ ᴍᴜsɪᴄ ♡゙゙

● ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ● **
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/http://t.me/RadhikaMusicRobot?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/Usesense"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/AuraVisual"),
          ],
               [
                InlineKeyboardButton("• ɴᴇᴛᴡᴏʀᴋ •", url=f"https://t.me/AuraVisual"),
],
[
InlineKeyboardButton("• ʀᴇᴘᴏ •", url=f"https://github.com"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/qu0hhu.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
