
'''
    https://www.rapidtables.com/convert/number/roman-numerals-converter.html
    This program will convert 0 < x < 4999 to roman. 
    Conversion mapping is taken from above link.
'''
import sys

def i_to_r(number):
    int_val = [ 1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4, 1
              ]
    rom_val = [ "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"
              ]

    roman = ''
    i = 0
    while  number > 0:
        for rng in range(number // int_val[i]):
            roman += rom_val[i]
            number -= int_val[i]
        i += 1
    return roman


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("%s to Roman: %s" % (sys.argv[1], i_to_r(int(sys.argv[1]))))
    else:
        print("4678 to Roman: %s" % (i_to_r(4678)))
        print("\n\nProvide int number  as a command line argument...")
        print("0 < number < 4999")
