#!/usr/bin/python3

# Takes 2 hexstring and xors them returning 3rd hex string
def fixed_xor_hexstr(h1, h2):
	xor = int(h1, 16) ^ int(h2, 16)
	return hex(xor)[2:]

if __name__ == "__main__":
	import sys
	if len(sys.argv) < 3:
		print("fixed_xor_hexstr('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')")
		print(fixed_xor_hexstr('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))
	else:
		print(fixed_xor_hexstr(sys.argv[1], sys.argv[2]))
