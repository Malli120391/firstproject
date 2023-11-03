punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str1 = "Hello!!!, then{}{}^^, he said$$$ ---and \\went...."

#my_str1 = input("Enter your string here!: ")
no_punctuation = ""
for char in my_str1:
    if char not in punctuation:
        no_punctuation = no_punctuation + char
print(no_punctuation)
