def get_word_count(book_text):
  word_list = book_text.split()
  return len(word_list)

def get_character_dict(book_text):
  character_dict = {}
  for char in book_text:
      lchar = char.lower()
      if lchar not in character_dict:
         character_dict[lchar] = 1
      else:
         character_dict[lchar] += 1
  return character_dict