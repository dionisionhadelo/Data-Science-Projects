def generate_hale_seq(num):
    lnum = [num]
    while num != 1:
        if (num%2) == 0:
            num = num//2
            lnum.append(num)
        else:
            num = (num * 3) + 1
            lnum.append(num)
    return lnum

print(generate_hale_seq(10))