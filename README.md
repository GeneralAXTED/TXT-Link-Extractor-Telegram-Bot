# TXT Link Extractor Telegram Bot

This Telegram bot receives `.txt` files from users, automatically extracts all `http/https` links from the text, and sends each link back as a separate message.

## 🌟 Features
* Only accepts and processes `.txt` format files.
* Accurately extracts links from the text using Regex.
* Sends each link with a 0.3-second pause to prevent triggering Telegram's spam filters (Flood Control).
* Built with asynchronous execution using the modern `aiogram 3.x` library.

## 🛠 Technologies
* **Python 3.8+**
* **Aiogram 3.x**
* **asyncio**
* **python-dotenv**

## 🚀 Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/GeneralAXTED/TXT-Link-Extractor-Telegram-Bot.git]
   cd TXT-Link-Extractor-Telegram-Bot

Create and activate a Virtual Environment:

Bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Linux/Mac:
source venv/bin/activate
Install required libraries:

Bash
pip install -r requirements.txt
Set up the bot token:
Replace the TOKEN = "BOT_token_here" line in the source code with your actual token obtained from @BotFather (or preferably use a .env file for security).

Run the bot:

Bash
python main.py
📝 Usage Guide
Send the /start command to the bot.

Upload any .txt document containing web links.

The bot will read the file and send you all the extracted links one by one!
