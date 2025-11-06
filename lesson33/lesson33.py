def meanymedian(a_list):
    mean = sum(a_list) / len(a_list)
    #sort out for median
    new_list = []
    while len(a_list) > 0:
        smallest = min(a_list)
        new_list.append(smallest)
        a_list.remove(smallest)

    if len(new_list) % 2 == 0:
        upper = len(new_list) // 2 
        lower = (len(new_list) // 2) - 1
        median = (new_list[lower] + new_list[upper]) / 2
    else:
        median = new_list[len(new_list) // 2]
    return mean, median

testy = meanymedian([2,2,4,5,7,6])
print(testy)