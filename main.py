def main():
      path = "books/frankenstein.txt"
      text = get_book_text(path)
      num_words = word_counter(text)
      print(f"Found {num_words} total words")


def get_book_text(path):
        with open(path) as f:
            book_output = f.read()
        return book_output

    

def word_counter(book):
     return len(book.split())



main()