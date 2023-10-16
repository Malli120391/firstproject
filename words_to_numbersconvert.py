
def words_to_number(input_string):
    # Define a mapping of words to digits
    word_map = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }

    # Split the input string into words and remove any empty strings
    words = input_string.split()
    words = [word for word in words if word]

    # Initialize an empty string to store the result
    result = ""

    # Iterate through the words in the input string
    for word in words:
        if word.lower() in word_map:
            # Convert words to digits using the mapping
            digit = word_map[word.lower()]
            result += digit
        else:
            result += word  # Keep non-matching words as is

    return result

# Test the function
input_string = "two zero nine six eight nine four six zero"
converted_number = words_to_number(input_string)
print(str(converted_number))  # Output: "209689460"
