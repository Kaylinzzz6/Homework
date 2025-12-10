# Lesson 44
def alphafreq(stringy):
    listedstringy = sorted(stringy.lower())
    empty_dic = {}

    for alphas in stringy:
        if alphas not in empty_dic:
            empty_dic[alphas] = 1
        else:
            empty_dic[alphas] += 1

    return empty_dic

answer = alphafreq("ajskdljaklsd")
print(answer)