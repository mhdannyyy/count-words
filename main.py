#Program 1: Count Words
#Name: Muhammad Danish bin Zaini
#Student ID: 2024275948

sentence = input("Enter a sentence: ")

if sentence.strip() == "":
    print("No sentence was entered.")
else:
    words = sentence.split()
    print("Number of words:", len(words))