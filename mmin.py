import telebot
import requests

# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual bot token
bot = telebot.TeleBot("6086609576:AAHOrTRJa15VosHEEN9_7K3Ja-Gdt4TQDfw")

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, " hi welcome to my bot I hope get answers and enjoy :) muadax", reply_markup=markup)

# Handle the "What is your name?" message
@bot.message_handler(func=lambda message: message.text == "What is your name?")
def send_bot_name(message):
    bot.send_message(message.chat.id, "Hi, I'm bot developed by M programmer")

# Handle the "azkar" message
@bot.message_handler(func=lambda message: message.text in ["أذكار الصباح", "أذكار المساء"])
def send_azkar_info(message):
    if message.text == "أذكار الصباح":
        bot.send_message(message.chat.id, "   بعض أذكار الصباح مع عدد التكرار:\n"
                                          "1- سُبْحَانَ اللَّهِ وَبِحَمْدِهِ، عَدَدَ خَلْقِهِ، وَرِضَا نَفْسِهِ، وَزِنَةَ عَرْشِهِ، وَمِدَادَ كَلِمَاتِهِ. (100 مرة)\n"
                                          "2- اللَّهُمَّ إِنِّي أَصْبَحْتُ أُشْهِدُكَ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ، وَمَلائِكَتِكَ، وَجَمِيعَ خَلْقِكَ، أنَّكَ أنْتَ اللهُ لا إله إلا أنْتَ وحْدَكَ لا شريك لك، وأنَّ مُحَمَّدًا عبْدُكَ ورسولُك. (4 مرات)\n"
                                          "3- اللهم بك أصبحنا، وبك أمسينا، وبك نحيا، وبك نموت، وإليك النشور. (1 مرة)\n"
                                          " 4- سُبْحـانَ اللهِ وَبِحَمْـدِهِ ( 100 مرة ) \n"
                                          "5- أَعُوذُ بِكَلِماتِ اللهِ التّامّاتِ، مِنْ شَرِّ ما خَلَقَ. (3 مرات)\n"
                                          "6- اللَّهُمَّ إِنِّي أَسْأَلُكَ عِلْمًا نَافِعًا، وَرِزْقًا طَيِّبًا، وَعَمَلاً مُتَقَبَّلاً. (1 مرة)\n"
              "7- اللهم إني أسألك العفو والعافية، والمعافاة في الدنيا والآخرة، اللهم إني أسألك العفو والعافية في ديني ودنياي، وأهلي ومالي، اللهم استرني فوق الأرض، وتحت الأرض، ويوم العرض عليك. (3 مرات)\n"
"8- اللهم صلى على محمد وعلى آل محمد، كما صليت على إبراهيم وعلى آل إبراهيم، إنك حميد مجيد، اللهم بارك على محمد وعلى آل محمد، كما باركت على إبراهيم وعلى آل إبراهيم، إنك حميد مجيد. (10 مرات)\n")
    else:
        bot.send_message(message.chat.id,  " اذكار المساء :\n"
                     "بسم الله الرحمن الرحيم\n"
                     "1. سُبْحَانَ اللَّهِ وَبِحَمْدِهِ - 100 مرة\n"
                     "2. اللَّهُمَّ إِنِّي أَسْأَلُكَ العَفْوَ وَالعَافِيَةَ - 100 مرة\n"
                     "3. لا إِلَهَ إِلاَّ اللهُ وَحْدَهُ لا شَرِيكَ لَهُ، لَهُ المُلْكُ وَلَهُ الحَمْدُ يُحْيِي وَيُمِيتُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ - 100 مرة\n"
                     "4. أستغفر الله العظيم الذي لا إله إلا هو الحي القيوم وأتوب إليه - 100 مرة\n"
                     "5. اللهم صل على محمد وعلى آل محمد كما صليت على إبراهيم وعلى آل إبراهيم إنك حميد مجيد - 100 مرة.")


# Create a keyboard with 3 buttons
markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
btn1 = telebot.types.KeyboardButton('أذكار المساء')
btn2 = telebot.types.KeyboardButton('أذكار الصباح')
btn3 = telebot.types.KeyboardButton('Programmer')
markup.add(btn1, btn2, btn3)

# Handle the "programmer" button
@bot.message_handler(func=lambda message: message.text == "Programmer")
def send_programmer_info(message):
    bot.send_message(message.chat.id, "This bot by Muad")

# Handle the "about" message
@bot.message_handler(func=lambda message: message.text == "about")
def send_about_info(message):
    bot.send_message(message.chat.id, "Idk , but this a test for my bot enjoy :)")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # Send "processing" message
    processing_message = bot.send_message(message.chat.id, "wait me I will answer U now , I hope bot like U @muadax ")
    

    # Send API request to get the response
    text = message.text
    api = requests.get("https://GPTCHATPRO.devxpro.repl.co/?text="+text).json()["res"]
    # Edit the "processing" message with the API response
    bot.edit_message_text(chat_id=message.chat.id, message_id=processing_message.message_id, text=api)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False)

# Start the bot
print("Bot is running...")
bot.polling()
