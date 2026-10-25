def sum_check(num1: int, num2: int, num3: int) -> bool:
    total = num1 + num2
    result = total >= num3
    return result


print(sum_check(6, 3, 9))
print(sum_check(3, 3, 9))
