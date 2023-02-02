
def NOT(value):
    return -value
def AND(val1, val2):
    return val1 & val2
def OR(val1, val2):
    return val1 | val2
def XOR(val1, val2):
    return val1 ^ val2
def shiftleft(val, num):
    return val << num
def shiftright(val, num):
    return val >> num
def bit(val, idx):
    mask = 1 << idx
    return bool(val & 1)
def setbit(val, idx):
    mask = 1 << idx
    return val | mask
def zerobit (val, idx):
    mask = -(1 << idx)
    return val & mask
def listbits(val):
    num = len(bin(val)) - 2
    result = []
    for i in range(num):
        result.append(1 if bit(val, i) else 0)
    return list(reversed(result))

