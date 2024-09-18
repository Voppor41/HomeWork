team1_num = 5
team2_num = 6

# Пример 1: "В команде Мастера кода участников: 5!"
formatted_str1 = "В команде Мастера кода участников: %d!" % team1_num
print(formatted_str1)

# Пример 2: "Итого сегодня в командах участников: 5 и 6!"
formatted_str2 = "Итого сегодня в командах участников: %d и %d!" % (team1_num, team2_num)
print(formatted_str2)

score_2 = 42
team1_time = 18015.2

# Пример 1: "Команда Волшебники данных решила задач: 42!"
formatted_str3 = "Команда Волшебники данных решила задач: {}!".format(score_2)
print(formatted_str3)

# Пример 2: "Волшебники данных решили задачи за 18015.2 с!"
formatted_str4 = "Волшебники данных решили задачи за {:.1f} с!".format(team1_time)
print(formatted_str4)

score_1 = 40
score_2 = 42
tasks_total = 82
time_avg = 350.4
challenge_result = "Победа команды Мастера кода!"

# Пример 1: "Команды решили 40 и 42 задач."
formatted_str5 = f"Команды решили {score_1} и {score_2} задач."
print(formatted_str5)

# Пример 2: "Результат битвы: победа команды Мастера кода!"
formatted_str6 = f"Результат битвы: {challenge_result}"
print(formatted_str6)

# Пример 3: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!"
formatted_str7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(formatted_str7)

team1_time = 1552.512
team2_time = 2153.31451

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

print(f"Результат битвы: {challenge_result}")
