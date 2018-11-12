clear = '\033[2K\r'


def binary_search(func, lo=0, hi=1000, threshold=1, label='binary search'):
    print(f'{label}: binary search', end='', flush=True)
    result = [0, 8000000]
    while abs(hi - lo) > threshold:
        mid = (hi - lo) // 2 + lo
        res = func(mid)
        if res:
            print(f'{clear}{label}: lo={lo} mid={mid} hi={hi}: {res}', end='', flush=True)
            lo = mid
            result = [mid, res]
        else:
            print(f'{clear}{label}: lo={lo} mid={mid} hi={hi}: fail', end='', flush=True)
            hi = mid
    print(clear, end='', flush=True)
    return result
