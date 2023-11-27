# farm_app.py

import os
import json
from PyQt5.QtWidgets import (
    QMainWindow, 
    QVBoxLayout, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QLineEdit, 
    QTextEdit, 
    QListWidget, 
    QInputDialog,
    QMessageBox
)
from PyQt5.QtGui import QIntValidator
from farm_classes import FarmTask, Field

class FarmSchedulerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.load_data()  # Завантаження даних при запуску

    def initUI(self):
        self.setWindowTitle('Сільськогосподарський розклад')
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.task_name_label = QLabel("Назва завдання:")
        self.task_name_input = QLineEdit()

        self.task_duration_label = QLabel("Тривалість (дні):")
        self.task_duration_input = QLineEdit()
        self.task_duration_input.setValidator(QIntValidator())  # Додавання валідатора для цілочисельних значень

        self.culture_label = QLabel("Культура:")
        self.culture_input = QLineEdit()

        self.field_label = QLabel("Площі під культурами:")
        self.field_list = QListWidget()
        self.field_list.itemClicked.connect(self.field_selected)

        self.task_list = QListWidget()
        self.task_list.itemClicked.connect(self.task_selected)

        self.add_task_button = QPushButton("Додати завдання")
        self.add_task_button.clicked.connect(self.add_task)

        self.remove_task_button = QPushButton("Видалити завдання")
        self.remove_task_button.clicked.connect(self.remove_task)

        self.add_field_button = QPushButton("Додати площу")
        self.add_field_button.clicked.connect(self.add_field)

        self.remove_field_button = QPushButton("Видалити площу")
        self.remove_field_button.clicked.connect(self.remove_field)

        self.schedule_display = QTextEdit()

        self.layout.addWidget(self.task_name_label)
        self.layout.addWidget(self.task_name_input)
        self.layout.addWidget(self.task_duration_label)
        self.layout.addWidget(self.task_duration_input)
        self.layout.addWidget(self.culture_label)
        self.layout.addWidget(self.culture_input)
        self.layout.addWidget(self.field_label)
        self.layout.addWidget(self.field_list)
        self.layout.addWidget(self.add_field_button)
        self.layout.addWidget(self.remove_field_button)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.add_task_button)
        self.layout.addWidget(self.remove_task_button)
        self.layout.addWidget(self.schedule_display)

        self.central_widget.setLayout(self.layout)

        self.schedule = []
        self.fields = []

    def add_task(self):
        task_name = self.task_name_input.text().strip()
        task_duration_text = self.task_duration_input.text().strip()
        culture = self.culture_input.text().strip()

        if not task_name or not task_duration_text or not culture:
            self.show_error_message("Помилка", "Будь ласка, заповніть всі поля.")
            return

        try:
            task_duration = int(task_duration_text)
        except ValueError:
            self.show_error_message("Помилка", "Тривалість має бути цілим числом.")
            return

        selected_item = self.field_list.currentItem()
        field = None
        if selected_item:
            field_name = selected_item.text()
            for f in self.fields:
                if f.name == field_name:
                    field = f
                    break

        task = FarmTask(task_name, task_duration, culture, field)
        self.schedule.append(task)
        self.update_schedule_display()
        self.task_list.addItem(task.name)
        self.clear_inputs()

    def remove_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_name = selected_item.text()
            for task in self.schedule:
                if task.name == task_name:
                    self.schedule.remove(task)
                    self.task_list.takeItem(self.task_list.row(selected_item))
                    self.clear_inputs()
                    break
        self.update_schedule_display()

    def update_schedule_display(self):
        schedule_text = "Сільськогосподарський розклад:\n"
        for task in self.schedule:
            schedule_text += str(task)
            schedule_text += "----------\n"
        self.schedule_display.setPlainText(schedule_text)

    def clear_inputs(self):
        self.task_name_input.clear()
        self.task_duration_input.clear()
        self.culture_input.clear()

    def add_field(self):
        field_name, ok = QInputDialog.getText(self, 'Додати площу', 'Введіть назву площі:')
        if ok:
            field_size_text, ok = QInputDialog.getText(self, 'Додати площу', 'Введіть розмір площі (га):')
            if ok:
                try:
                    field_size = float(field_size_text)
                except ValueError:
                    self.show_error_message("Помилка", "Розмір площі має бути числовим значенням.")
                    return

                field = Field(field_name, field_size, "")
                self.fields.append(field)
                self.field_list.addItem(field.name)

    def remove_field(self):
        selected_item = self.field_list.currentItem()
        if selected_item:
            field_name = selected_item.text()
            for field in self.fields:
                if field.name == field_name:
                    self.fields.remove(field)
                    self.field_list.takeItem(self.field_list.row(selected_item))
                    break

    def task_selected(self, item):
        task_name = item.text()
        for task in self.schedule:
            if task.name == task_name:
                self.task_name_input.setText(task.name)
                self.task_duration_input.setText(str(task.duration))
                self.culture_input.setText(task.culture)
                if task.field:
                    field_name = task.field.name
                    for i in range(self.field_list.count()):
                        if self.field_list.item(i).text() == field_name:
                            self.field_list.setCurrentRow(i)

    def field_selected(self, item):
        field_name = item.text()
        for field in self.fields:
            if field.name == field_name:
                self.field_list.setCurrentItem(item)

    def save_data(self):
        data = {
            'schedule': [task.to_dict() for task in self.schedule],
            'fields': [field.to_dict() for field in self.fields]
        }

        file_path = r'C:\kursova\farm_data.json'

        with open(file_path, 'w') as f:
            json.dump(data, f)

    def load_data(self):
        file_path = r'C:\kursova\farm_data.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)

            self.schedule = []
            for task_data in data.get('schedule', []):
                field_data = task_data.get('field')
                field = None
                if field_data:
                    field = Field(field_data['name'], field_data['size'], field_data['culture'])
                task = FarmTask(task_data['name'], task_data['duration'], task_data['culture'], field)
                self.schedule.append(task)

            self.fields = []
            for field_data in data.get('fields', []):
                field = Field(field_data['name'], field_data['size'], field_data['culture'])
                self.fields.append(field)

            self.update_schedule_display()

    def closeEvent(self, event):
        self.save_data()
        event.accept()

    def show_error_message(self, title, message):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.exec_()








