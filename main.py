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
def shortest_word(string):
    cleaned_string = string.replace(',', '').replace('.', '')
    
    words_to_ignore = {"and", "or", "the", "from", "for", "to"}
    
    words = cleaned_string.split()

    shortest = None
    for word in words:
        if word.lower() not in words_to_ignore:
            if shortest is None or len(word) < len(shortest):
                shortest = word
    
    return shortest

'''Activity #4
Write a function that inverts the case of all the words in a string.
Precondition(Assumptions): String will either have all lowercase or all uppercase letters
Postcondition(Results): Returns all letters in the opposite case 
lower->upper, upper->lower
Example: hello -> HELLO; HI -> hi '''
def invert_case(string):
  if string[0].isLower():
    return string.lower()
  else:
      return string.lower()
      
