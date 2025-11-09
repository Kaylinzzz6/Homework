# Lesson 35
def dupremover(a_list):
    new_list = []
    for nums in a_list:
        if nums is not in a_list:
            new_list.append(nums)
            