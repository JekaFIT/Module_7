import os
import time

print('Директория:', os.getcwd())

# Создание или переход в директорию
if not os.path.exists('directory'):
    os.mkdir('directory')
os.chdir('directory')

# Создание тестовых файлов, если папка пуста
if not os.listdir('.'):
    for i in range(3):
        with open(f"test_file_{i + 1}.txt", 'w') as f:
            f.write(f"Это содержимое файла {i + 1}")

# Обход папок и файлов
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)

        # Время изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Размер файла
        filesize = os.path.getsize(filepath)

        # Родительская директория
        parent_dir = os.path.dirname(filepath)

        # Вывод информации
        print(f"Обнаружен файл: {file}")
        print(f"Полный путь: {filepath}")
        print(f"Размер: {filesize} байт")
        print(f"Время изменения: {formatted_time}")
        print(f"Родительская директория: {parent_dir}")
        print('-' * 40)
