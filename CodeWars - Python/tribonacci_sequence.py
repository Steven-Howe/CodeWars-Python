def tribonacci(signature, x):
    if not x:
        return []
    elif x < len(signature):
        return signature[:x]
    else:
        n = 0
        while n < x - 3 and n != len(signature):
            total = signature[n] + signature[n + 1] + signature[n + 2]
            signature.append(total)
            n += 1

    return signature