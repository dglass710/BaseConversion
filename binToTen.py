def main(a):
    'Takes a binary as an int and returns an int of equal value in base ten'
    for char in str(a):
        if char not in ('0', '1'):
            raise Exception(f'This number contains the digit {char} which is not 0 or 1')
    aBaseTen = 0
    power = 0
    for digit in reversed(str(a)):
        aBaseTen += 2 ** power * int(digit)
        power += 1
    return aBaseTen 
