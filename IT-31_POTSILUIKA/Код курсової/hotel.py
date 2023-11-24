import sqlite3

class Hotel:
    def __init__(self):
        self.conn = sqlite3.connect('hotel.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rooms (
                room_number TEXT PRIMARY KEY,
                capacity INTEGER,
                amenities TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id INTEGER PRIMARY KEY,
                room_number TEXT,
                date TEXT,
                FOREIGN KEY (room_number) REFERENCES rooms(room_number)
            )
        ''')
        self.conn.commit()

    def add_room(self, room_number, capacity, amenities):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO rooms (room_number, capacity, amenities)
            VALUES (?, ?, ?)
        ''', (room_number, capacity, amenities))
        self.conn.commit()

    def check_availability(self, date):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT room_number FROM rooms
            WHERE room_number NOT IN (
                SELECT room_number FROM bookings
                WHERE date = ?
            )
        ''', (date,))
        available_rooms = [row[0] for row in cursor.fetchall()]
        return available_rooms

    def book_room(self, room_number, date):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO bookings (room_number, date)
            VALUES (?, ?)
        ''', (room_number, date))
        self.conn.commit()
        print(f"Номер {room_number} успішно заброньовано на {date}.")

    def close_connection(self):
        self.conn.close()
