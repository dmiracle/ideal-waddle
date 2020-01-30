import math

def rank(permutation, line_num=1):
    N = len(permutation)
    if N == 1:
        return line_num
    d = permutation.pop(0)
    inc = (d - 1) * math.factorial(N - 1)
    line_num = (line_num + inc)
    permutation = [x - 1 if x > d else x for x in permutation]
    return rank(permutation, line_num)

def unrank(line_num, num_elements, permutation = []):
    N = num_elements - 1    
    d = (line_num // math.factorial(N)) + 1
    next_line_num = line_num - (d - 1) * math.factorial(N)
    sorted_permutation = permutation.copy()
    sorted_permutation.sort()
    for el in sorted_permutation:
        if el <= d:
            d += 1
    permutation.append(d)

    if N == 0:
        return permutation
    else:
        print("Next with: ", next_line_num, N, permutation)
        return unrank(next_line_num, N, permutation)
        