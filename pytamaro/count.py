def is_empty(a: list):
    return not a

def count(a: list):
    if is_empty(a): 
        return 0
    else:
        return 1+count(a[:-1])
