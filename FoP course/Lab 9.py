def count_words(string, word):
    if not string:
        return 0
    if len(string) > 1:
        words = string.split(None, 1)
        print(words)
        if not words:
            return 0
        first_word, rest = words[0], words[1] if len(words) > 1 else ""
        if first_word == word:
            return 1 + count_words(rest, word)
        else:
            return count_words(rest, word)
print(count_words("Hello world", "ll"))


# def count(string, char):
#     if not string:
#         return 0
#     if string[0] == char:
#         return 1 + count(string[1:], char)
#     else:
#         return count(string[1:], char)
#
# string = input("Enter a string: ")
# char = input("Enter a character: ")
# print(char, count(string, char), string)


# def depunct(string):
#     if not string:
#         return ""
#     if string[0].isalpha():
#         return string[0] + depunct(string[1:])
#     else:
#         return depunct(string[1:])
#
#
# print(depunct(input("Enter a sentence: ")))
#


""""Bonus"""


# count_characters.py

def count_occurrences(s, target):
    if not s:
        return 0

    if len(target) > 1:
        words = s.split(None, 1)  # Split into the first word and the rest
        if not words:  # No more words
            return 0
        first_word, rest = words[0], words[1] if len(words) > 1 else ""
        if first_word == target:
            return 1 + count_occurrences(rest, target)  # Count the word and process the rest
        else:
            return count_occurrences(rest, target)  # Skip and process the rest

    # If the target is a single character
    if s[0] == target:
        return 1 + count_occurrences(s[1:], target)  # Count this occurrence and process the rest
    else:
        return count_occurrences(s[1:], target)  # Skip and process the rest


def main():
    # Prompt the user to enter a string
    s = input("Enter a string: ")
    # Prompt the user to enter the target (character or word) to count
    target = input("Enter the character or word to count: ")
    # Validate input for character/word
    if not target:
        print("Please enter a valid character or word.")
        return
    # Call the recursive function and display the result
    count = count_occurrences(s, target)
    print(f"'{target}' occurs {count} times in '{s}'")


if __name__ == "__main__":
    main()
