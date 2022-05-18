# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module
from time import sleep
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot, HEROKU_APP_NAME, BOTLOG, BOTLOG_CHATID, ALIVE_NAME, USERBOT_VERSION, HEROKU_API_KEY, repo_lenk
from userbot.modules import ALL_MODULES
from telethon import version
from platform import python_version, uname

INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

cust_modules = []
try:
    from userbot.custom_modules import CUSTOM_MODULES
    if len(CUSTOM_MODULES) > 0:
        for module_name in CUSTOM_MODULES:
            try:
                imported_module = import_module("userbot.custom_modules." + module_name)
                cust_modules.append(module_name)
            except ImportError:
                LOGS.warning("failed to import custom module %s", module_name)
            except Exception as e:
                LOGS.error("Unable to load module %s because of %s", module_name, str(e))
                continue
    if len(cust_modules) > 0:
        LOGS.info("Custom modules successfully loaded: %s", cust_modules)
except Exception:
    pass

LOGS.info(f"You are running Project Fizilion on {repo_lenk}")

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
output = (
    "` =============================== `\n"
    f"`Zonik UserBot is Up and Running.... `\n"
    f"`=============================== `\n"
    f"•`Telethon       : v{version.__version__} `\n"
    f"•`Python         : v{python_version()} `\n"
    f"•`User           : {DEFAULTUSER} `\n"
    f"•`Fizilion       : {USERBOT_VERSION} `\n"
)

async def start():
    if BOTLOG:
        try:
            await bot.send_message(
                BOTLOG_CHATID, output
                        )
        except:
            None
    else:
        pass
bot.loop.run_until_complete(start())

LOGS.info(
    "Congratulations, your userbot is now running !! Test it by typing .alive / .on in any chat."
    "If you need assistance, head to https://t.me/CosmicUserbotChat")
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    print("HEROKU detected, sleeping for 5 minutes to prevent String Session Error")
    LOGS.info("HEROKU detected, sleeping for 5 minutes to prevent String Session Error")
    sleep(300)
    bot.run_until_disconnected()
bot.run_until_disconnected()
