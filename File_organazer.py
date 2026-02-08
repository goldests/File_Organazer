import sys
import os
import shutil
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui_main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.current_folder = ""
        
        
        self.setup_connections()
        
       
        self.setup_ui()
        
        
        self.setWindowTitle("📁 Организатор файлов")
    
    def setup_connections(self):
        """Подключение ВСЕХ кнопок"""
        # Кнопки выбора папки
        self.btnSelectFolder.clicked.connect(self.select_folder)
        
        # Основные кнопки сортировки
        self.btnQuickSort.clicked.connect(self.quick_sort_all)
        self.btnMoveToFolder.clicked.connect(self.move_to_folder)
        
        # двойной клик по файлу открывает его
        if hasattr(self, 'listWidgetFiles'):
            self.listWidgetFiles.itemDoubleClicked.connect(self.open_file)
    
    def setup_ui(self):
        """Дополнительная настройка UI"""
        # Включаем множественный выбор файлов!
        if hasattr(self, 'listWidgetFiles'):
            self.listWidgetFiles.setSelectionMode(QAbstractItemView.ExtendedSelection)
            
            
            self.listWidgetFiles.setStyleSheet("""
                QListWidget {
                    background-color: #2f3542;
                    color: #ffffff;
                    font-size: 14px;
                    border: 2px solid #70a1ff;
                    border-radius: 5px;
                }
                QListWidget::item {
                    background-color: #2f3542;
                    color: #ffffff;
                    padding: 5px;
                    border-bottom: 1px solid #3742fa;
                }
                QListWidget::item:selected {
                    background-color: #5352ed;
                    color: white;
                }
            """)
        
        
        if hasattr(self, 'listWidgetStats'):
            self.listWidgetStats.setStyleSheet("""
                QListWidget {
                    background-color: #2f3542;
                    color: #ffffff;
                    font-size: 14px;
                    border: 2px solid #70a1ff;
                    border-radius: 5px;
                }
                QListWidget::item {
                    background-color: #2f3542;
                    color: #ffffff;
                    padding: 5px;
                    border-bottom: 1px solid #3742fa;
                }
            """)
    
    def select_folder(self):
        """Выбор папки - ОСНОВНАЯ ФУНКЦИЯ"""
        folder = QFileDialog.getExistingDirectory(
            self, "Выберите папку", 
            self.current_folder or str(Path.home() / "Downloads")
        )
        
        if folder:
            self.current_folder = folder
            self.labelFolderPath.setText(folder)
            self.load_files()
            self.log_message(f"📂 Открыта папка: {folder}")
    
    def load_files(self):
        """Загрузка всех файлов из папки"""
        if not self.current_folder or not os.path.exists(self.current_folder):
            self.log_message("❌ Папка не существует!")
            return
        
       
        if hasattr(self, 'listWidgetFiles'):
            self.listWidgetFiles.clear()
        
        
        if hasattr(self, 'listWidgetStats'):
            self.listWidgetStats.clear()
        
        try:
            
            all_items = os.listdir(self.current_folder)
            files = []
            
            for item in all_items:
                full_path = os.path.join(self.current_folder, item)
                if os.path.isfile(full_path):
                    files.append(item)
            
            # Сортируем по имен
            files.sort()
            
            # Заполняем список 
            if hasattr(self, 'listWidgetFiles'):
                for filename in files:
                    item = QListWidgetItem(filename)
                    
                    
                    ext = os.path.splitext(filename)[1].lower()
                    item.setForeground(self.get_file_color(ext))
                    
                    
                    icon = self.get_file_icon(ext)
                    item.setText(f"{icon} {filename}")
                    
                    self.listWidgetFiles.addItem(item)
            
            # Показываем статистику
            self.show_statistics(files)
            
            self.log_message(f"✅ Загружено {len(files)} файлов")
            
        except PermissionError:
            self.log_message("❌ Нет доступа к папке!")
            QMessageBox.warning(self, "Ошибка", "Нет доступа к этой папке!")
        except Exception as e:
            self.log_message(f"❌ Ошибка: {str(e)}")
    
    def show_statistics(self, files):
        """Показ статистики по файлам"""
        if not hasattr(self, 'listWidgetStats'):
            return
            
        
        file_counts = {}
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext:
                file_counts[ext] = file_counts.get(ext, 0) + 1
            else:
                file_counts["без расширения"] = file_counts.get("без расширения", 0) + 1
        
        
        self.listWidgetStats.addItem(f"📊 Всего файлов: {len(files)}")
        self.listWidgetStats.addItem("─" * 30)
        
        
        sorted_counts = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)
        
        for ext, count in sorted_counts:
            if ext == "без расширения":
                text = f"📄 Без расширения: {count}"
            else:
                # Преобразуем .jpg в JPG
                ext_display = ext[1:].upper() if ext.startswith('.') else ext
                icon = self.get_file_icon(ext)
                text = f"{icon} {ext_display}: {count}"
            
            self.listWidgetStats.addItem(text)
    
    def move_to_folder(self):
        """Переместить выбранные файлы в новую папку"""
        if not self.current_folder:
            self.log_message("❌ Сначала выберите папку!")
            QMessageBox.warning(self, "Ошибка", "Сначала выберите папку!")
            return
        
        
        if not hasattr(self, 'listWidgetFiles'):
            QMessageBox.warning(self, "Ошибка", "Список файлов не найден!")
            return
        
        
        selected_items = self.listWidgetFiles.selectedItems()
        if not selected_items:
            self.log_message("❌ Выберите файлы для перемещения!")
            QMessageBox.warning(self, "Ошибка", "Выберите файлы для перемещения!")
            return
        
        # Получаем название папки из поля ввода
        if not hasattr(self, 'lineEditFolderName'):
            QMessageBox.warning(self, "Ошибка", "Поле для ввода названия папки не найдено!")
            return
            
        folder_name = self.lineEditFolderName.text().strip()
        if not folder_name:
            self.log_message("❌ Введите название папки!")
            QMessageBox.warning(self, "Ошибка", "Введите название папки в поле выше!")
            return
        
        # Создаем папку
        target_folder = os.path.join(self.current_folder, folder_name)
        
        try:
            os.makedirs(target_folder, exist_ok=True)
            self.log_message(f"📁 Создана папка: {folder_name}")
        except Exception as e:
            self.log_message(f"❌ Ошибка создания папки: {str(e)}")
            return
        
        
        moved_count = 0
        failed_count = 0
        
        for item in selected_items:
            # Извлекаем имя файла
            text = item.text().strip()
            
            # Убираем иконку
            if ' ' in text:
                parts = text.split(' ', 1)
                if len(parts) > 1:
                    filename = parts[1].strip()
                else:
                    filename = text
            else:
                filename = text
            
            filename = filename.strip()
            
            source = os.path.join(self.current_folder, filename)
            destination = os.path.join(target_folder, filename)
            
            try:
                
                counter = 1
                while os.path.exists(destination):
                    name, ext = os.path.splitext(filename)
                    new_name = f"{name}_{counter}{ext}"
                    destination = os.path.join(target_folder, new_name)
                    counter += 1
                
                shutil.move(source, destination)
                moved_count += 1
                self.log_message(f"   → {filename}")
                
            except Exception as e:
                failed_count += 1
                self.log_message(f"   ✗ Ошибка: {filename} - {str(e)}")
        
        
        self.load_files()
        
        # результат
        if failed_count == 0:
            self.log_message(f"✅ Успешно перемещено {moved_count} файлов")
            QMessageBox.information(self, "Готово", 
                                  f"Перемещено {moved_count} файлов в папку '{folder_name}'")
        else:
            self.log_message(f"⚠️  Перемещено {moved_count} файлов, ошибок: {failed_count}")
            QMessageBox.warning(self, "Частично выполнено",
                              f"Перемещено {moved_count} файлов\n"
                              f"Не удалось переместить: {failed_count}")
        
        # Очищаем поле ввода
        self.lineEditFolderName.clear()
    
    def quick_sort_all(self):
        """Быстрая сортировка ВСЕХ файлов по типам"""
        if not self.current_folder:
            self.log_message("❌ Сначала выберите папку!")
            QMessageBox.warning(self, "Ошибка", "Сначала выберите папку!")
            return
        
        # подтверждение
        reply = QMessageBox.question(
            self, "Подтверждение",
            "Выполнить быструю сортировку ВСЕХ файлов?\n"
            "Файлы будут автоматически разложены по папкам.",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply != QMessageBox.Yes:
            return
        
        # Категории для сортировки
        categories = {
            "Изображения": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
            "Документы": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt", ".rtf"],
            "Архивы": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Видео": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
            "Аудио": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
            "Программы": [".exe", ".msi", ".apk", ".jar"],
            "Торренты": [".torrent"],
        }
        
        self.log_message("🚀 Начинаю быструю сортировку...")
        
        # Получаем все файлы
        all_files = []
        if hasattr(self, 'listWidgetFiles'):
            for i in range(self.listWidgetFiles.count()):
                item = self.listWidgetFiles.item(i)
                text = item.text()
                
                # Извлекаем имя файла
                text = text.strip()
                if ' ' in text:
                    parts = text.split(' ', 1)
                    if len(parts) > 1:
                        filename = parts[1].strip()
                    else:
                        filename = text
                else:
                    filename = text
                
                filename = filename.strip()
                if filename:
                    all_files.append(filename)
        
        total_moved = 0
        
        
        for category, extensions in categories.items():
            files_in_category = []
            
            
            for filename in all_files[:]:
                ext = os.path.splitext(filename)[1].lower()
                if ext in extensions:
                    files_in_category.append(filename)
                    all_files.remove(filename)
            
            if files_in_category:
                
                category_folder = os.path.join(self.current_folder, category)
                os.makedirs(category_folder, exist_ok=True)
                
                # Перемещаем файлы
                for filename in files_in_category:
                    source = os.path.join(self.current_folder, filename)
                    destination = os.path.join(category_folder, filename)
                    
                    try:
                        # Проверка дубликатов
                        counter = 1
                        while os.path.exists(destination):
                            name, ext = os.path.splitext(filename)
                            new_name = f"{name}_{counter}{ext}"
                            destination = os.path.join(category_folder, new_name)
                            counter += 1
                        
                        shutil.move(source, destination)
                        total_moved += 1
                        
                    except Exception as e:
                        self.log_message(f"   ✗ {filename}: {str(e)}")
                
                self.log_message(f"   📁 {category}: {len(files_in_category)} файлов")
        
        # Оставшиеся файлы в папку "Разное"
        if all_files:
            other_folder = os.path.join(self.current_folder, "Разное")
            os.makedirs(other_folder, exist_ok=True)
            
            for filename in all_files:
                source = os.path.join(self.current_folder, filename)
                destination = os.path.join(other_folder, filename)
                
                try:
                    # Проверка дубликат
                    counter = 1
                    while os.path.exists(destination):
                        name, ext = os.path.splitext(filename)
                        new_name = f"{name}_{counter}{ext}"
                        destination = os.path.join(other_folder, new_name)
                        counter += 1
                    
                    shutil.move(source, destination)
                    total_moved += 1
                    
                except Exception as e:
                    self.log_message(f"   ✗ {filename}: {str(e)}")
            
            self.log_message(f"   📁 Разное: {len(all_files)} файлов")
        
        
        self.load_files()
        self.log_message(f"✅ Быстрая сортировка завершена!")
        self.log_message(f"📊 Перемещено файлов: {total_moved}")
        
        QMessageBox.information(self, "Готово", 
                              f"Отсортировано {total_moved} файлов!\n"
                              f"Созданы папки: Изображения, Документы, Архивы, и т.д.")
    
    
    def open_file(self, item):
        """Открыть файл по двойному клику"""
        if not self.current_folder:
            return
        
        
        text = item.text().strip()
        if ' ' in text:
            parts = text.split(' ', 1)
            if len(parts) > 1:
                filename = parts[1].strip()
            else:
                filename = text
        else:
            filename = text
            
        filepath = os.path.join(self.current_folder, filename)
        
        if os.path.exists(filepath):
            try:
                os.startfile(filepath)
                self.log_message(f"📂 Открыт файл: {filename}")
            except Exception as e:
                self.log_message(f"❌ Не удалось открыть файл: {filename}")
    
    def get_file_color(self, extension):
        """Цвет для типа файла"""
        colors = {
            '.jpg': QColor(255, 200, 100), '.jpeg': QColor(255, 200, 100),
            '.png': QColor(100, 200, 255), '.gif': QColor(255, 100, 200),
            '.pdf': QColor(255, 100, 100), '.doc': QColor(100, 150, 255),
            '.docx': QColor(100, 150, 255), '.xls': QColor(100, 200, 150),
            '.zip': QColor(255, 150, 50), '.rar': QColor(255, 150, 50),
            '.mp4': QColor(255, 100, 150), '.mp3': QColor(200, 100, 255),
            '.exe': QColor(255, 100, 100), '.py': QColor(100, 200, 255),
        }
        return colors.get(extension.lower(), QColor(200, 200, 200))
    
    def get_file_icon(self, extension):
        """Иконка для типа файла"""
        icons = {
            '.jpg': '🖼', '.jpeg': '🖼', '.png': '🖼', '.gif': '🖼',
            '.pdf': '📄', '.doc': '📝', '.docx': '📝',
            '.xls': '📊', '.xlsx': '📊',
            '.zip': '📦', '.rar': '📦',
            '.mp4': '🎬', '.avi': '🎬',
            '.mp3': '🎵', '.wav': '🎵',
            '.exe': '⚙️', '.msi': '⚙️',
            '.py': '🐍', '.js': '⚡',
            '.html': '🌐', '.htm': '🌐',
        }
        return icons.get(extension.lower(), '📄')
    
    def log_message(self, message):
        """Добавление сообщения в лог"""
        if hasattr(self, 'textEditLog'):
            timestamp = QDateTime.currentDateTime().toString("hh:mm:ss")
            self.textEditLog.append(f"[{timestamp}] {message}")
            
            scrollbar = self.textEditLog.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
        else:
            print(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())