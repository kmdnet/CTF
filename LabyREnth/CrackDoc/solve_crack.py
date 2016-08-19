password = [171,184,42,184,88,26,47,154,20,219,203,130,52,19,180,214,156,94,186,74,30,248,119,235,139,130,175,141,179,197,8,204,252]


def decode(strings):
    s = [178, 192, 199, 24, 97, 196, 254, 31, 188, 102, 214, 245, 205, 39, 211, 204, 21, 229, 253, 163, 115, \
     194, 154, 63, 37, 46, 209, 88, 66, 103, 19, 73, 130, 114, 158,78, 49, 92, 119, 146, 32, 12, 153, 203, \
     81, 242, 84, 239, 129, 34, 183, 43, 91, 171, 162, 71, 128, 218, 121, 137, 45, 85, 56, 233, 150, 151, \
     255, 167, 42, 35, 17, 133, 107, 185, 117, 200, 215, 210,13, 28, 8, 104, 74, 108, 244, 227, 54, 9, 68, \
     41, 64, 72, 106, 168, 61, 220, 186, 6, 93, 142, 157,57, 156, 248, 18, 232, 234, 181, 159, 110, 236, 126, \
     62, 70, 76, 138, 105, 155, 251, 177, 247, 22, 89, 176, 0, 182, 52, 27, 29, 216, 100, 206, 15, 195, 202, \
     179, 217, 23, 252, 65, 207, 161, 44, 243, 95, 131, 47, 1, 201, 98, 250, 67, 38, 198, 189, 224, 20, 58, 213, \
     96, 77, 127,174, 125, 240, 86, 187, 184, 222, 228, 148, 25, 94, 219, 55, 191, 5, 109, 246, 113, 101, 3, 122, \
     48, 175, 170, 40, 223, 144, 36, 123, 30, 120, 26, 169, 135, 164, 197, 53, 134, 208, 112, 147, 124, 16, 83, 180, \
     172, 149, 87, 132, 2, 51, 230, 69, 139, 50, 212, 160, 166, 165, 82, 75, 235, 140, 80, 193, 10, 173, 14, 59, 116, \
     99, 136, 152, 60, 226, 145, 111, 190, 225, 249, 237, 79, 11, 33, 4, 90, 231, 241, 221, 141, 238, 7, 118, 143]
    
    num = len(strings)
    x = 0
    y = 189
    ret = []
    
    for  i in range(1,num+1):
        x = (x+1) % 256
        y = (y + s[x]) % 256
        tmp = s[x]
        s[x] = s[y]
        s[y] = tmp

        ret.append(s[(s[x]+s[y]) % 256] ^ ord(strings[i-1:i]))
    return ret


def check(array):
    num = len(array)
    if password[num-1] != array[num-1]:
            return False
    return True


def main():
    word  = ""
    
    for i in range(0,len(password)):
        for x in range(33,126):
            word += chr(x)
            res = decode(word)
            if check(res):
                break
            word = word[:-1]

    print word

    
if __name__ == '__main__':
    main()
