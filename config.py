import config
import telebot
import os

bot = telebot.TeleBot(config.token)

# Начальное приветствие
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I am a command bot. Select one of the following commands:\n/getnewaddress - Get a new address\n/getbalance - Get balance\n/walletinfo - Get wallet information")

# Получить новый адрес
@bot.message_handler(commands=['getnewaddress'])
def get_new_address(message):
    new_address = os.popen("~/kzcash-cli getnewaddress").read()
    bot.send_message(message.chat.id, f"New address generated: {new_address}")

# Получить баланс
@bot.message_handler(commands=['getbalance'])
def get_balance(message):
    balance = os.popen("~/kzcash-cli getbalance").read()
    bot.send_message(message.chat.id, f"Current balance: {balance}")

# Получить информацию о кошельке
@bot.message_handler(commands=['walletinfo'])
def wallet_info(message):
    info = os.popen("~/kzcash-cli getwalletinfo").read()
    bot.send_message(message.chat.id, f"Wallet info: {info}")

if __name__ == '__main__':
    bot.infinity_polling()
