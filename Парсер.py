import requests
from bs4 import BeautifulSoup

print("(00-ПАРСЕР-00)")

url = 'https://quotes.toscrape.com/'
print("1. Загружаю сайт...")

response = requests.get(url)

if response.status_code == 200:
    print("2. Сайт загружен! Начинаю разбор...")

    soup = BeautifulSoup(response.text,'html.parser')

    quotes = soup.find_all('span',class_='text')

    print("3. Найденные цитаты:")
    print("-" * 30)

    for quote in quotes:
        print(quote.text)

    print("-" * 30)
    print("4. Готово!")

else:
    print(f"Ошибка! Сайт вернул код: {response.status_code}")

