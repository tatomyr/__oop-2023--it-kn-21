from flask import Blueprint, app, request, jsonify
from models import User, Equipment, RentalTransaction
from auth import token_required, admin_required
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from config import Config
from flask import jsonify
from models import Equipment, RentalTransaction
from datetime import datetime, timedelta

equipment_bp = Blueprint('equipment', __name__)

@equipment_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "message": "Everything is fine"}), 200

@equipment_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')  # За замовчуванням встановлюється роль 'user'
    print(data)

    # Перевірка чи користувач вже існує
    if User.objects(username=username).first() is not None:
        return jsonify({'error': 'Username already exists'}), 409

    if User.objects(email=email).first() is not None:
        return jsonify({'error': 'Email already exists'}), 409

    # Генерація хешу пароля
    password_hash = generate_password_hash(password)

    # Створення нового користувача
    user = User(username=username, email=email, password_hash=password_hash, role=role).save()

    return jsonify({'message': 'User created successfully'}), 201

@equipment_bp.route('/login', methods=['POST'])
def login():
    # Отримати дані з запиту
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Знайти користувача в базі даних
    user = User.objects(username=username).first()

    # Перевірити існування користувача та вірність пароля
    if user and check_password_hash(user.password_hash, password):
        # Створення JWT токена
        token = jwt.encode({
          'username': user.username,
           'role': user.role,  # Додаємо роль користувача
         }, Config.SECRET)

        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
    
@equipment_bp.route('/create_equipment', methods=['POST'])
@token_required
@admin_required
def create_equipment():
    data = request.json
    name = data.get('name')
    type = data.get('type')

    if Equipment.objects(name=name).first() is not None:
      return jsonify({'error': 'Equipment name already exists'}), 409

    # Створення нової одиниці техніки
    equipment = Equipment(name=name, type=type, status='available').save()


    print(equipment)

    return jsonify({"id": str(equipment.id)}), 201

@equipment_bp.route('/rent_equipment', methods=['POST'])
@token_required  # Використовуйте декоратор, який перевіряє аутентифікацію користувача
def rent_equipment(current_user):
    data = request.json
    equipment_id = data.get('equipment_id')
    rental_start = datetime.now()
    rental_end = datetime.now() + timedelta(days=1)

    equipment = Equipment.objects(id=equipment_id, status='available').first()

    if not equipment:
        return jsonify({'message': 'Equipment not available'}), 404

    # Створення орендної транзакції
    rental = RentalTransaction(
        equipment=equipment,
        renter=current_user,
        rental_start=rental_start,
        rental_end=rental_end
    ).save()

    # Оновлення статусу техніки
    equipment.update(status='rented')

    return jsonify({'message': 'Equipment rented successfully'}), 201

@equipment_bp.route('/delete_equipment', methods=['POST'])
@token_required  # Використовуйте декоратор, який перевіряє аутентифікацію користувача
@admin_required
def delete_equipment(current_user):
    # Пошук та видалення обладнання
    data = request.json
    equipment_id = data.get('equipment_id')
    equipment = Equipment.objects(id=equipment_id).first()

    if not equipment:
        return jsonify({'message': 'No equipment found'}), 404

    equipment.update(status='deleted')
    return jsonify({'message': 'Equipment deleted successfully'}), 200



@equipment_bp.route('/equipment-usage-stats')
@token_required
def equipment_usage_stats(current_user):
    end_date = datetime.now() + timedelta(days=365)
    start_date = datetime.now() - timedelta(days=365)  # Одн рік тому

    print(f"Start date: {start_date}, End date: {end_date}")

    stats = []
    for equipment in Equipment.objects:
        rental_count = RentalTransaction.objects(
            equipment=equipment,
            rental_start__gte=start_date,
            rental_end__lte=end_date
        ).count()

        print(f"Equipment: {equipment.name}, Rental count: {rental_count}")

        stats.append({
            'equipment_id': str(equipment.id),
            'name': equipment.name,
            'rental_count': rental_count,
            'type': equipment.type,
            'status': equipment.status
        })

    return jsonify(stats)
