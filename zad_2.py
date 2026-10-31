def numbers(numbers_array):
    array = []
    for a in numbers_array:
        a *= 2
        array.append(a)
    return array


def numbers2(numbers_array):
    return [a * 2 for a in numbers_array]


list1 = [1, 2, 3, 4, 5]

print(numbers(list1))
print(numbers2(list1))
