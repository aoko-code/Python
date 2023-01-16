def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):
    odd_list=[]
    for i in list:
        if func(i):
            odd_list.append(i)
    return odd_list

aList = range(1, 20)

print(change_list(aList, is_it_odd))