def group_list(seq , size):
    group = []
    coll = range(0 , len(seq) , size)
    for i in coll:
        group.append(seq[i : i + size])
    return group