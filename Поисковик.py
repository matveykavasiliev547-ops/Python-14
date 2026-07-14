from playwright.sync_api import sync_playwright
import time
import random
from datetime import datetime


class Request:
    
    @staticmethod 
    def beginning():
        print("-" * 45)
        print("?-|Поисковик|-?")
        request = input("Введите запрос в умный поисковик: ")
        return request


class Smarty_search:
    
    @staticmethod
    def run_search(request):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            try:
                page.goto("https://duckduckgo.com")
                page.wait_for_load_state("networkidle")
                time.sleep(random.uniform(2,4))

                page.fill('input[name="q"]', request)
                time.sleep(random.uniform(1,3))

                page.keyboard.press("Enter")
                time.sleep(random.uniform(2,4))

                current_date = datetime.now().strftime('%d.%m.%Y')

                with open('history_search.txt', 'a', encoding='utf-8') as f:
                          f.write(f"['{request}': запрос был сделан - {current_date}]\n")

            except Exception as e:
                print(f"Ошибка: {e}")

            input("Если нашли то что хотели, посмотрите информацию и выключите браузер пожалуйста... :3")
            browser.close()
    
user_request = Request.beginning()
Smarty_search.run_search(user_request)
