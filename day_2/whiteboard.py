def lucky_number(arr):

    list_counter = [-1]
    for i in arr:
        if i == arr.count(i):
            list_counter.append(i)

    return max(list_counter)

print(lucky_number([2, 2, 3, 4]))
