from datetime import datetime
import os
import shutil


class FileSorter:
    def __init__(self, directory: str):
        self.directory = directory

    def get_year(self, file_path: str) -> str:
        """Получает год последнего изменения файла."""
        timestamp = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(timestamp)
        return str(date.year)

    def sort_files(self) -> tuple[int, list[str]]:
        """
        Сортирует файлы по папкам годов.
        Возвращает количество перемещенных файлов и список ошибок.
        """
        if not os.path.exists(self.directory):
            raise ValueError("Указанный путь не существует")

        moved_count = 0
        errors = []

        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)

            # Пропускаем директории
            if os.path.isdir(file_path):
                continue

            try:
                year = self.get_year(file_path)
                year_dir = os.path.join(self.directory, year)

                if not os.path.exists(year_dir):
                    os.makedirs(year_dir)

                target_path = os.path.join(year_dir, filename)
                shutil.move(file_path, target_path)
                moved_count += 1
            except Exception as e:
                errors.append(f"{filename}: {e}")

        return moved_count, errors