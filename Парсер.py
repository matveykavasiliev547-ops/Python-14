import asyncio
import httpx
import pandas as pd
from bs4 import BeautifulSoup


class BaseParser:
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }


class AsyncBookParser(BaseParser):
    def __init__(self, pages: int = 3):
        self.pages = pages
        self.results: list[dict] = []

    async def fetch_page(self, client: httpx.AsyncClient, page: int) -> str | None:
        url = self.base_url.format(page)
        try:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            return response.text
        except httpx.ConnectError:
            print(f"❌ [Стр. {page}] Ошибка сети: сервер недоступен.")
        except httpx.TimeoutException:
            print(f"⏳ [Стр. {page}] Таймаут запроса.")
        except httpx.HTTPStatusError as e:
            print(f"⚠️ [Стр. {page}] HTTP ошибка: {e.response.status_code}")
        except Exception as e:
            print(f"💥 [Стр. {page}] Непредвиденный сбой: {e}")
        return None

    def parse_html(self, html: str, page: int) -> list[dict]:
        soup = BeautifulSoup(html, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        parsed_items = []

        for book in books:
            title = book.find("h3").find("a")["title"]
            price = book.find("p", class_="price_color").text.strip()
            availability = book.find("p", class_="instock availability").text.strip()

            parsed_items.append({
                "Страница": page,
                "Название": title,
                "Цена": price,
                "Наличие": availability,
            })
        return parsed_items

    async def run(self):
        print(f"🚀 Запускаю асинхронный парсинг ({self.pages} стр.)...")
        async with httpx.AsyncClient(headers=self.headers, follow_redirects=True) as client:
            tasks = [self.fetch_page(client, page) for page in range(1, self.pages + 1)]
            html_pages = await asyncio.gather(*tasks)

        for page_num, html in enumerate(html_pages, start=1):
            if html:
                items = self.parse_html(html, page_num)
                self.results.extend(items)
                print(f"✅ Страница {page_num}: собрано {len(items)} позиций.")

        print(f"\n📦 Итого собрано товаров: {len(self.results)}")

    def export_data(self, filename: str = "books_catalog"):
        if not self.results:
            print("⚠️ Нет данных для экспорта.")
            return

        df = pd.DataFrame(self.results)

        csv_path = f"{filename}.csv"
        xlsx_path = f"{filename}.xlsx"

        # utf-8-sig нужен, чтобы Excel на Windows не ломал кириллицу и символ £
        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        df.to_excel(xlsx_path, index=False, engine="openpyxl")

        print(f"💾 Данные сохранены в '{csv_path}' и '{xlsx_path}'")


async def main():
    parser = AsyncBookParser(pages=5)
    await parser.run()
    parser.export_data("books_catalog")


if __name__ == "__main__":
    asyncio.run(main())