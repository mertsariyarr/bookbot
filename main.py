from stats import word_counter, char_counter,new_sorted

def main():
      path = "books/frankenstein.txt"
      text = get_book_text(path)
      num_words = word_counter(text)
      my_chars = char_counter(text)
      print("============ BOOKBOT ============")
      print(f"Analzying book found at {path}...")
      print("----------- Word Count ----------")
      print(f"Found {num_words} total words")
      print("--------- Character Count -------")
      new_sorted(my_chars)
      
    

def get_book_text(path):
        with open(path) as f:
            book_output = f.read()
        return book_output

main()