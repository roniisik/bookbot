def main():
      text = get_text("frankenstein.txt")
      
      print_report("frankenstein.txt", text)

def print_report(filename, text):
    word_count = count_words(text)
    char_count_dict = character_count(text)
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document\n")

    for char in char_count_dict:
        print(f"The {char} character was found {char_count_dict[char]} times")
        print("--- End report ---")       


def get_text(filename):
        with open(f"books/{filename}", "r") as f:
            return f.read()

def count_words(text):
        words = text.split()
        
        return len(words)

def character_count(text):
      dict1 = {}
      for char in text.lower():
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
      return dict1
    
    
main()
