class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_price):
        self._price = shirt_price
        self.color = shirt_color
        self.size = shirt_size

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        self._price = new_price

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size


shirt_one = Shirt('Purple', 'M', 25)

print(shirt_one.get_price())


class Pants:
    def __init__(self, pant_color, pant_waist_size, pant_length, pant_price):
        self.color = pant_color
        self.waist_size = pant_waist_size
        self.length = pant_length
        self.price = pant_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


class SalesPerson:
    def __init__(self, sales_person_first_name, sales_person_last_name, sales_person_employee_id, sales_person_salary,
                 sales_person_pants_sold=None, sales_person_total_sales = 0):

        if sales_person_pants_sold is None:
            sales_person_pants_sold = []

        self.first_name = sales_person_first_name
        self.last_name = sales_person_last_name
        self.employee_id = sales_person_employee_id
        self.salary = sales_person_salary
        self.pants_sold = sales_person_pants_sold
        self.total_sales = sales_person_total_sales

    def sell_pants(self, pant):
        self.pants_sold.append(pant)

    def display_sales(self):
        for pant in self.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}'.format(pant.color, pant.waist_size, pant.length,
                                                                            pant.price))

    def calculate_sales(self):
        self.total_sales = 0
        for pant in self.pants_sold:
            self.total_sales += pant.price

        return self.total_sales

    def calculate_commission(self, commission_percentage):
        self.total_sales = 0
        for pant in self.pants_sold:
            self.total_sales += pant.price

        return self.total_sales * commission_percentage


def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)

    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0

    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color

    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)

    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(), 2) == 47.36
    assert round(salesperson.calculate_commission(.1), 2) == 4.74

    print('Great job, you made it to the end of the code checks!')


check_results()

pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

salesperson.sell_pants(pants_one)
salesperson.sell_pants(pants_two)
salesperson.sell_pants(pants_three)

salesperson.display_sales()