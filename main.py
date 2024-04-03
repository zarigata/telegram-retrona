from typing import Final
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from ollama import Client

# Function to read token from JSON file
def read_token_from_json(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
        return config.get('TOKEN')

# Read token from JSON file
TOKEN: Final = read_token_from_json('token.json')
BOT_USERNAME: Final = '@retronabot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_to_message('whazap, im rezz, im the intern at Retrona and i will help you in any way i can')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_to_message('soo, like, im here to help you to buy, sell and create a wallet with retrona on it like ,soo cool')

# Function to handle responses
def handle_responses(text:str) -> str:
    processed: str = text
    client = Client(host='http://192.168.15.115:11434')
    response = client.chat(model='retrona:latest', messages=[
        {'role': 'user',
         'content': processed,
         'stream' : 'false',
         'options' : {
             'num_ctx' : 1024,
         }
        },])
    grouptext = response
    return response['message']['content']

# Function to handle messages
async def handle_message(update: Update,context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        response: str = handle_responses(text)

    print('Bot', response)
    await update.message.reply_text(response)

# Error handling function
async def error(update: Update,context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error on!!!!! {context.error}')

# Main block
if __name__ == '__main__':
    print('STARTING')
    
    # Build application with token read from JSON
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)
    
    print('POOLING')
    app.run_polling(poll_interval=2)
