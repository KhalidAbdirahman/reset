# def first_letter(file):
#     fp = open('simple.txt')
#     text = fp.read()
#     tokens = text.split()
#     counting = {}
#     for token in tokens:

#         if token[0] in counting:
#             counting[token[0]] += 1
#         else:
#             counting[token[0]] = 1
#     print(counting)
#     fp.close()

#______________________________________________________________________
# def sum_values(pairs):
#     total = 0
#     for tup in pairs.items():
#         total += tup[1]
#     return total





#______________________________________________________________________

# def smallest_merge(dict_one,dict_two):
#     counts = {}
#     for tup in dict_one.items():
#         for tup_two in dict_two.items():
#             if tup[0] == tup_two[0]:
#                 minimum = min(tup[1],tup_two[1])
#                 counts[tup[0]][minimum]
                
    #return counts
                
#______________________________________________________________________

def smallest_merge(dict_one,dict_two):
    merged = dict_one.copy()
    final = {}
    for tup in merged.items():
        for tup_two in dict_two.items():
            if tup[0] == tup_two[0]:
                minimum = min(tup[1],tup_two[1])
                [tup][minimum]

    return final
#______________________________________________________________________


def smallest_merges(dict_one,dict_two):
    merged = dict_one.copy()
    final = {}
    for tup in merged.items():
        for tup_two in dict_two.items():
            if tup[0] == tup_two[0]:
                minimum = min(tup[1],tup_two[1])
                final[tup[0]] = minimum
            elif tup[0] != tup_two[0]:
                return dict_two.update(merged)

    return final
                
#______________________________________________________________________


def smallest_merge(dict_one,dict_two):
    final = {}

    for value in dict_one:
        for value_2 in dict_two:
            if value in value_2:
                minimum = min(dict_one[value], dict_two[value_2])
                final[value] = minimum
                
            elif value not in dict_two:
                final[value] = dict_one[value]
                final[value_2] = dict_two[value_2]


    return final


print(smallest_merge({"Sam": 11, "Victoria": 99, "Nick":100}, {"Sam": 11, "Scot": 99, 'Jacquelyn': 1000}))
