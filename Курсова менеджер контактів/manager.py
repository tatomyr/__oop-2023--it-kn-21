class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return f"Ім'я: {self.name}\nТелефон: {self.phone}\nEmail: {self.email}"

    def get_contact(self):
        return self.name, self.phone, self.email

    def set_contact(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email