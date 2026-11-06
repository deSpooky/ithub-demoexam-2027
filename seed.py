import random

courses = ["ОАиП", "ОВД", "ВМ"]
payment_types = ["Наличные", "Перевод"]
statuses = ["Новая", "Идет обучение", "Обучение завершено"]

users = [
    { "login": f"testuser{ix}", "password": f"testpassword{ix}", "fullname": f"Тест Тестович{ix}", "phone": f"8(999)999-99-9{ix}", "email": f"testuser{ix}@gmail.com" }
    for ix in range(1, 5)
] + [
    { "login": "Admin1", "password": "KorokNET", "fullname": "Модератор", "phone": "8(991)999-99-99", "email": "koroknet@gmail.com", "role": "moderator" }
]

records = [
    { 
        "course": random.choice(courses), 
        "payment": random.choice(payment_types), 
        "date": "2026-11-06",
        "user_login": random.choice(users[:-1])["login"],
        "status": random.choice(statuses)
    }
    for _ in range(50)
]