# Фіксовані ціни
COST_SGL = 150  # Вартість одномісного номера на добу
COST_TWIN = 190  # Вартість двомісного номера на добу
COST_POOL = 35  # Вартість оренди басейну за годину (макс. 3 особи на доріжку)
COST_GYM = 200 / 2  # Вартість спортзалу (200$ за 2 години, тобто 100$ за годину)
COST_LUNCH = 35  # Вартість обіду на людину
COST_DINNER = 45  # Вартість вечері на людину
TRANSFER_AIRPORT = 1600  # Трансфер аеропорт-готель-20 pax
TRANSFER_POOL_HOTEL = 5750  # Трансфер басейн-готель

# Дані про групи
groups = [
    {"name": "Group 1", "athletes": 15, "coaches": 5, "days": 15, "pool_hours": 5, "gym_hours": 3,
     "lunch_days": 15, "dinner_days": 15, "twin_rooms": 7, "sgl_rooms": 6},
    {"name": "Group 2", "athletes": 18, "coaches": 6, "days": 15, "pool_hours": 6, "gym_hours": 4,
     "lunch_days": 15, "dinner_days": 15, "twin_rooms": 9, "sgl_rooms": 6}
]

# Функція розрахунку вартості

def calculate_cost(group):
    # Проживання
    accommodation_cost = (group["twin_rooms"] * COST_TWIN + group["sgl_rooms"] * COST_SGL) * group["days"]
    
    # Харчування
    food_cost = (group["athletes"] + group["coaches"]) * (group["lunch_days"] * COST_LUNCH + group["dinner_days"] * COST_DINNER)
    
    # Басейн (враховуємо, що 3 особи на доріжку)
    lanes_needed = -(- (group["athletes"] + group["coaches"]) // 3)  # Округлення вгору
    pool_cost = lanes_needed * COST_POOL * group["pool_hours"]
    
    # Спортзал
    gym_cost = group["gym_hours"] * COST_GYM
    
    # Трансфери
    transfer_cost = TRANSFER_AIRPORT + TRANSFER_POOL_HOTEL
    
    # Загальна вартість
    total_cost = accommodation_cost + food_cost + pool_cost + gym_cost + transfer_cost
    
    return total_cost

# Обчислення вартості для кожної групи
for group in groups:
    cost = calculate_cost(group)
    print(f"{group['name']} - Total cost: ${cost}")
