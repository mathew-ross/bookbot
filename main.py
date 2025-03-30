from stats import get_word_count, get_character_dict, get_sorted_dict

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents


def main():
  file = "books/frankenstein.txt"
  text = get_book_text(file)
  char_dict = get_character_dict(text)
  print(f"============ BOOKBOT ============\nAnalyzing books found at {file}...")
  print(f"----------- Word Count ----------\nFound {get_word_count(text)} total words")
  print(f"--------- Character Count -------")
  sorted_dict = get_sorted_dict(char_dict)
  for char in sorted_dict:
    if char.isalpha() is True:
      print(f"{char}: {sorted_dict[char]}")
  print("============= END ===============")

main()