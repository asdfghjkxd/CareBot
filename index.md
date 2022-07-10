# CareBot

![GitHub release (latest by date)](https://img.shields.io/github/v/release/asdfghjkxd/CareBot)
[![Made with Python](https://img.shields.io/badge/Python->=3.9-blue?logo=python&logoColor=white)](https://python.org "Python Homepage")
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)

A simple Telegram bot that assists in pairing volunteers with a VWO that aligns with their interest.

<p align="center"> 
    <img src="https://github.com/asdfghjkxd/CareBot/blob/main/assets/main_screen.png?raw=True" alt="Main Page" width="500"/> 
</p>

## Installation

Firstly, clone this repository onto your machine by running `git clone https://github.com/asdfghjkxd/CareBot`, or by clicking the green `Code` button, and selecting `Download ZIP`, followed by extracting the ZIP file to the desired location on your machine.

Next, create a `.env` file and place your secret Telegram API key in it, or modify the existing file `.secrets.env` with your Telegram API key.

To access this key in the code in `bot.py`,  replace the filename with the name of your `.env` file on line 15 (if you created a new `.env` file), and change line 19 to the name of your Telegram secret API key in your `.env` file, as seen below:

![Uncommenting lines](assets/api_key.png)

An example `.env` file should look like this:

```dotenv
TELEGRAM_API_KEY=YOUR_KEY_HERE
```

If you do not wish to store your API key in the `.env` file, you may instead choose to store your environment variable in your instance of your Terminal instead. To do so, run the command:

```sh
export YOUR_ENV_VAR_NAME=API_KEY
```

on a Linux-based system or  

```powershell
$env:YOUR_ENV_VAR_NAME = API_KEY
```

on a Windows system, and comment out line 15 of `bot.py`, and replace the variable name in line 19 to `YOUR_ENV_VAR_NAME` instead.

After doing so, run the command `pip install -r requirements.txt` to install all requirements of this project. You should be doing this in a properly configured Python environment (`venv` or `conda`) to avoid dependency clashes.

## Usage

To start the bot, simply run the command `python bot.py` on your Terminal. Do ensure that you have properly activated your environment by running `conda activate YOUR_ENV_NAME` for `conda`, `source path/to/your/env/bin/activate` on Mac/Linux systems or `path\to\your\env\Scripts\activate.bat` on Windows systems for `venv`.

## Deployment

We have launched our bot on Microsoft Azure, on a Windows 10 Enterprise Virtual Machine. Our live instance of the Telegram bot can be found at the following link: [Telegram Bot](https://t.me/life_hacked_bot)
