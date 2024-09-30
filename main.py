#In-Class Activity: Strings

'''Activity #1
A palindrome is a string that is the same forward as it is backwards
# There are multiple ways to achieve this, I can think of at least 3.
examples: racecar, mom, kayak'''
def is_palindrome(string):
    return string == string[::-1]

'''Activity #2
Write a function that counts the number of vowels in a string and returns the value
'''
def vowel_count(string):
    count = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            count += 1
    return count
'''Activity #3
Write a function that finds and returns the shortest word in a string'''
def shortest_word(string):
  words_to_ignore = "and, or, the, from, for, to"
  # Step #1 remove all commas and periods from the string
  # Step #2 At start, assume the first word is shortest word
  # Search for shortest word, make sure it
  # is not one of the words to ignore, from above
  # Hints: Split, loop(s), conditional statements
  pass
'''Activity #4
Write a function that inverts the case of all the words in a string.
Precondition(Assumptions): String will either have all lowercase or all uppercase letters
Postcondition(Results): Returns all letters in the opposite case 
lower->upper, upper->lower
Example: hello -> HELLO; HI -> hi '''
def invert_case(string):
  pass
