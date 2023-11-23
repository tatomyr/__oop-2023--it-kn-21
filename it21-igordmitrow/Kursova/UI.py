from service import DeezerService, YoutubeService
from player import MusicPlayer
import tkinter as tk
from tkinter import Entry, Listbox, Button, Label
from server import app as server
import webbrowser
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import os
class UserInterface():
    def __init__(self) -> None:
        """
        Initialize the user interface
        @return: None
        """
        self.service = None

    def get_search_query(self) -> None:
        """
        Get the search query from the user

        @return: The search query
        """
        pass

    def display_results(self, results: list) -> None:
        """
        Display the results of the search
        @param results: The results to display
        @return: None
        """
        pass

    def display_download_status(self, status: str) -> None:
        """
        Display the download status
        @param status: The status to display
        @return: None
        """
        pass

    def get_track_selection(self, results: list) -> None:
        """
        Get the track selection from the user
        @param results: The results to select from
        @return: None
        """
        pass

    def start_music_player(self) -> None:
        """
        Start the music player
        @return: None
        """
        player = MusicPlayer()
        player.run()

    def run(self) -> None:
        """
        Run the user interface
        @return: None
        """
        pass


class CommandLineUI(UserInterface):
        
    def get_search_query(self) -> str:
        return input("Введіть запит для пошуку музики або вставте Ютуб посилання (введіть 1, щоб відкрити музичний плеєр): ")

    def is_youtube_link(self, query: str) -> bool:
        # Перевірка на посилання
        return 'youtu' in query and '.com' in query

    def handle_youtube_link(self, query: str) -> None:
        # Обробка посилання
        self.service = YoutubeService()
        self.display_download_status('Початок завантаження')
        status = self.service.start_downloading(query)
        if status: 
            self.display_download_status('Завантажено успішно!')

    def is_music_player_command(self, query: str) -> bool:
        # Перевірка на команду відкриття музичного плеєра
        return query == '1'

    def search_deezer(self, query: str) -> None:
        # Пошук треків на Deezer
        self.service = DeezerService()
        results = self.service.search_music(query)[:10]

        if results:
            print("Результати пошуку:")
            for i, result in enumerate(results, start=1):
                print(f"{i}. {result['title']} - {result['artist']['name']}")
            self.get_track_selection(results)
        else:
            print("Немає результатів для відображення.")

    def display_results(self, query: str) -> None:
        if self.is_youtube_link(query):
            self.handle_youtube_link(query)
        elif self.is_music_player_command(query):
            self.start_music_player()
        else:
            self.search_deezer(query)

    def display_download_status(self, status):
        print(f"Статус завантаження: {status}")

    def get_track_selection(self, results) -> None:
        while True:
            try:
                choice = int(input("Виберіть номер треку для завантаження (або 0 для скасування): "))
                if choice == 0:
                    return
                if 0 <= choice <= len(results):
                    status = self.service.start_downloading(results[choice - 1])
                    if status:
                        return self.display_download_status('Успішно завантажено!')
                    else:
                        return self.display_download_status('Помилка завантаження!')
                else:
                    print("Недійсний вибір. Спробуйте ще раз.")
            except ValueError:
                print("Недійсний вибір. Введіть номер треку.")

    def run(self) -> None:
        while True:
            query = self.get_search_query()
            self.display_results(query)

class WebUI(UserInterface):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self) -> None:
        webbrowser.open('http://localhost:5001/')
        server.run(host='localhost', port='5001')

class GUI(UserInterface):
    def __init__(self):
        # Ініціалізація графічного інтерфейсу
        self.root = tk.Tk()
        self.root.title("Завантажувач музики")
        self.results = []

        # Ініціалізація сервісу
        self.service = DeezerService()

        # Відображення запиту для пошуку
        self.label = Label(self.root, text="Введіть запит для пошуку")
        self.entry = Entry(self.root)
        self.entry.bind("<Return>", self.get_search_query)

        self.status = None
        self.listbox = Listbox(self.root, selectmode=tk.MULTIPLE)

        # Відображення кнопки завантаження треків та кнопки відтворення музики
        self.download_button = Button(self.root, text="Скачати", command=self.get_track_selection)
        self.play_button = Button(self.root, text="Відтворити музику", command=self.start_music_player)

        self.display_results("")
        self.show_elements(self.label, self.entry, self.play_button)


    # Відображення та приховування елементів
    def hide_elements(self, *elements):
        for element in elements:
            element.pack_forget()

    def show_elements(self, *elements):
        for element in elements:
            element.pack()

    
    def display_results(self, text):
        if text == "":
            self.hide_elements(self.listbox, self.download_button)
            return
        
        results = self.service.search_music(text)[:10]
        # Виведення результатів пошуку

        if results:
            self.results = results
            self.listbox.delete(0, tk.END)
            for i in range(10):
                self.listbox.insert(tk.END, f"{i+1}. {results[i]['title']} - {results[i]['artist']['name']}")
            self.hide_elements(self.play_button)
            self.show_elements(self.listbox, self.download_button, self.play_button)
        else:
            self.hide_elements(self.listbox, self.download_button)

    def display_download_status(self, status):
        if self.status:
            self.hide_elements(self.status_label, self.status)
        self.status_label = Label(self.root, text="Статус завантаження")
        self.status = Label(self.root, text=status)
        self.show_elements(self.status_label, self.status)
        self.root.update()

    def get_track_selection(self):
        selected_items = self.listbox.curselection()
        for index in selected_items:
            self.display_download_status(f"Скачування: {self.results[index]['title']} - {self.results[index]['artist']['name']}")
            self.service.start_downloading(self.results[index])
            self.display_download_status(f"Завантажено: {self.results[index]['title']} - {self.results[index]['artist']['name']}")
        
        self.listbox.selection_clear(0, tk.END)

    def get_search_query(self, event):
        text = self.entry.get()
        self.display_results(text)

    def run(self) -> None:
        self.root.mainloop()

class TelegramUI(UserInterface):
    def __init__(self) -> None:
        super().__init__()
        self.token = os.environ.get("TOKEN")
        self.service = DeezerService()

        self.app = ApplicationBuilder().token(self.token).build()
        self.app.add_handler(MessageHandler(filters.TEXT, self.get_search_query))
        self.app.add_handler(CallbackQueryHandler(self.get_track_selection))

    async def get_search_query(self, update, context):
        text = update.message.text
        results = self.service.search_music(text)[:10]
        await self.display_results(results, update)

    async def display_results(self, results, update):
        keyboard = []
        for result in results:
            keyboard.append([InlineKeyboardButton(f"{result['title']} - {result['artist']['name']}", callback_data=result['id'])])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Виберіть трек для завантаження:', reply_markup=reply_markup)

    async def display_download_status(self, status, update):
        await update.message.reply_text(status)

    async def get_track_selection(self, update, context):
        query = update.callback_query
        await query.answer()
        await self.display_download_status("Скачування", query)
        status = self.service.start_downloading(query.data, t='id')
        print(status)
        if status:
            await query.message.reply_audio(status)
            await self.display_download_status('Завантажено успішно!', query)
        else:
            await self.display_download_status('Помилка завантаження!', query)

    def run(self) -> None:
        print("Телеграм-бот запущено!\nПосилання на бота: https://t.me/YouTube_Spotify_Deezer_Bot")
        self.app.run_polling(drop_pending_updates=True)

def selectUI():
    """
    Select the user interface
    You can choose between a command line, web, or graphical user interface
    @return: The selected user interface

    """
    while True:
        try:
            choice = int(input("Виберіть тип інтерфейсу:\n1 - командний рядок,\n2 - веб,\n3 - графічний,\n4 - Telegram: "))
            if choice == 1:
                return CommandLineUI()
            elif choice == 2:
                return WebUI()
            elif choice == 3:
                return GUI()
            elif choice == 4:
                return TelegramUI()
            else:
                print("Недійсний вибір. Спробуйте ще раз.")
        except ValueError:
            print("Недійсний вибір. Введіть номер інтерфейсу.")
