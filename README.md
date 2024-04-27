Welcome to the Retrona Bot!
==========================

This README file will give you all the juicy details about our awesome bot. We built this baby using Python 3.x, Telegram API, and some sweet JSON files. So, grab a snack, sit back, and get ready for the most epic bot experience ever!

What does it do?
----------------

Our Retrona Bot is a multi-talented marvel that can:

* Start conversations: When someone starts a chat with our bot, we'll send them a personalized message introducing ourselves. It's like having a conversation with a super cool robot (which we basically are)!
* Provide help: If someone types `help`, we'll give them a brief rundown of what we can do and how they can use us to buy, sell, or create wallets on Retrona.
* Respond to messages: When someone sends us a message in a group chat, our bot will respond with a clever answer generated using OLLAMA's AI magic!
* Handle group chats: Our bot is designed to handle group conversations seamlessly. It can identify when someone is talking about something and respond accordingly.
How does it work?
------------------

Our bot uses the Telegram API to connect with users and send/receive messages. We also rely on some fancy JSON files to store our configuration data, like our token and username. When a user interacts with our bot, we use these files to determine how to respond.

Technical Stuff:
-----------------

* Programming Language: Python 3.x
* Library: OLLAMA for AI-powered responses
* JSON Files: Used for storing configuration data (like token and username)
* Telegram API: Used for connecting with users and sending/receiving messages
How to Use It?
------------------

1. Clone this repository: `git clone https://github.com/zarigata/Retrona-Bot.git`
2. Install the necessary libraries: `pip install -r requirements.txt` (assuming you have Python 3.x installed)
3. Create a new file named `token.json` and add your Retrona bot token to it. The format should be:
```json
{
    "TOKEN": "[your-token]"
}
