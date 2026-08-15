# Проект FitLife - MVP версия 1.0

# Неизменяемые величины
WATER_ML_PER_KG = 30
ML_PER_LITER = 1000

# 1. Знакомство
user_name = input(
    "Привет, я - спортивный бот, как я могу к тебе обращаться?\n"
)
user_age = int(input(f"Привет, {user_name}! Сколько тебе лет?\n"))


# 2. Сбор данных
# .replace нагуглил для защиты от неккоректного вода
user_weight = float(
    input(f"Отлично, {user_name}! Сколько ты весишь (в кг)?\n").replace(
        ",", "."
    )
)
user_height = float(
    input(
        f"Принял, {user_name}! А теперь скажи какой у тебя рост "
        "(в метрах)?\n"
    ).replace(",", ".")
)

# 3. Логика расчетов
bmi_value_round = round(user_weight / (user_height ** 2), 1)
water_l = user_weight * WATER_ML_PER_KG / ML_PER_LITER


# 4. Вывод красивого результата
print(
    f"Отчет для пользователя: {user_name} ({user_age})\n"
    f"Твой Индекс Массы Тела: {bmi_value_round}\n"
    f"Рекомендуемая норма воды: {water_l:.1f} л. в день\n\n"
    "Расчет окончен. Будьте здоровы! ",
)
