def main(a):
    'Takes a positive int in base ten and returns the binary with an equal value'
    power = 0
    numStr = ''
    while 2 ** (power + 1) < a:
        power += 1
    while power >= 0:
        if 2 ** power < a + 1:
            numStr += '1'
            a -= 2 ** power
        else:
            numStr += '0'
        power -= 1
    return int(numStr)
