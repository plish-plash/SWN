
table_len = 256
max_value = 254

for j in range(9):

    buf = ""

    for i in range(table_len):
        if buf:
            buf += ","
        val = i / table_len
        if val <= 0.5:
            val = val / 0.5
        else:
            val = 1.0 - ((val - 0.5) / 0.5)
        if j < 4:
            val = pow(val, 2 - (j / 4))
        elif j > 4:
            val = pow(val, 1 - ((j - 4) / 8))
        buf += str(int(val * max_value))

    print("{%s}" % (buf))
