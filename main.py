def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents


def main():
  from stats import get_word_count, get_character_dict, get_sorted_dict
  import sys
  if len(sys.argv) != 2: 
    print("Bookbot program requires two args, first is main.py and second is the path to the book for analysis.\nUsage: python3 main.py <path_to_book>\nPlease fix and rerun.")
    sys.exit(1)
  file = sys.argv[1]
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