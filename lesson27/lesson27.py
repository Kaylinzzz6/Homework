# Lesson 27
def is_alpha(string):
    '''
    '''
    result = ''
    for character in string:
        if character.isalpha():
            result += character.lower()
            # + symbol is concatenation, joining two or more strings to form a single new string

    return result
#end of is_alpha

text = is_alpha("09ADUSAH!!@@-090klalalla")
print(f"New text is: {text}")