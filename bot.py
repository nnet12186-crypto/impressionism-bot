import telebot
from telebot import types

TOKEN = '8990195903:AAHA_XxQKNMGvU4u39lpa1j5FmsiNoefMSQ'
bot = telebot.TeleBot(TOKEN)

# ---------- ТЕКСТЫ ----------
INFO = {
    "about": (
        "🎨 *Импрессионизм*\n\n"
        "Импрессионизм — направление в искусстве, зародившееся во Франции "
        "в 1860-х годах. Название произошло от картины Клода Моне "
        "*«Впечатление. Восходящее солнце»* (Impression, soleil levant).\n\n"
        "Художники стремились передать мимолётные впечатления, игру света "
        "и воздуха, а не точные детали. Они писали быстрыми мазками, "
        "часто на пленэре (на открытом воздухе)."
    ),
    "features": (
        "✨ *Особенности импрессионизма:*\n\n"
        "• Передача света и атмосферы\n"
        "• Быстрые, раздельные мазки\n"
        "• Яркие, чистые цвета\n"
        "• Работа на пленэре\n"
        "• Мимолётные сцены повседневной жизни\n"
        "• Отсутствие чётких контуров\n"
        "• Интерес к городской жизни и природе"
    ),
    "artists": (
        "👨‍🎨 *Главные художники:*\n\n"
        "🇫🇷 *Клод Моне* — «Впечатление. Восходящее солнце», «Кувшинки»\n"
        "🇫🇷 *Пьер Огюст Ренуар* — «Завтрак гребцов», «Бал в Мулен де ла Галетт»\n"
        "🇫🇷 *Эдгар Дега* — «Голубые танцовщицы», «Абсент»\n"
        "🇫🇷 *Камиль Писсарро* — «Бульвар Монмартр»\n"
        "🇫🇷 *Эдуард Мане* — «Завтрак на траве», «Олимпия»\n"
        "🇫🇷 *Берта Моризо* — «Колыбель»\n"
        "🇺🇸 *Мэри Кассат* — «Мать и дитя»"
    ),
    "paintings": (
        "🖼 *Известные картины:*\n\n"
        "1️⃣ «Впечатление. Восходящее солнце» — Клод Моне (1872)\n"
        "2️⃣ «Завтрак гребцов» — Ренуар (1881)\n"
        "3️⃣ «Голубые танцовщицы» — Дега (1897)\n"
        "4️⃣ «Кувшинки» — Моне (цикл, 1899–1926)\n"
        "5️⃣ «Бал в Мулен де ла Галетт» — Ренуар (1876)\n"
        "6️⃣ «Бульвар Монмартр» — Писсарро (1897)\n"
        "7️⃣ «Завтрак на траве» — Мане (1863)"
    ),
    "history": (
        "📜 *История направления:*\n\n"
        "*1860-е* — Молодые художники начинают экспериментировать "
        "со светом и цветом.\n\n"
        "*1874* — Первая выставка «Анонимного общества художников». "
        "Критик Луи Леруа в насмешку назвал их «импрессионистами», "
        "но название прижилось.\n\n"
        "*1880-е* — Признание публики, успех у коллекционеров.\n\n"
        "*1890-е–1900-е* — Влияние на постимпрессионизм "
        "(Ван Гог, Сезанн, Гоген)."
    ),
    "legacy": (
        "🌍 *Влияние и наследие:*\n\n"
        "• Открыл путь модернизму XX века\n"
        "• Повлиял на постимпрессионизм, фовизм, кубизм\n"
        "• Изменил отношение к свету и цвету в живописи\n"
        "• Вдохновил музыку (Дебюсси) и литературу\n"
        "• Сегодня работы импрессионистов — среди самых дорогих в мире"
    ),
}

# ---------- КЛАВИАТУРЫ ----------
def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📖 О направлении", "✨ Особенности")
    kb.row("👨‍🎨 Художники", "🖼 Картины")
    kb.row("📜 История", "🌍 Наследие")
    kb.row("❓ Викторина")
    return kb


def quiz_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("Вопрос 1", "Вопрос 2", "Вопрос 3")
    kb.row("🔙 В меню")
    return kb

# ---------- ОБРАБОТЧИКИ ----------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я расскажу тебе о *импрессионизме* — одном из самых "
        "ярких направлений в искусстве.\n\n"
        "Выбери, что тебя интересует 👇",
        parse_mode='Markdown',
        reply_markup=main_menu()
    )


@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(
        message.chat.id,
        "Используй кнопки ниже, чтобы узнать об импрессионизме 👇",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda m: m.text == "📖 О направлении")
def about(message):
    bot.send_message(message.chat.id, INFO["about"], parse_mode='Markdown')


@bot.message_handler(func=lambda m: m.text == "✨ Особенности")
def features(message):
    bot.send_message(message.chat.id, INFO["features"], parse_mode='Markdown')


@bot.message_handler(func=lambda m: m.text == "👨‍🎨 Художники")
def artists(message):
    bot.send_message(message.chat.id, INFO["artists"], parse_mode='Markdown')


@bot.message_handler(func=lambda m: m.text == "🖼 Картины")
def paintings(message):
    bot.send_message(message.chat.id, INFO["paintings"], parse_mode='Markdown')


@bot.message_handler(func=lambda m: m.text == "📜 История")
def history(message):
    bot.send_message(message.chat.id, INFO["history"], parse_mode='Markdown')


@bot.message_handler(func=lambda m: m.text == "🌍 Наследие")
def legacy(message):
    bot.send_message(message.chat.id, INFO["legacy"], parse_mode='Markdown')


# ---------- ВИКТОРИНА ----------
@bot.message_handler(func=lambda m: m.text == "❓ Викторина")
def quiz(message):
    bot.send_message(
        message.chat.id,
        "🎯 *Викторина об импрессионизме*\n\nВыбери вопрос:",
        parse_mode='Markdown',
        reply_markup=quiz_menu()
    )


@bot.message_handler(func=lambda m: m.text == "Вопрос 1")
def q1(message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("Клод Моне", callback_data="q1_monet"),
        types.InlineKeyboardButton("Ренуар", callback_data="q1_wrong"),
    )
    kb.add(
        types.InlineKeyboardButton("Дега", callback_data="q1_wrong"),
        types.InlineKeyboardButton("Мане", callback_data="q1_wrong"),
    )
    bot.send_message(
        message.chat.id,
        "Кто написал картину «Впечатление. Восходящее солнце»?",
        reply_markup=kb
    )


@bot.message_handler(func=lambda m: m.text == "Вопрос 2")
def q2(message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("Италия", callback_data="q2_wrong"),
        types.InlineKeyboardButton("Франция", callback_data="q2_france"),
    )
    kb.add(
        types.InlineKeyboardButton("Испания", callback_data="q2_wrong"),
        types.InlineKeyboardButton("Германия", callback_data="q2_wrong"),
    )
    bot.send_message(
        message.chat.id,
        "В какой стране зародился импрессионизм?",
        reply_markup=kb
    )


@bot.message_handler(func=lambda m: m.text == "Вопрос 3")
def q3(message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("1874", callback_data="q3_1874"),
        types.InlineKeyboardButton("1863", callback_data="q3_wrong"),
    )
    kb.add(
        types.InlineKeyboardButton("1890", callback_data="q3_wrong"),
        types.InlineKeyboardButton("1901", callback_data="q3_wrong"),
    )
    bot.send_message(
        message.chat.id,
        "В каком году прошла первая выставка импрессионистов?",
        reply_markup=kb
    )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    answers = {
        "q1_monet": "✅ Верно! «Впечатление. Восходящее солнце» написал Клод Моне в 1872 году.",
        "q1_wrong": "❌ Неверно. Правильный ответ — Клод Моне (1872).",
        "q2_france": "✅ Верно! Импрессионизм зародился во Франции.",
        "q2_wrong": "❌ Неверно. Правильный ответ — Франция.",
        "q3_1874": "✅ Верно! Первая выставка прошла в 1874 году в Париже.",
        "q3_wrong": "❌ Неверно. Правильный ответ — 1874 год.",
    }
    bot.answer_callback_query(call.id)
    if call.data in answers:
        bot.send_message(call.message.chat.id, answers[call.data])


@bot.message_handler(func=lambda m: m.text == "🔙 В меню")
def back(message):
    bot.send_message(message.chat.id, "Главное меню 👇", reply_markup=main_menu())


# ---------- ЗАПУСК ----------
if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()