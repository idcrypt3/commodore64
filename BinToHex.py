my_bin = """1111 1111 0000 0000 1000 0000 0010 0000 0100 0100 1110 0101 1010

 1001 0000 1100 1000 1101 1000 0110 0000 0010 1010 1001

 0000 0011 1000 1101 0010 0000 1101 0000 1010 1001 0000

 1011 1000 1101 0010 0001 1101 0000 1010 1001 0000 1000

 1000 1101 0000 0000 0000 0100 1010 1001 0000 0101 1000

 1101 0000 0001 0000 0100 1010 1001 0000 1100 1000 1101

 0000 0010 0000 0100 1000 1101 0000 0011 0000 0100 1010

 1001 0000 1111 1000 1101 0000 0100 0000 0100 0110 0000"""

def encrypt(string, length):
    return ' '.join(string[i:i+length] for i in range(0, len(string), length))

my_bin = my_bin.rstrip()
my_bin = my_bin.replace("\n", "")
my_bin = my_bin.replace(" ", "")

b = hex(int(my_bin, 2))[2:].zfill(2)

new_hex = encrypt(b[2:], 4)
print(new_hex)
