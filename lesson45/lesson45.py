# Lesson 45
def fruitydict(fruitlist):
    empty_dic = {}

    for fruit in fruitlist:
        empty_dic[fruit] = len(fruit)
    return empty_dic

testy_test = fruitydict(['apple', 'banana', 'pineapple', 'cherry', 'kiwi'])
print(testy_test)