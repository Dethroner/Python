def get_formatted_name(first_name, middle_name,	last_name):
  """Возвращает аккуратно отформатированное полное имя."""
  full_name = first_name + ' ' + middle_name + ' ' + last_name
  return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
