import base64
import re

lmark = "eval MIME::Base64::decode"
sp = 'decode.\"(.+)\".;'
output = ""
count2 = 0

with open("bowie.pl","r") as f:
	data = f.read()

p = re.compile(sp)
m = p.findall(data)


def analyze(word):
	import __main__
	word = base64.b64decode(word)
	with open(str(__main__.count2)+".txt","w") as f:
		f.write(word)

	mm = p.findall(word)
	for y in mm:
		num = word.find(y)
		if word[num-25-2:num-2]==lmark:
			__main__.count2 += 1
			analyze(y)
			return 

def main():
	output2 = ""
	strings = data
	for x in m:
		num = strings.find(x)
		if strings[num-25-2:num-2]==lmark:
			with open("00.gif","w") as f:
				f.write(output2)
			analyze(x)		
			break
		else:
			output2 += base64.b64decode(x)

main()

