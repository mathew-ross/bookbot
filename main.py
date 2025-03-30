from stats import get_word_count, get_character_dict

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents


def main():
  file = "books/frankenstein.txt"
  text = get_book_text(file)
  # print(text)
  print(f"{get_word_count(text)} words found in the document")
  print(get_character_dict(text))

main()