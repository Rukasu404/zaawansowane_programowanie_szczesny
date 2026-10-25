def list_fusion(list1: list, list2: list) -> list:
    fused_list = list1 + list2
    clear_list = list(set(fused_list))
    return [a ** 3 for a in clear_list]


print(list_fusion([1, 2, 3], [1, 2, 3, 4, 5]))
