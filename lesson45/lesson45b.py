def fibconfirm(integer):
    empty_dic = {0:0, 1:1}
    if integer in empty_dic:
        return empty_dic
    else:
        for nums in range(2, integer+1):
            empty_dic[nums] = empty_dic[nums-1] + empty_dic[nums-2]
        return empty_dic

testerrr = fibconfirm(11)
print(testerrr)
