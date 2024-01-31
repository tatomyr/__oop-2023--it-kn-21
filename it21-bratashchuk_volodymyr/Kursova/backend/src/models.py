from mongoengine import Document, StringField, ReferenceField, DateTimeField

class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True)
    password_hash = StringField(required=True)
    role = StringField(required=True, default='user')  

class Equipment(Document):
    name = StringField(required=True)
    type = StringField(required=True)
    status = StringField(required=True)

class RentalTransaction(Document):
    equipment = ReferenceField(Equipment)
    renter = ReferenceField(User)
    rental_start = DateTimeField(required=True)
    rental_end = DateTimeField()


