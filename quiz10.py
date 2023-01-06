#question 1
def max_even(lst):
    if not lst:
        return 0
    if lst == []:
        return []
    else:
        if lst[0] %  2 != 0:
            return max_even(lst[1:])
        elif lst[0] %  2 == 0:
            return max(lst[0], max_even(lst[1:]))
            
#print(max_even([6, 11, 42, 999]))

def max_even_list(list):
    if not list:
        return []
    if len(list) == 1:
        if list[0] % 2 == 0:
            return list[0]
    if list[0] % 2 == 0:
        return max(list[0], max_even_list(list[1:]))
    else:
        return max_even_list(list[1:])

#print(max_even_list([1,2,3,5,7,11,13]))

def max_even (xs):
  if not xs:
    return 0
  elif xs[0] % 2 == 0:
    return max(xs[0], max_even(xs[1:]))
  else:
    return max_even(xs[1:])

#print(max_even([8,7,10,9,2,3]))


#question 2
student = {
    'name' : 'Emmma',
    '1133' : 10,
    '1933' : 17,
    '2021' : 1000
}
del student['2021']
#print(student)

#question 5
def sum_sq(n):
    if n == 0:
        return (0)
    else:
        return sum_sq(n-1) + (n**2)
#question 5.2
def sum_sq(lst):
    if lst == []:
        return []
    else:
        return [lst[0]**2] + sum_sq(lst[1:])


def maths(x):                #1
    if x % 10 == 0:          #2
        return 12            #3
    elif x > 12:             #4
        return maths(x+8)    #5
    else:                    #6
        return x-2           #7


def sum_sq(n):
    if n == 0:
        return [0]
    else:
        return sum_sq(n-1) + [n**2]

print(sum_sq(1000))