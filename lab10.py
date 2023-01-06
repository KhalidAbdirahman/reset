import turtle

def mystery(lst):
    if lst == []:
        return []
    else:
        return [lst[0]-5] + mystery(lst[1:])

#warmup 1
def mystery2(lst):
    final = []
    for i in range(len(lst)):
        answer1 = lst[0] - 5
        final.append(answer1)
        lst = lst[1:]
    return final




#warmup 2
def sum_list(vals):
    if vals == []:
        return 0
    else:
        return vals[0] + sum_list(vals[1:])



#warmup 3
def reverse_string(lst):
    if lst == '':
        return ''
    else:
        return lst[-1] + reverse_string(lst[:-1])


#stretch 1
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

#stretch 2
def double_reverse(str_list):
    if str_list == []:
        return []
    else:
        return (double_reverse((str_list[1:]))) + [reverse_string((str_list[0]))]

#workout1
def deep_square(lst):
    if lst == []:
        return []
    else:
        if type(lst) == int:
            return [lst**2]
        if type(lst[0]) == list:
            return [deep_square(lst[0])] + deep_square(lst[1:])
        else:
            return [lst[0]**2] + deep_square(lst[1:])

#print(deep_square([1,[2],[3,4,5],6]))
#workout2
def flat_square(lst):
    if lst == []:
        return []
    else:
        if type(lst) == int:
            return [lst**2]
        if type(lst[0]) == list:
            return flat_square(lst[0]) + flat_square(lst[1:])
        else:
            return [lst[0]**2] + flat_square(lst[1:])


print(flat_square([1,[2],[3,4,5],6]))


# def tree(t, trunk_length):
#     if trunk_length < 0:
#         return 
#     else:
#         t.forward(trunk_length)
#         t.right(30)
#         tree(t, trunk_length-15)
#         tree(t, trunk_length-15)
#         t.left(60)
#         tree(t, trunk_length-15)
#         tree(t, trunk_length-15)
#         t.right(30)
#         t.backward(trunk_length)


# tree_turtle = turtle.Turtle()
# tree_turtle.left(90)
# tree_turtle.speed(0)
# tree(tree_turtle,100)
# turtle.exitonclick()



