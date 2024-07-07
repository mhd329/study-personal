hex_c = "0x"+input()

char = int(hex_c, 16) # A ~ F

for i in range(1, 16):
    print("%X"%char, '*', "%X"%i, '=', "%X"%(char * i), sep = '')