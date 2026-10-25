def list_checker(list1: list, num: int) -> bool:
    result = False
    if num in list1:
        result = True
    return result


print(list_checker([0, 1, 3], 1))
print(list_checker([0, 2, 3], 1))
