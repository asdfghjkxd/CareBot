import datetime
import logging
import json
import os

from typing import *
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, Updater
from dotenv import load_dotenv


# load API secrets
# load_dotenv('.secrets.env')

# set loggers, form URLs, and API key
LOGGER = logging.getLogger("CareBot")
TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScJfCz5iYAhRPNEabDAzrA5uHhwf-Kvj2OlINFSt6dM14x0rg/viewform?usp=sf_link"

# for Heroku
PORT = int(os.environ["PORT", "8443"])
APP_NAME = "https://lifehack2022.herokuapp.com/"

class VWOOptions:
    """Class to manage the VWOs Keyboards"""

    def __init__(self) -> None:
        self.keyboards = {}

        # add the few options into the init function
        self.add_options("children", {
            "Make-A-Wish": ("make_a_wish", FORM_URL),
            "Singapore Children's Society": ("scs", FORM_URL),
            "Save The Children": ("stc", FORM_URL)
        })
        self.add_options("elderly", {
            "TOUCH": ("touch", FORM_URL),
            "Institute of Mental Health": ("imh", FORM_URL)
        })
        self.add_options("coding", {
            "C4SG": ("c4sg", FORM_URL),
            "Singapore Computer Society": ("sg_com_soc", FORM_URL)
        })
        self.add_options("low_income", {
            "Food From The Heart": ("ffth", FORM_URL),
            "HereWithYouSG": ("hwy_sg", FORM_URL)
        })
        self.add_options("students", {
            "Children's Wishing Well": ("cww", FORM_URL)
        })
        self.add_options("healthcare", {
            "UNICEF": ("unicef", FORM_URL)
        })
        self.add_options("flag", {
            "Red Cross": ("redX", FORM_URL)
        })

    def add_options(self, option_name: str, button_name_to_data_and_url: Mapping[str, Sequence[str]]) -> None:
        """Adds a series of button names, mapped to a sequence containing both the callback value and the URL"""

        kb = []

        for name, value in button_name_to_data_and_url.items():
            value = list(value)
            kb.append(InlineKeyboardButton(name, callback_data=value[0], url=value[1]))

        self.keyboards[option_name] = kb

    def retrieve_option(self, option_name: str) -> List:
        """Returns the keyboard options for a particular input option"""

        if option_name not in self.keyboards:
            raise ValueError("Invalid Option")
        else:
            return self.keyboards.get('option_name')


# set the keyboards
VWO_OPTIONS = VWOOptions()


# functions for the telegram bot
async def startScreen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the user the starting message to familiarlise themselves with the bot"""

    await update.message.reply_markdown(f"Hello {update.message.from_user.full_name}! 👋👋👋\n\n"
                                        "Welcome to our Telegram Bot aimed at helping you connect to Volunteering Organisations in "
                                        "Singapore!\n\n"
                                        "Kindly choose any one of the following categories to begin finding "
                                        "the right VWO for you!")

    kb = [
        [
            InlineKeyboardButton("Children",
                                 callback_data="children"),
            InlineKeyboardButton("Elderly",
                                 callback_data="elderly"),
            InlineKeyboardButton("Coding for Good", callback_data="coding")
        ],
        [
            InlineKeyboardButton(
                "Families", callback_data="low_income"),
            InlineKeyboardButton("Students", callback_data="students"),
            InlineKeyboardButton("Healthcare", callback_data="healthcare")
        ],
        [InlineKeyboardButton("Flag Day", callback_data="flag")]
    ]

    inline_kb = InlineKeyboardMarkup(kb)
    await update.message.reply_text("Choose any one below: ", reply_markup=inline_kb)


async def startResponse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Retrieves the starting screen response from the user"""

    answer = update.callback_query

    await answer.answer()
    
    correct_kb = await dispatchToType(answer.data)
    await answer.message.reply_text("Here's a list of VWOs which match your selection: ", reply_markup=correct_kb)
    
    # Passing user input into saveData func to save into file
    await saveData(update, answer.data)


async def dispatchToType(types: Literal["children", "elderly", "coding", "low_income", "students", "healthcare", "flag"]) \
    -> InlineKeyboardMarkup:
    """Calls the right function to show the right page containing all VWOs attached/related to the types of VWO selected"""
    
    kb = VWO_OPTIONS.keyboards.get(types)
    kb = InlineKeyboardMarkup([[k] for k in kb])
    return kb


async def saveData(update, data) -> None:
    """Saves user info into users.json file"""
    
    user = update.effective_user

    user_info = {
        'username': user.username,
        'name': user.first_name,
        'chat_id': update.effective_chat.id,
        'choice': data
    }

    with open('users.json', 'r') as user_db:
        users = json.load(user_db)

    users[user.id] = user_info

    with open('users.json', 'w') as user_db:
        json.dump(users, user_db)

def herokuMain():
    """Function to start the bot on Heroku"""

    LOGGER.warning(msg=f'Bot started at {datetime.datetime.now()}')
    updater = Updater(TELEGRAM_API_KEY, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", startScreen))
    dispatcher.add_handler(CallbackQueryHandler(startResponse))
    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TELEGRAM_API_KEY,
                          webhook_url=APP_NAME + TELEGRAM_API_KEY)
    updater.idle()

def pythonMain():
    """Function to start the bot locally"""

    LOGGER.warning(msg=f'Bot started at {datetime.datetime.now()}')
    
    app = ApplicationBuilder().token(TELEGRAM_API_KEY).build()
    app.add_handler(CommandHandler("start", startScreen))
    app.add_handler(CallbackQueryHandler(startResponse))
    app.run_polling()

# main code
if __name__ == '__main__':
    herokuMain()
    # pythonMain()