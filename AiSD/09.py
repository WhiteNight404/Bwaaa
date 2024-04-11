def car_info(brand='Audi', model='A4', color='черного', year=2010, mileage=150000, number_plate='А111АА77', price=900000):
    print(f"Марка: {brand}, модель: {model}, цвет: {color}, {year} года выпуска с пробегом: {mileage} км, с номерным знаком: {number_plate}. Цена: {price} рублей.")

c1 = {'brand': 'BMW', 'model': 'X5', 'color': 'белый', 'year': 2006, 'mileage': 215000, 'number_plate': 'X012АМ77', 'price': 1115000}
c2 = {'brand': 'Mercedes', 'year': 2015, 'mileage': 1000000, 'price': 1500000}

car_info(**c1)
car_info(**c2)