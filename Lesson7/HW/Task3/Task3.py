# Задача 3. Удаление старых файлов
# Напишите скрипт, который удаляет файлы в указанном каталоге, которые не
# изменялись более заданного количества дней. Скрипт должен принимать путь к
# каталогу и количество дней.
# Подсказка № 1
# Используйте time.time() для получения текущего времени в секундах с начала
# эпохи (01.01.1970). Это поможет вам определить, сколько времени прошло с
# последнего изменения файлов.
# Подсказка № 2
# Преобразуйте количество дней в секунды для сравнения. Умножьте количество дней
# на 86400 (количество секунд в одном дне), чтобы получить пороговое значение
# времени.
# Подсказка № 3
# Используйте os.walk() для рекурсивного обхода всех каталогов и файлов в
# указанном каталоге. Это позволит вам проверить каждый файл, независимо от уровня
# вложенности.
# Подсказка № 4
# Для получения времени последнего изменения файла используйте
# os.path.getmtime(). Сравните это время с пороговым значением, чтобы
# определить, нужно ли удалить файл.
# Подсказка № 5
# Для удаления файлов используйте os.remove(). Убедитесь, что файл действительно
# нужно удалить, чтобы избежать случайного удаления важных данных.

import os
import time

def delete_old_files(directory, days):

    if not os.path.isdir(directory):
        print(f"Каталог '{directory}' не найден.")
        return

    current_time = time.time()
    time_threshold = days * 86400  

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            file_mtime = os.path.getmtime(file_path)
            
            if current_time - file_mtime > time_threshold:
                try:
                    os.remove(file_path)
                    print(f"Файл '{file_path}' удалён.")
                except Exception as e:
                    print(f"Не удалось удалить файл '{file_path}': {e}")

delete_old_files(
    directory="путь/к/каталогу",  
    days=30                        
)
