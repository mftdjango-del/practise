from random import  choice

def group_list(seq , size):
    group = []
    coll = range(0 , len(seq) , size)
    for i in coll:
        group.append(seq[i : i + size])
    return group


def create_random_code(size):
    var = ""
    for item in range(size):
        var += str(choice(range(10)))
    return var