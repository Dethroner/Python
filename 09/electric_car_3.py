class Car():
  """Простая	модель	автомобиля."""

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
	
  def get_descriptive_name(self):
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()
    
  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")
	
  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")
	
  def increment_odometer(self, miles):
    self.odometer_reading += miles

class Battery():
  """Простая модель аккумулятора электромобиля."""

  def __init__(self, battery_size=70):
    """Инициализирует атрибуты аккумулятора."""
    self.battery_size = battery_size
 
  def describe_battery(self):
    """Выводит информацию о мощности аккумулятора."""
    print("This car has a " + str(self.battery_size) + "-kWh battery.")			

class ElectricCar(Car):
  """Представляет аспекты машины, специфические для электромобилей."""
  def __init__(self, make, model, year):
    """Инициализирует атрибуты класса-родителя."""
    super().__init__(make, model, year)

    self.battery = Battery()
	
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

