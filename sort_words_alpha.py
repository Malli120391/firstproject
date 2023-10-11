
#my_string = "HI i am this is my python programm for string to sort the words"

my_string = input("Enter your string here:")

words = [word.lower() for word in my_string.split()]

words.sort()

print("The sorted words are here:")
for word in words:
    print(word)


