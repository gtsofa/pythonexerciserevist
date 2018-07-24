def swap(s):
    
    if not s:
        return 'list is empty'

    if all(isinstance(item, int) for item in s):
        return list(reversed(s))

    if all(isinstance(item, str) for item in s):
        return [item.upper() for item in s]

    else:
        return s
