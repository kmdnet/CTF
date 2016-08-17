def decode(arg):
	try:
		eax = arg
		ebp_38 = 0
		ebp_34 = 0

		while ebp_34 - 0x28 <= 0:
			ebp_30 = 0

			eax = ord(arg[ebp_34])
			eax ^= 0x33
			eax &= 0xFF
			ebp_30 = eax

			# func1 GetCurrentProcess -> CheckRemoteDebuggerPresent()
			edx  = ebp_30
			edx += 0x44
			edx &= 0xFF
			ebp_30 = edx

			# func2 FindWindowW "OLLYDBG"
			ecx  = ebp_30
			ecx ^= 0x55
			ecx &= 0xFF
			ebp_30 = ecx

			# func3 IsDebuggerPresent
			eax  = ebp_30
			eax -= 0x66
			eax &= 0xFF
			ebp_30 = eax

			# func4 
			edx  = ebp_38
			edx &= 0xFF
			edx ^= ebp_30
			edx &= 0xFF

			ebp_30 = edx
			eax  = ebp_34
			ecx  = password[eax]
			ecx &= 0xFF
			if ecx != ebp_30:
				return ebp_34

			edx  = ebp_38
			edx += ebp_30
			ebp_38 = edx
			
			ecx  = ebp_34
			ecx += 0x1
			ebp_34 = ecx

		return True
	except:
		return ebp_34


password = [ \
0x8C,\
0x0F1,\
0x53,\
0x0A3,\
0x8,\
0x0D7,\
0x0DC,\
0x48,\
0x0DB,\
0x0C,\
0x3A,\
0x0EE,\
0x15,\
0x22,\
0x0C4,\
0x0E5,\
0x0C9,\
0x0A0,\
0x0A5,\
0x0C,\
0x0D3,\
0x0DC,\
0x51,\
0x0C7,\
0x39,\
0x0FD,\
0x0D0,\
0x0F8,\
0x3B,\
0x0E8,\
0x0CC,\
0x3,\
0x6,\
0x43,\
0x0F7,\
0x0DA,\
0x7E,\
0x65,\
0x0AE,\
0x80 ]


def main():
	word = ""
	for i in range(0,40):
		for x in range(33,126):
			word += chr(x)
			res = decode(word)
			if res > i:
				break
			word = word[:-1]
	
	print word


main()
