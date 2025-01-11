import requests
import pandas as pd
import matplotlib.pyplot as plt

#Использование библиотеки requests
def get_data(user_url):
    url = user_url

    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")


user_url = input('Введите url сайта с которого хотите считать данные: ')
get_data(user_url)


#Использование библиотеки pandas
df = pd.read_csv('data.csv')
df = pd.DataFrame(df)
print(df.head())

print('-----------------------------')
print('Люди которым меньше 30')
print('-----------------------------')
young = df[df['Возраст'] < 30]
print(young)


#Использование библиотеки matplotlib
plt.plot(df['Город'], df['Возраст'], marker='o')
plt.title('Средний возраст по городам')
plt.xlabel('Город')
plt.ylabel('Возраст')
plt.grid()
plt.show()

