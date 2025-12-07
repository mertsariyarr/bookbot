def word_counter(book):
     return len(book.split())

def char_counter(book):
     myDict = {}
     for char in book:
          if char.isalpha():
            if char.lower() in myDict:
                myDict[char.lower()] += 1
            else:
                myDict[char.lower()] = 1
     return myDict


def sort_on(items):
     return items["num"]


def new_sorted(word_dict):
      myList = []
      for item in word_dict.keys():
            myList.append({"char": item, "num": word_dict[item]})               
      myList.sort(reverse=True, key=sort_on)
      for item in myList:
            print(f"{item['char']}: {item['num']}")
      
