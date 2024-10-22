# Создание пустого списка для хранения пришельцев.
aliens = []
# Создание 30 зеленых	пришельцев.
for alien_number in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
  print(alien)
print("...")

# Вывод количества созданных пришельцев.
print("Total number of aliens: " + str(len(aliens)))
