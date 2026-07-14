from datetime import datetime
import os
import shutil

class FileSorter:
    def __init__(self, directory):
        self.directory = directory

    def get_year(self, file_path):
        timestamp = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(timestamp)
        return str(date.year)

    def sort_files(self):
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)

            if os.path.isdir(file_path) or filename == __file__:
                continue

            year = self.get_year(file_path)
            year_dir = os.path.join(self.directory, year)

            if not os.path.exists(year_dir):
                os.makedirs(year_dir)
   
            try:
                shutil.move(file_path, os.path.join(year_dir, filename))
                print(f"Перемещён:{filename} -> {year}/")
            except Exception as e:
                print(f"Ошибка при перемещении! {filename}: {e}")

            
if __name__ == "__main__":
    print("[-FILE_SORTER-]")
    road = input("Введите путь к папке для сортировки: ")
    if os.path.exists(road):
        sorter = FileSorter(road)
        sorter.sort_files()
        print("Готово! Папка отсортирована.")

    else:
        print("Путь не существует!")
        
        
        
