# farm_classes.py

import json

class FarmTask:
    def __init__(self, name, duration, culture, field=None):
        self.name = name
        self.duration = duration
        self.culture = culture
        self.field = field

    def to_dict(self):
        if self.field:
            field_info = {
                'name': self.field.name,
                'size': self.field.size,
                'culture': self.field.culture
            }
        else:
            field_info = None

        task_info = {
            'name': self.name,
            'duration': self.duration,
            'culture': self.culture,
            'field': field_info
        }

        return task_info

    def __str__(self):
        task_info = f"Робота: {self.name}\n"
        task_info += f"Тривалість (дні): {self.duration}\n"
        task_info += f"Культура: {self.culture}\n"
        if self.field:
            task_info += f"Площа: {self.field.name}\n"
            task_info += f"Розмір площі (га): {self.field.size}\n"
        return task_info

class Field:
    def __init__(self, name, size, culture):
        self.name = name
        self.size = size
        self.culture = culture

    def to_dict(self):
        return {
            'name': self.name,
            'size': self.size,
            'culture': self.culture
        }