#!/usr/bin/python3
from collections import defaultdict
from fixedxor import fixed_xor_hexstr


def char_freq(hexstr):
	d = defaultdict(lambda : 0)
	for i in range(0, len(hexstr), 2):
		d[hexstr[i:i+2]]+=1
	return d

def char_freq_to_ascii_freq(char_freq):
	return {chr(int(x, 16)): char_freq[x] for x in char_freq}

def asciify(hexstr):
	return "".join([chr(int(hexstr[i:i+2], 16)) for i in range(0, len(hexstr), 2)])

def int2paddedhex(num, pad):
	h = hex(num)[2:]
	return h.rjust(pad, '0')

hexstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
nbytes = len(hexstr) // 2

ascii_map_dict = {}
char_freq_dict = {}
for i in range(256):
	singlexor = nbytes * int2paddedhex(i, 2)
	xored = fixed_xor_hexstr(hexstr, singlexor)
	ascii_map_dict[i] = asciify(xored)
	char_freq_dict[i] = char_freq(xored)


for key, freq in char_freq_dict.items():
	if '65' in freq:
		print(key, char_freq_to_ascii_freq(freq))

# Be lazy and look
# Could compare to printable chars and match with above freq analysis
#import pprint
#pprint.pprint(ascii_map_dict)

print("answer: {}".format(ascii_map_dict[88]))
