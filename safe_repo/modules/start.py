from pyrogram import filters
from safe_repo import app
from safe_repo.core import script
from safe_repo.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

# Placeholder for logged-in users
logged_in_users = set()

# ------------------- Start-Buttons ------------------- #
buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Join Channel", url="https://t.me/Sonickuwalupdate")],
        [InlineKeyboardButton("Buy Premium", url="https://t.me/Sonickuwalupdatebot")],
        [InlineKeyboardButton("Join Sports Group", url="https://t.me/sports_group")],
        [InlineKeyboardButton("Join Technology Group", url="https://t.me/tech_group")],
        [InlineKeyboardButton("Login", callback_data="login"), InlineKeyboardButton("Logout", callback_data="logout")],
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return

    await message.reply_photo(
        photo="URL_TO_YOUR_IMAGE",  # Replace with the actual URL or path of the image
        caption=script.START_TXT.format(message.from_user.mention),
        reply_markup=buttons
    )

@app.on_callback_query(filters.regex("login"))
async def login_user(_, callback_query):
    await callback_query.answer("Please enter your phone number with country code (e.g., +123456789).")
    
    # Here we would implement the actual login logic, perhaps using a separate function to validate phone numbers
    # For example: log the user into your database or session management
    
    logged_in_users.add(callback_query.from_user.id)

@app.on_callback_query(filters.regex("logout"))
async def logout_user(_, callback_query):
    if callback_query.from_user.id in logged_in_users:
        logged_in_users.remove(callback_query.from_user.id)
        await callback_query.answer("You have been logged out.")
    else:
        await callback_query.answer("You are not logged in.")

async def create_emoji_response(command, user_id):
    emoji_map = {
        'happy': '😊',
        'sad': '😢',
        'sports': '⚽️',
        'technology': '💻',
        # Additional commands and their emojis can be added here
    }
    emoji = emoji_map.get(command, '')
    if emoji:
        await app.send_message(user_id, emoji)

@app.on_message(filters.text & filters.private)
async def command_handler(_, message):
    command = message.text.lower()
    await create_emoji_response(command, message.from_user.id)

@app.on_callback_query()
async def handle_callback_query(_, query: CallbackQuery):
    await query.answer()  # This acknowledges the callback query promptly
