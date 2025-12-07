def word_counter(book):
     return len(book.split())

def char_counter(book):
     myDict = {}
     for char in book:
          if char.lower() in myDict:
               myDict[char.lower()] += 1
          else:
               myDict[char.lower()] = 1
     return myDict