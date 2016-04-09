import string
# I'm not cheating, Python's ability to manipulate low level datatypes is poor
from bitstring import BitArray

msg = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"

def xor(char, key):
    # OK, assuming our input is good we can do an XOR
    # if one or other, then one. if both, then 0 - without using Python's XOR operator!
    hex1 = hex(ord(char))
    hex2 = hex(ord(key))
    b1, b2 = BitArray(hex1), BitArray(hex2)
    # print "b1: %s, b2: %s" % (b1, b2),
    res = BitArray('0b00000000')
    # print "hex1: %s, hex2: %s, res: %s" % (hex1, hex2, res), 
    for j in range(0, 8):
        # print j, b1[j:j+1],
        if b1[j:j+1] == '0b1' and b2[j:j+1] == '0b1':
            res[j:j+1] = '0b0'
        else:
            if b1[j:j+1] == '0b1' or b2[j:j+1] == '0b1':
                res[j:j+1] = '0b1'
    return res.hex

encoded_msg = ""
i = 0
for c in msg:
    encoded_msg += xor (c, key[i])
    i += 1
    if i == len(key):
        i = 0
print encoded_msg   