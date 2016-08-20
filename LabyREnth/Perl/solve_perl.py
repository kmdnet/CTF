import base64
import re

lmark = "eval MIME::Base64::decode"
sp = 'decode.\"(.+)\".;'

data = ""
output = ""
result = ""
p = re.compile(sp)


for num in range(0,20):
	with open(str(num)+".txt","r") as f:
		data = f.read()

	m = p.findall(data)
	for x in m:
		n_m = data.find(x)
		if data[n_m-25-2:n_m-2]!=lmark:
			output += base64.b64decode(x)


with open("00.gif","r") as f:
	data = f.read()


result = data + output
with open("entrevue.gif","w") as f:
	f.write(result)

