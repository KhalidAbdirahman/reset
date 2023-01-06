

# def mystery(nested_list):
#     total = 0
#     #looping through each elements in nested_list
#     for inner in nested_list:
#         for ele in inner:
#             total += ele
#     return total

# def mystery2(nested_list):
#     total = 0
#     #looping through each of the elements based on the index of each elements 
#     for i in range(len(nested_list)):
#         for j in range(len(nested_list[i])):
#             #adding each value to total
#             total+=nested_list[i][j]
#     return total
# #calling function 
# print(mystery2([[1,2,3],[4,5,6]]))
# print(mystery([[1,2,3],[4,5,6]]))



def get_evens(nested_list):
    final = []
    for list_i in nested_list:
        count = 0
        for list_j in list_i:
            if list_j % 2 == 0:
                count = count + 1
        final.append(count)
    return final

print(get_evens([[-20, 10, 2, 4, 5], [4], [8, 25, 10], [7]]))