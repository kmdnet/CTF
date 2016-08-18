import base64

x = "MDgxOTE2MjMwZTMxMDIzMTNhNjk2YjA3NjgzNjM0MjE2YTJjMzA2ODJiNmIwNzBmMzA2ODA3MTMz\nNjY4MmYwNzJmMzA2YjJhNmI2YTM0Njg2ODMzMjU="
work = []
flag = ""

base = base64.b64decode(x)

for i in range(0,len(base),2):
    work.append(base[i:i+2])


for y in work:
    flag += chr(int(y,16) ^ 0x58)


print flag
