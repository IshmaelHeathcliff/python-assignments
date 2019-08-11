def vector_multiple(lst1, lst2):
    for i in range(len(lst1)):
        assert isinstance(lst1[i], int), 'Please check'
    for i in range(len(lst2)):
        assert isinstance(lst2[i], int), 'Please check'
    if len(lst1) != len(lst2):
        return None
    else:
        product = 0
        for i in range(len(lst1)):
            product += lst1[i] * lst2[i]
        return product

print(vector_multiple([1, 2, 3], [2, 3, 'a']))
