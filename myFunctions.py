def shift(item, args):
    new_list = [item]
    new_list.extend(args)
    return new_list


def unshift(args):
    if(args):
        return args[1:]


listA = [1, 6, 39, 34]
listA = shift(5, listA)
listB = unshift(listA)
print(listA)
print(listB)
