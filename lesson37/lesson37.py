# Lesson 37
def stringcompress(text):
    result = ''
    counter = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            counter += 1
        else:
            result += text[i-1]
            result += str(counter)
            counter = 1
    result += text[-1] + str(counter)

    if len(result) >= len(text):
        return text
    else:
        return result

tester = stringcompress("aajjkkiiiilloooooooo")
print(tester)