def count_words(filename):
  """Подсчет приблизительного количества строк в файле."""
  try:
    with open(filename) as f_obj:
      contents = f_obj.read()
  except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
  else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
	
filenames = ['alice.txt', 'alice1.txt', 'programming1.txt', 'programming2.txt']
for filename in filenames:
  count_words(filename)