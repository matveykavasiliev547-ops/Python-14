import asyncio
from api_client import AsyncJokesAPIClient
import customtkinter as ctk
import httpx

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')


class CyberJokesApp(ctk.CTk):

  def __init__(self, api_client: AsyncJokesAPIClient):
    super().__init__()

    self.api = api_client

    # Настройки окна (увеличили высоту под форму добавления)
    self.title('Garage & IT Jokes — Cyberpunk Edition')
    self.geometry('600x580')
    self.resizable(False, False)
    self.configure(fg_color='#121212')

    # --- Заголовок ---
    self.title_label = ctk.CTkLabel(
        self,
        text='⚡ RANDOM JOKE GENERATOR ⚡',
        font=ctk.CTkFont(family='Segoe UI', size=20, weight='bold'),
        text_color='#FFCC00',
    )
    self.title_label.pack(pady=(20, 5))

    # --- Карточка под текст шутки ---
    self.card_frame = ctk.CTkFrame(
        self,
        fg_color='#1E1E1E',
        border_color='#FFCC00',
        border_width=2,
        corner_radius=15,
    )
    self.card_frame.pack(fill='x', padx=30, pady=10)

    self.joke_label = ctk.CTkLabel(
        self.card_frame,
        text='Нажми кнопку ниже, чтобы зарядить порцию юмора! 🚀',
        font=ctk.CTkFont(family='Segoe UI', size=14),
        text_color='#E0E0E0',
        wraplength=480,
        justify='center',
    )
    self.joke_label.pack(fill='both', expand=True, padx=20, pady=20)

    self.id_label = ctk.CTkLabel(
        self.card_frame,
        text='ID: ---',
        font=ctk.CTkFont(family='Segoe UI', size=10, weight='bold'),
        text_color='#777777',
    )
    self.id_label.pack(anchor='se', padx=15, pady=(0, 10))

    # --- Кнопка следующей шутки ---
    self.next_btn = ctk.CTkButton(
        self,
        text='НЕКСТ ШУТКА 🎲',
        command=self.fetch_joke,
        font=ctk.CTkFont(family='Segoe UI', size=15, weight='bold'),
        fg_color='#FFCC00',
        text_color='#000000',
        hover_color='#E6B800',
        height=40,
        corner_radius=10,
    )
    self.next_btn.pack(pady=5, padx=30, fill='x')

    # --- Блок добавления своей шутки ---
    self.add_frame = ctk.CTkFrame(self, fg_color='transparent')
    self.add_frame.pack(fill='x', padx=30, pady=(15, 0))

    self.entry_label = ctk.CTkLabel(
        self.add_frame,
        text='➕ Добавь свой прикол в базу Postgres:',
        font=ctk.CTkFont(family='Segoe UI', size=12, weight='bold'),
        text_color='#888888',
    )
    self.entry_label.pack(anchor='w', pady=(0, 5))

    self.joke_entry = ctk.CTkEntry(
        self.add_frame,
        placeholder_text='Введи шутку про ваг, бэхи или питон...',
        font=ctk.CTkFont(family='Segoe UI', size=13),
        fg_color='#1E1E1E',
        border_color='#444444',
        text_color='#FFFFFF',
        height=38,
        corner_radius=8,
    )
    self.joke_entry.pack(fill='x', pady=(0, 10))

    self.add_btn = ctk.CTkButton(
        self.add_frame,
        text='СОХРАНИТЬ В БАЗУ 💾',
        command=self.send_joke,
        font=ctk.CTkFont(family='Segoe UI', size=13, weight='bold'),
        fg_color='#28A745',  # Зеленый акцент
        text_color='#FFFFFF',
        hover_color='#218838',
        height=38,
        corner_radius=8,
    )
    self.add_btn.pack(fill='x')

  def fetch_joke(self):
    try:
      # Асинхронный вызов через asyncio.run для интеграции с GUI
      data = asyncio.run(self.api.get_random_joke())
      self.joke_label.configure(text=data['joke'])
      self.id_label.configure(text=f"ID: #{data['id']}")
    except httpx.ConnectError:
      self.joke_label.configure(
          text=(
              '❌ Сервер FastAPI недоступен!\nУбедись, что Docker-контейнеры'
              ' запущены.'
          )
      )
      self.id_label.configure(text='ID: ERR')
    except httpx.HTTPStatusError as e:
      if e.response.status_code == 404:
        self.joke_label.configure(
            text='⚠️ База шуток пуста! Запусти Seed.py или добавь первую шутку.'
        )
      else:
        self.joke_label.configure(text=f'❌ Ошибка сервера: {e}')
      self.id_label.configure(text='ID: ERR')
    except Exception as e:
      self.joke_label.configure(text=f'❌ Неизвестная ошибка: {e}')
      self.id_label.configure(text='ID: ERR')

  def send_joke(self):
    text = self.joke_entry.get().strip()
    if not text:
      return

    try:
      # Асинхронный запуск добавления шутки через API-клиент
      res = asyncio.run(self.api.add_joke(text))
      self.joke_entry.delete(0, 'end')  # Очищаем поле ввода
      self.joke_label.configure(
          text=f"✅ Заброшено в Postgres!\n\n«{res['text']}»"
      )
      self.id_label.configure(text=f"ID: #{res['id']}")
    except httpx.ConnectError:
      self.joke_label.configure(text='❌ Сервер FastAPI недоступен!')
      self.id_label.configure(text='ID: ERR')
    except Exception as e:
      self.joke_label.configure(text=f'❌ Ошибка при отправке: {e}')
      self.id_label.configure(text='ID: ERR')


if __name__ == '__main__':
  client = AsyncJokesAPIClient(base_url='http://127.0.0.1:8000')
  app = CyberJokesApp(api_client=client)
  app.mainloop()