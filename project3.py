import pandas as pd
import requests
from bs4 import BeautifulSoup

# Завантаження сторінки
url = 'https://uk.wikipedia.org/wiki/Таблиця'
response = requests.get(url)

# Парсинг HTML-коду сторінки
soup = BeautifulSoup(response.text, 'html.parser')

# Знаходження таблиці на сторінці (замініть на власний шлях до таблиці)
table = soup.find('table')

# Створення DataFrame з таблиці
df = pd.read_html(str(table), header=0)[0]

# Очищення від дублікатів
df.drop_duplicates(inplace=True)

# Сортування за ім'ям в алфавітному порядку
df.sort_values(by=['Ім\'я'], inplace=True)

# Збереження в форматі CSV
df.to_csv('output.csv', index=False, encoding='utf-8')
