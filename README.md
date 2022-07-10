# CareBot

![GitHub release (latest by date)](https://img.shields.io/github/v/release/asdfghjkxd/CareBot)
[![Made with Python](https://img.shields.io/badge/Python->=3.9-blue?logo=python&logoColor=white)](https://python.org "Python Homepage")

A simple Telegram bot that assists in pairing volunteers with a VWO that aligns with their interest.

<p align="center"> 
    <img src="https://github.com/asdfghjkxd/CareBot/blob/main/assets/main_screen.png?raw=True" alt="Main Page" width="500"/> 
</p>

## Installation

To install and run this bot locally, create a `.env` file and place your secret Telegram API key in it.

To access this key in the code in `bot.py`,  replace the filename with the name of your `.env` file on line 15, and change line 19 to the name of your Telegram secret API key in your `.env` file, as seen below:

![Uncommenting lines](assets/api_key.png)

An example `.env` file should look like this:

```env
TELEGRAM_API_KEY=YOUR_KEY_HERE
```

After doing so, run the command `pip install -r requirements.txt` to install all requirements of this project. You should be doing this in a properly configured Python environment (venv or conda) to avoid dependency clashes.

You may instead choose to store your environment variable in your instance of your terminal instead. To do so, run the command:

```sh
export YOUR_ENV_VAR_NAME=API_KEY
```

on a Linux-based system or  

```powershell
$env:YOUR_ENV_VAR_NAME = API_KEY
```

and comment out line 15, and replace the variable name in line 19 to `YOUR_ENV_VAR_NAME` instead.

Finally, run the command `python bot.py` to start the bot.

## Usage

If you wish to run this bot locally on your machine, simply run `python bot.py`.

We have launched our bot on Microsoft Azure, on a Windows 10 Enterprise Virtual Machine. Our Telegram bot can be found at the following link: <https://t.me/life_hacked_bot>.
