def subs(string, *args, **kwargs):
    return string.format(*args, **kwargs).encode()

def ref(i):
    return subs('{} 0 R', i)