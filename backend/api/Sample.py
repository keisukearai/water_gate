data = '052003021754543f8c31ffea0700070f000000000000000000000000000000000000000000000000000000'

# d1 = data[0:2]
# print(d1)

# d2 = data[2:4]
# print(d2)

# d3 = data[4:6]
# print(d3)

# h = hex('3f')
# print(h)
# hex_num = 0x3f

hex_s = "0x8c"
hex_i = int(hex_s, 16)
hex_n = hex(hex_i)
print(type(hex_n))
print(hex_n)

n_bin = format(hex_i, "08b")
print(type(n_bin))
print(n_bin)
