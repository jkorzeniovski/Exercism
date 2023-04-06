import string

def is_pangram():
  if alphabet - sentence_set == ([]):
    print("its a pangram")
  else:
    print("its not a pangram")
    

alphabet = set(string.ascii_lowercase)
print(type(alphabet))

sentence = input("ur sentence: ")
sentence_set = set(sentence.lower())
print(sentence_set)
print(type(sentence_set))

is_pangram()
