class Car():
  """Простая модель автомобиля."""
  def __init__(self, make, model, year):
    """Инициализирует	атрибуты	описания	автомобиля."""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0


  def get_descriptive_name(self):
    """Возвращает аккуратно отформатированное описание."""
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()

  def read_odometer(self):
    """Выводит пробег машины в милях."""
    print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
